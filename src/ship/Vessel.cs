using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Items;

namespace Shipstick.Ship;

/// <summary>
/// The ship as it runs: its capsules, the doors between them, every inventory aboard by id, and the clock that cycles
/// the devices (GAM-7).
/// </summary>
/// <remarks>
/// <para>
/// <b>Time moves only by <see cref="AdvanceTo"/>.</b> Each device's cycle is an event due at <see cref="Device.DueS"/>;
/// an advance runs every event due by then, in due order and ties in the order they were scheduled, so the same
/// actions at the same times give the same ship however the advances fall (SHP-3).
/// </para>
/// <para>
/// An inventory's id is its place in the order it came aboard, stable for the ship's life; a client names slots by it.
/// </para>
/// </remarks>
public sealed class Vessel
{
    readonly Capsule?[] capsules;
    readonly List<Door> doors = [];
    readonly List<Inventory> inventories = [];
    readonly Dictionary<Inventory, int> ids = new(ReferenceEqualityComparer.Instance);
    readonly Dictionary<Inventory, Device> devices = new(ReferenceEqualityComparer.Instance);
    readonly PriorityQueue<(Device Device, int Generation), (double DueS, long Order)> due = new();
    long scheduled;

    public Vessel(ShipGrid grid, int cellsAcross)
    {
        Grid = grid;
        CellsAcross = cellsAcross;
        capsules = new Capsule?[grid.Columns * grid.Rows];
    }

    public ShipGrid Grid { get; }

    /// <summary>The cells along one side of every capsule's floor.</summary>
    public int CellsAcross { get; }

    /// <summary>The ship time of the last advance.</summary>
    public double NowS { get; private set; }

    public IReadOnlyList<Door> Doors => doors;

    public Capsule? CapsuleOn(CapsuleAt at) => Grid.Holds(at) ? capsules[Grid.IndexOf(at)] : null;

    /// <summary>Every capsule placed, in the grid's reading order.</summary>
    public IEnumerable<Capsule> Capsules => capsules.OfType<Capsule>();

    public int IdOf(Inventory inventory) => ids[inventory];

    public Inventory? InventoryOf(int id) => id >= 0 && id < inventories.Count ? inventories[id] : null;

    /// <summary>The device whose inventory has the id, or null for a holding fixture's or a door's.</summary>
    public Device? DeviceOf(int id) => InventoryOf(id) is { } inventory ? devices.GetValueOrDefault(inventory) : null;

    public Capsule Place(CapsuleAt at)
    {
        Grid.Place(at);
        return capsules[Grid.IndexOf(at)] ??= new Capsule(at, CellsAcross);
    }

    /// <summary>Hangs a door of <paramref name="slots"/> slots in every wall two held places share.</summary>
    public void HangDoors(int slots, int stackMost)
    {
        foreach (var capsule in Capsules)
            foreach (var side in (ReadOnlySpan<Side>)[Side.East, Side.South])
            {
                if (CapsuleOn(ShipGrid.Beside(capsule.At, side)) is not { } neighbour || capsule.DoorOn(side) is not null) continue;
                var door = new Door(capsule.At, neighbour.At, Board(Inventory.Open(slots, stackMost)));
                capsule.Hang(side, door);
                neighbour.Hang(ShipGrid.Opposite(side), door);
                doors.Add(door);
            }
    }

    /// <summary>
    /// Walls every capsule round (GAM-10, SHP-7): each edge cell of its floor a <paramref name="wall"/> holding
    /// nothing, or the <paramref name="door"/> where a door is hung, holding that door's own slots (SHP-2). An edge cell
    /// two or more capsules share (<see cref="ShipCell"/>) is one wall section, its one inventory standing in each
    /// (SHP-8).
    /// </summary>
    /// <remarks>Doors are hung first; a cell already stood on is an error, as any overlap is (SHP-5).</remarks>
    public void Enclose(DeviceEntry wall, DeviceEntry door, int stackMost)
    {
        var sections = new Dictionary<(int Column, int Row), Inventory>();
        foreach (var capsule in Capsules)
            for (var row = 0; row < CellsAcross; row++)
                for (var column = 0; column < CellsAcross; column++)
                {
                    if (!capsule.OnEdge(column, row)) continue;
                    var cell = new FloorArea(column, row, 1, 1);
                    if (capsule.DoorAt(column, row) is { } hung)
                        capsule.Stand(new Fixture(cell, hung.Inventory, door, null));
                    else if (sections.TryGetValue(ShipCell(capsule.At, column, row), out var section))
                        capsule.Stand(new Fixture(cell, section, wall, null));
                    else
                        sections.Add(ShipCell(capsule.At, column, row),
                            Stand(capsule.At, new Fixture(cell, Inventory.Empty(stackMost), wall, null)).Inventory);
                }
    }

