using Shipstick.Items;

namespace Shipstick.Ship;

/// <summary>
/// One capsule: a square floor of cells, the fixtures standing on it, and a door in each wall that has a neighbour
/// (GAM-4). Its walls and doors are fixtures too, on the floor's edge cells (GAM-10, SHP-7).
/// </summary>
public sealed class Capsule
{
    readonly List<Fixture> fixtures = [];
    readonly Door?[] doors = new Door?[ShipGrid.MostNeighbours];

    public Capsule(CapsuleAt at, int cellsAcross)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(cellsAcross);
        At = at;
        CellsAcross = cellsAcross;
    }

    public CapsuleAt At { get; }

    public int CellsAcross { get; }

    public IReadOnlyList<Fixture> Fixtures => fixtures;

    public Door? DoorOn(Side side) => doors[(int)side];

    /// <summary>Whether a player seated here can reach into <paramref name="inventory"/>: a fixture's here, or a door's in these walls (SHP-1).</summary>
    public bool Reaches(Inventory inventory)
    {
        foreach (var fixture in fixtures)
            if (ReferenceEquals(fixture.Inventory, inventory)) return true;
        foreach (var door in doors)
            if (ReferenceEquals(door?.Inventory, inventory)) return true;
        return false;
    }

    /// <summary>Whether a cell lies on the floor's edge, where the walls stand (SHP-7).</summary>
    public bool OnEdge(int column, int row) =>
        column == 0 || row == 0 || column == CellsAcross - 1 || row == CellsAcross - 1;

    /// <summary>The edge cell a door in a side's wall stands on: the middle of that edge (SHP-7).</summary>
    public (int Column, int Row) DoorCell(Side side)
    {
        int middle = CellsAcross / 2, last = CellsAcross - 1;
        return side switch
        {
            Side.North => (middle, 0),
            Side.East => (last, middle),
            Side.South => (middle, last),
            _ => (0, middle),
        };
    }

    /// <summary>The door hung in a wall whose door cell is this one, or null.</summary>
    public Door? DoorAt(int column, int row)
    {
        for (var side = Side.North; side <= Side.West; side++)
            if (DoorOn(side) is { } door && DoorCell(side) == (column, row)) return door;
        return null;
    }

    /// <summary>The fixture covering a floor cell, or null if the cell is free.</summary>
    public Fixture? FixtureAt(int column, int row)
    {
        foreach (var fixture in fixtures)
            if (fixture.Area.Covers(column, row)) return fixture;
        return null;
    }

    /// <summary>Whether <paramref name="area"/> lies wholly on the floor and shares no cell with a fixture (SHP-5).</summary>
    public bool Fits(FloorArea area)
    {
        if (!area.Within(CellsAcross)) return false;
        foreach (var fixture in fixtures)
            if (fixture.Area.Overlaps(area)) return false;
        return true;
    }

    internal void Stand(Fixture fixture)
    {
        if (!Fits(fixture.Area))
            throw new InvalidOperationException($"{fixture.Area} does not fit on the floor of {At}");
        fixtures.Add(fixture);
    }

    internal void Hang(Side side, Door door) => doors[(int)side] = door;
}
