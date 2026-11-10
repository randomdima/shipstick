namespace Shipstick.Ship;

/// <summary>A capsule's place on the ship's grid, column from the left and row from the top.</summary>
public readonly record struct CapsuleAt(int Column, int Row);

/// <summary>The four walls of a capsule, clockwise from the top; a capsule has a door in each wall that has a neighbour.</summary>
public enum Side : byte
{
    North,
    East,
    South,
    West,
}

/// <summary>
/// The ship as a grid of capsule places, each held by a capsule or empty (GAM-1).
/// </summary>
/// <remarks>
/// A capsule meets only the capsules on its four sides (GAM-2); a diagonal never touches, so a place has at most
/// <see cref="MostNeighbours"/> neighbours whatever the ship's shape.
/// </remarks>
public sealed class ShipGrid
{
    /// <summary>The sides a capsule has a door on.</summary>
    public const int MostNeighbours = 4;

    static readonly (int Column, int Row)[] Steps = [(0, -1), (1, 0), (0, 1), (-1, 0)];

    readonly bool[] held;

    public ShipGrid(int columns, int rows)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(columns);
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(rows);
        Columns = columns;
        Rows = rows;
        held = new bool[columns * rows];
    }

    public int Columns { get; }

    public int Rows { get; }

    public bool Contains(CapsuleAt at) => at.Column >= 0 && at.Column < Columns && at.Row >= 0 && at.Row < Rows;

    public bool Holds(CapsuleAt at) => Contains(at) && held[IndexOf(at)];

    /// <summary>Puts a capsule at a place on the grid; a place already held stays held.</summary>
    public void Place(CapsuleAt at)
    {
        if (!Contains(at)) throw new ArgumentOutOfRangeException(nameof(at), at, "outside the ship's grid");
        held[IndexOf(at)] = true;
    }

    /// <summary>The place across <paramref name="side"/>'s wall, held or not, on the grid or not.</summary>
    public static CapsuleAt Beside(CapsuleAt at, Side side)
    {
        var (column, row) = Steps[(int)side];
        return new CapsuleAt(at.Column + column, at.Row + row);
    }

    public static Side Opposite(Side side) => (Side)(((int)side + MostNeighbours / 2) % MostNeighbours);

    /// <summary>A held or empty place's index in reading order, row by row from the top left.</summary>
    public int IndexOf(CapsuleAt at) => at.Row * Columns + at.Column;
}
