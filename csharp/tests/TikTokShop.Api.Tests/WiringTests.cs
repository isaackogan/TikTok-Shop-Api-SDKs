using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text.Json;
using Xunit;

namespace TikTokShop.Api.Tests;

public class WiringTests
{
    private static readonly string[] ExpectedGroups =
    {
        "AffiliateCreator", "AffiliatePartner", "AffiliateSeller", "Analytics", "Authorization", "CustomerEngagement",
        "CustomerService", "Event", "Finance", "FulfilledByTikTok", "Fulfillment", "Logistics", "Orders", "Products",
        "Promotion", "ReturnAndRefund", "Seller", "SupplyChain", "Tools",
    };

    private static IEnumerable<PropertyInfo> GroupProperties() =>
        typeof(TikTokShopClient).GetProperties(BindingFlags.Public | BindingFlags.Instance)
            .Where(p => p.PropertyType.Namespace == "TikTokShop.Api.Generated.Api");

    [Fact]
    public void TheGroupNamesArePascalCaseAndMatchTheSharedList()
    {
        // R9: "TikTok" is one word.
        Assert.Equal(ExpectedGroups, GroupProperties().Select(p => p.Name).OrderBy(n => n, StringComparer.Ordinal).ToArray());
        Assert.Equal(ExpectedGroups, Generated.Meta.Groups.Select(g => g.Name).OrderBy(n => n, StringComparer.Ordinal).ToArray());
    }

    [Fact]
    public void TheGroupNamesAreTheSharedCanonicalOnesInPascalCase()
    {
        var shared = Repo.Json("shared", "api-groups.json").EnumerateObject()
            .Select(p => char.ToUpperInvariant(p.Value.GetString()![0]) + p.Value.GetString()![1..])
            .OrderBy(n => n, StringComparer.Ordinal)
            .ToArray();
        Assert.Equal(shared, GroupProperties().Select(p => p.Name).OrderBy(n => n, StringComparer.Ordinal).ToArray());
    }

    [Fact]
    public void EveryGroupIsTheConcreteGeneratedApiClass()
    {
        foreach (var group in Generated.Meta.Groups)
        {
            var property = typeof(TikTokShopClient).GetProperty(group.Name);
            Assert.NotNull(property);
            Assert.Equal(group.ApiType, property!.PropertyType);
            Assert.True(property.PropertyType.IsClass);
            Assert.NotEqual(typeof(object), property.PropertyType);
        }
    }

    [Fact]
    public void EveryOperationIsReachableAsClientGroupMethod()
    {
        Assert.NotEmpty(Generated.Meta.Operations);
        foreach (var op in Generated.Meta.Operations)
        {
            var group = typeof(TikTokShopClient).GetProperty(op.Group);
            Assert.True(group is not null, $"{op.OperationId}: no group property {op.Group}");
            var method = group!.PropertyType.GetMethods(BindingFlags.Public | BindingFlags.Instance)
                .Any(m => m.Name == op.OperationId + "Async");
            Assert.True(method, $"{op.OperationId}: {group.PropertyType.Name} has no {op.OperationId}Async");
        }
    }

    [Fact]
    public void EveryOperationBelongsToAKnownGroup()
    {
        var names = Generated.Meta.Groups.Select(g => g.Name).ToHashSet();
        Assert.All(Generated.Meta.Operations, op => Assert.Contains(op.Group, names));
    }
}
