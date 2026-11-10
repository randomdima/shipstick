namespace Shipstick.Items;

/// <summary>
/// A kind of item, named by its catalogue id (<c>wat-001</c>). <see cref="None"/>, the default, is the kind of an empty
/// slot and is never carried.
/// </summary>
/// <remarks>
/// An item holds only its id: what it is called and what it does are the catalogue's (economy/), looked up by whoever
/// needs them. Whether an id names a real item is checked where one comes in from outside the game — an admin's edit.
/// </remarks>
public readonly record struct Item(string? Id)
{
    public static Item None => default;

    public override string ToString() => Id ?? "none";
}

/// <summary>What one slot holds: one kind of item and how many of it (ITM-2).</summary>
public readonly record struct Stack(Item Item, int Count)
{
    public bool IsEmpty => Count == 0;
}

/// <summary>
/// The items a slot accepts by hand (ITM-4). The default filter is universal: a slot nobody set a filter on takes
/// anything, as a chest's and a door's do; a device's layout narrows its own.
/// </summary>
/// <remarks>
/// Kept as the set accepted, null for universal, so <c>default</c> refuses nothing. A filter binds only a player's
/// move: a slot's owner fills it regardless (<see cref="Inventory.TryAdd"/>), which is how a device's output slot,
/// refusing every item, is filled.
/// </remarks>
public readonly struct SlotFilter : IEquatable<SlotFilter>
{
    readonly Item[]? accepted;

    SlotFilter(Item[] accepted) => this.accepted = accepted;

    /// <summary>Every item.</summary>
    public static SlotFilter Universal => default;

    /// <summary>No item by hand: a device's output, emptied by hand and filled only by the device.</summary>
    public static SlotFilter TakeOnly => new([]);

    /// <summary>The given items and no other.</summary>
    public static SlotFilter Only(params ReadOnlySpan<Item> items) =>
        new([.. items.ToArray().Where(item => item != Item.None).Distinct()]);

    public bool IsUniversal => accepted is null;

    public bool Accepts(Item item) => item != Item.None && (accepted is null || Array.IndexOf(accepted, item) >= 0);

    /// <summary>The items it accepts; empty for a universal filter, which accepts every item (<see cref="IsUniversal"/>).</summary>
    public Item[] Accepted() => accepted is null ? [] : [.. accepted];

    public bool Equals(SlotFilter other) =>
        accepted is null ? other.accepted is null : other.accepted is not null && accepted.SequenceEqual(other.accepted);

    public override bool Equals(object? obj) => obj is SlotFilter other && Equals(other);

    public override int GetHashCode() => accepted is null ? 0 : accepted.Length;
}
