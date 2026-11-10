using Shipstick.Items;

namespace Shipstick.Ship;

/// <summary>
/// The slots in the wall between two neighbouring capsules: one inventory, reached from both sides, and the only way
/// anything passes between them (GAM-3, SHP-2).
/// </summary>
public sealed class Door(CapsuleAt first, CapsuleAt second, Inventory inventory)
{
    public CapsuleAt First { get; } = first;

    public CapsuleAt Second { get; } = second;

    public Inventory Inventory { get; } = inventory;

    /// <summary>The capsule on the other side from <paramref name="from"/>.</summary>
    public CapsuleAt Across(CapsuleAt from) => from == First ? Second : First;
}