    /// <summary>
    /// Where a capsule's floor cell lies on the ship's one floor: each capsule starts a cell short of its west and north
    /// neighbours' far edges, so the edge two neighbours face is the same cells of both (SHP-8).
    /// </summary>
    public (int Column, int Row) ShipCell(CapsuleAt at, int column, int row) =>
        (at.Column * (CellsAcross - 1) + column, at.Row * (CellsAcross - 1) + row);

    /// <summary>Stands a fixture that only holds things — a chest, a locker — on a capsule's floor.</summary>
    public Fixture Install(CapsuleAt at, FloorArea area, Inventory chest, DeviceEntry entry) =>
        Stand(at, new Fixture(area, chest, entry, null));

    /// <summary>Stands a device on a capsule's floor, its top-left cell at a column and row, and schedules its first cycle.</summary>
    public Fixture Install(CapsuleAt at, int column, int row, Device device)
    {
        var area = new FloorArea(column, row, device.Entry.Columns, device.Entry.Rows);
        var fixture = Stand(at, new Fixture(area, device.Inventory, device.Entry, device));
        devices.Add(device.Inventory, device);
        Schedule(device);
        return fixture;
    }

    /// <summary>
    /// A player seated at <paramref name="seat"/> sets a device to run the <paramref name="way"/>th of its ways from
    /// now (DEV-5), refused unless the seat reaches it (SHP-1). A cycle already scheduled under its old way is dropped
    /// (SHP-3).
    /// </summary>
    /// <returns>Whether the device now runs that way.</returns>
    public bool Select(CapsuleAt seat, int id, int way)
    {
        if (CapsuleOn(seat) is not { } capsule || InventoryOf(id) is not { } inventory) return false;
        if (!capsule.Reaches(inventory) || !devices.TryGetValue(inventory, out var device)) return false;
        if (!device.Select(way, NowS)) return false;
        Schedule(device);
        return true;
    }

    /// <summary>
    /// A player seated at <paramref name="seat"/> drags one slot onto another (ITM-3), refused unless the seat reaches
    /// both inventories (SHP-1).
    /// </summary>
    /// <returns>Whether anything moved.</returns>
    public bool Move(CapsuleAt seat, int fromId, int fromSlot, int toId, int toSlot)
    {
        if (CapsuleOn(seat) is not { } capsule) return false;
        if (InventoryOf(fromId) is not { } from || InventoryOf(toId) is not { } to) return false;
        if (fromSlot < 0 || fromSlot >= from.Slots || toSlot < 0 || toSlot >= to.Slots) return false;
        if (!capsule.Reaches(from) || !capsule.Reaches(to)) return false;
        return Inventory.Move(from, fromSlot, to, toSlot);
    }

    /// <summary>
    /// An admin's edit (SHP-6): sets one slot to <paramref name="count"/> of <paramref name="item"/> from no seat,
    /// refused unless the slot may hold that item and the count is at most a stack. A count of 0 empties the slot.
    /// </summary>
    /// <returns>Whether the slot was set.</returns>
    public bool Set(int id, int slot, Item item, int count)
    {
        if (InventoryOf(id) is not { } inventory || slot < 0 || slot >= inventory.Slots) return false;
        if (count < 0 || count > inventory.StackMost) return false;
        if (count > 0 && !MayHold(inventory, slot, item)) return false;
        inventory.Set(slot, new Stack(item, count));
        return true;
    }

    /// <summary>A device's slot holds the one item its layout gives it; any other slot what its filter accepts.</summary>
    bool MayHold(Inventory inventory, int slot, Item item) =>
        devices.TryGetValue(inventory, out var device)
            ? device.SlotItem(slot) == item
            : inventory.FilterOf(slot).Accepts(item);

    /// <summary>Runs every cycle due by <paramref name="nowS"/>, in order; a time already passed changes nothing.</summary>
    public void AdvanceTo(double nowS)
    {
        while (due.TryPeek(out var next, out var when) && when.DueS <= nowS)
        {
            due.Dequeue();
            if (next.Generation != next.Device.Generation) continue;
            NowS = when.DueS;
            next.Device.Cycle();
            Schedule(next.Device);
        }

        NowS = Math.Max(NowS, nowS);
    }

    Fixture Stand(CapsuleAt at, Fixture fixture)
    {
        var capsule = CapsuleOn(at) ?? throw new InvalidOperationException($"no capsule at {at}");
        capsule.Stand(fixture);
        Board(fixture.Inventory);
        return fixture;
    }

    Inventory Board(Inventory inventory)
    {
        ids.Add(inventory, inventories.Count);
        inventories.Add(inventory);
        return inventory;
    }

    void Schedule(Device device) => due.Enqueue((device, device.Generation), (device.DueS, scheduled++));
}
