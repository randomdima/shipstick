using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Items;

namespace Shipstick.Ship;

/// <summary>A rectangle of a capsule's floor: its top-left cell, and the columns and rows it covers.</summary>
public readonly record struct FloorArea(int Column, int Row, int Columns, int Rows)
{
    public bool Covers(int column, int row) =>
        column >= Column && column < Column + Columns && row >= Row && row < Row + Rows;

    public bool Overlaps(FloorArea other) =>
        Column < other.Column + other.Columns && other.Column < Column + Columns &&
        Row < other.Row + other.Rows && other.Row < Row + Rows;

    /// <summary>Whether it covers at least one cell and lies wholly on a square floor <paramref name="cellsAcross"/> on a side.</summary>
    public bool Within(int cellsAcross) =>
        Columns > 0 && Rows > 0 && Column >= 0 && Row >= 0 && Column + Columns <= cellsAcross && Row + Rows <= cellsAcross;
}

/// <summary>
/// A thing standing on a capsule's floor, covering a rectangle of cells (SHP-5): a device running a way, or a fixture
/// that only holds things, as a chest or a locker does.
/// </summary>
public sealed class Fixture(FloorArea area, Inventory inventory, DeviceEntry entry, Device? device)
{
    public FloorArea Area { get; } = area;

    /// <summary>A holding fixture's slots, or the device's (<see cref="Device.Inventory"/>).</summary>
    public Inventory Inventory { get; } = inventory;

    /// <summary>What the catalogue calls it.</summary>
    public DeviceEntry Entry { get; } = entry;

    /// <summary>The device, or null for a fixture that only holds things.</summary>
    public Device? Device { get; } = device;
}
