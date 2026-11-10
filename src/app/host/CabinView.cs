using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Items;
using Shipstick.Ship;

namespace Shipstick.App.Host;

/// <summary>
/// One capsule's floor as a client draws it: its fixtures and the doors in its walls, with every slot they hold. Sent as
/// JSON, so a client never holds a game type (HST-4). What a fixture or an item is called is the codex's, looked up by
/// id.
/// </summary>
/// <remarks>
/// <b>A player's cabin names no capsule beyond its doors (WEB-1):</b> <see cref="Seated"/> leaves every door's
/// <see cref="DoorView.Beyond"/> null, and the JSON drops a null, so it never reaches the player. Where the cabin is on
/// the ship (<see cref="At"/>) both are told, since the ship's walls are drawn round it. The ship's time is not here but
/// in the frame around it, so a view changes only when the floor does.
/// </remarks>
/// <param name="Failing">Whether its life support starved on its last cycle (DEV-3).</param>
sealed record CabinView(int CellsAcross, CapsuleAt At, bool Failing, FixtureView[] Fixtures, DoorView[] Doors)
{
    /// <summary>The cabin as the player seated in it sees it.</summary>
    public static CabinView Seated(Vessel vessel, CapsuleAt seat, WayIndex ways) => Of(vessel, seat, ways, namesBeyond: false);

    /// <summary>The cabin as the admin sees it: the capsule beyond each door as well.</summary>
    public static CabinView Entered(Vessel vessel, CapsuleAt at, WayIndex ways) => Of(vessel, at, ways, namesBeyond: true);

    static CabinView Of(Vessel vessel, CapsuleAt at, WayIndex ways, bool namesBeyond)
    {
        var capsule = vessel.CapsuleOn(at) ?? throw new ArgumentOutOfRangeException(nameof(at), at, "no capsule there");
        var doors = new List<DoorView>();
        for (var side = Side.North; side <= Side.West; side++)
            if (capsule.DoorOn(side) is { } door)
                doors.Add(new DoorView(side, namesBeyond ? door.Across(at) : null, InventoryView.Of(vessel, door.Inventory)));

        return new CabinView(vessel.CellsAcross, at, IsFailing(capsule),
            [.. capsule.Fixtures.Select(fixture => FixtureView.Of(vessel, fixture, ways))], [.. doors]);
    }

    /// <summary>Whether the capsule's life support starved on its last cycle (DEV-3).</summary>
    public static bool IsFailing(Capsule capsule) =>
        capsule.Fixtures.Any(f => f.Entry?.Id == Catalogue.LifeSupport && f.Device?.Last == CycleOutcome.Starved);
}

/// <summary>
/// A fixture on the floor. <see cref="Kind"/> is its catalogue device id; a holding fixture has no <see cref="Way"/>,
/// no <see cref="Layout"/> and no cycle.
/// </summary>
/// <param name="Way">The way it runs, by its <see cref="WayIndex"/>.</param>
sealed record FixtureView(
    FloorArea Area,
    string Kind,
    int? Way,
    LayoutView[] Layout,
    CycleOutcome Last,
    Item ShortOf,
    double CycleS,
    double DueS,
    InventoryView Inventory)
{
    public static FixtureView Of(Vessel vessel, Fixture fixture, WayIndex ways)
    {
        var kind = fixture.Entry?.Id ?? "";
        if (fixture.Device is not { } device)
            return new FixtureView(fixture.Area, kind, null, [], CycleOutcome.NotYet, Item.None, 0, 0,
                InventoryView.Of(vessel, fixture.Inventory));
        var layout = device.Layout.Select(g => new LayoutView(g.Use, g.Item, g.Count, g.Slots.Start.Value, g.Slots.End.Value));
        return new FixtureView(fixture.Area, kind, ways[device.Way], [.. layout], device.Last, device.ShortOf(),
            device.CycleS, device.DueS, InventoryView.Of(vessel, fixture.Inventory, device));
    }
}

/// <summary>A run of a device's slots, from <see cref="From"/> up to <see cref="To"/>, and what it holds (DEV-4).</summary>
sealed record LayoutView(SlotUse Use, Item Item, int Count, int From, int To);

/// <summary>A door in one wall; <see cref="Beyond"/> is the capsule it opens on, known to the admin alone.</summary>
sealed record DoorView(Side Side, CapsuleAt? Beyond, InventoryView Inventory);

sealed record InventoryView(int Id, SlotView[] Slots)
{
    /// <param name="device">The device that owns the inventory, if one does: it says what each slot holds.</param>
    public static InventoryView Of(Vessel vessel, Inventory inventory, Device? device = null)
    {
        var slots = new SlotView[inventory.Slots];
        for (var slot = 0; slot < slots.Length; slot++)
        {
            var (item, count) = inventory[slot];
            var filter = inventory.FilterOf(slot);
            slots[slot] = new SlotView(item, count, filter.IsUniversal, filter.Accepted(), device?.SlotItem(slot));
        }

        return new InventoryView(vessel.IdOf(inventory), slots);
    }
}

/// <summary>
/// A slot's stack and its filter: universal, or the items it accepts by hand — none for a device's output.
/// <see cref="Holds"/> is the one item a device's slot holds, its output's too, and none for a closed one; null for a
/// chest's or a door's.
/// </summary>
sealed record SlotView(Item Item, int Count, bool Universal, Item[] Accepts, Item? Holds);
