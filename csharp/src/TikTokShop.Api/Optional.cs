using System;

namespace TikTokShop.Api;

/// <summary>
/// An argument that may be left out. <c>default</c> (and an omitted argument) means "keep the current value";
/// any value, including <c>null</c>, means "use this value".
/// </summary>
/// <typeparam name="T">The value type.</typeparam>
public readonly struct Optional<T>
{
    private readonly T _value;

    /// <summary>Wraps a value that was given, even if it is <c>null</c>.</summary>
    public Optional(T value)
    {
        _value = value;
        HasValue = true;
    }

    /// <summary>Whether a value was given.</summary>
    public bool HasValue { get; }

    /// <summary>The value given; throws when none was.</summary>
    public T Value => HasValue ? _value : throw new InvalidOperationException("No value was given.");

    /// <summary>The value given, or <paramref name="fallback"/> when none was.</summary>
    public T GetValueOrDefault(T fallback) => HasValue ? _value : fallback;

    /// <summary>Wraps a value that was given.</summary>
    public static implicit operator Optional<T>(T value) => new(value);
}
