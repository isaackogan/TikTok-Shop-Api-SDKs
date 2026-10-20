//! Every operation in the rendered meta is a method on its group; the groups are the canonical ones.
use std::collections::BTreeSet;
use tiktok_shop_api::generated::groups::*;
use tiktok_shop_api::generated::meta::{GROUPS, OPERATIONS};
use tiktok_shop_api::{Options, TikTokShop};

const GROUPS_RS: &str = include_str!("../src/generated/groups.rs");

/// The source of one group's `impl` block.
fn impl_block<'a>(type_name: &str) -> &'a str {
    let start = GROUPS_RS.find(&format!("impl {type_name} {{")).unwrap_or_else(|| panic!("no impl for {type_name}"));
    let rest = &GROUPS_RS[start..];
    // The block ends at the Debug impl that follows it.
    &rest[..rest.find(&format!("impl fmt::Debug for {type_name}")).unwrap()]
}

#[test]
fn every_operation_is_a_method_on_its_group() {
    assert!(!OPERATIONS.is_empty());
    for op in OPERATIONS {
        let group = GROUPS
            .iter()
            .find(|g| g.name == op.group)
            .unwrap_or_else(|| panic!("{}: unknown group {}", op.operation_id, op.group));
        let needle = format!("pub async fn {}(", op.method);
        assert!(
            impl_block(group.type_name).contains(&needle),
            "{} should be {}.{}",
            op.operation_id,
            group.name,
            op.method
        );
    }
}

#[test]
fn no_group_has_a_method_the_meta_does_not_know() {
    for g in GROUPS {
        let in_source = impl_block(g.type_name).matches("pub async fn ").count();
        let in_meta = OPERATIONS.iter().filter(|o| o.group == g.name).count();
        assert!(in_meta > 0, "{} has no operations", g.name);
        assert_eq!(in_source, in_meta, "{}", g.name);
    }
}

/// The canonical group name in snake_case, with "TikTok" as one word (ruling R9).
fn snake(camel: &str) -> String {
    let camel = camel.replace("TikTok", "Tiktok");
    let mut out = String::new();
    for c in camel.chars() {
        if c.is_ascii_uppercase() {
            out.push('_');
            out.push(c.to_ascii_lowercase());
        } else {
            out.push(c);
        }
    }
    out
}

#[test]
fn group_names_are_the_canonical_snake_case_ones() {
    let explicit = [
        "affiliate_creator",
        "affiliate_partner",
        "affiliate_seller",
        "analytics",
        "authorization",
        "customer_engagement",
        "customer_service",
        "event",
        "finance",
        "fulfilled_by_tiktok",
        "fulfillment",
        "logistics",
        "orders",
        "products",
        "promotion",
        "return_and_refund",
        "seller",
        "supply_chain",
        "tools",
    ];
    let text = std::fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/../shared/api-groups.json")).unwrap();
    let tags: serde_json::Map<String, serde_json::Value> = serde_json::from_str(&text).unwrap();
    let from_json: BTreeSet<String> = tags.values().map(|v| snake(v.as_str().unwrap())).collect();
    assert_eq!(from_json, explicit.iter().map(|s| s.to_string()).collect::<BTreeSet<_>>());
    let from_meta: BTreeSet<String> = GROUPS.iter().map(|g| g.name.to_string()).collect();
    assert_eq!(from_meta, from_json);
}

/// Compile-time: each client field has its concrete group type (never a boxed or dynamic one).
#[test]
fn every_group_field_has_its_concrete_type() {
    let c = TikTokShop::new(Options::new("k", "s")).unwrap();
    let _: &AffiliateCreatorApi = &c.affiliate_creator;
    let _: &AffiliatePartnerApi = &c.affiliate_partner;
    let _: &AffiliateSellerApi = &c.affiliate_seller;
    let _: &AnalyticsApi = &c.analytics;
    let _: &AuthorizationApi = &c.authorization;
    let _: &CustomerEngagementApi = &c.customer_engagement;
    let _: &CustomerServiceApi = &c.customer_service;
    let _: &EventApi = &c.event;
    let _: &FinanceApi = &c.finance;
    let _: &FulfilledByTikTokApi = &c.fulfilled_by_tiktok;
    let _: &FulfillmentApi = &c.fulfillment;
    let _: &LogisticsApi = &c.logistics;
    let _: &OrdersApi = &c.orders;
    let _: &ProductsApi = &c.products;
    let _: &PromotionApi = &c.promotion;
    let _: &ReturnAndRefundApi = &c.return_and_refund;
    let _: &SellerApi = &c.seller;
    let _: &SupplyChainApi = &c.supply_chain;
    let _: &ToolsApi = &c.tools;
}
