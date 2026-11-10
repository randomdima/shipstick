namespace Shipstick.Core.Config;

/// <summary>
/// Every number the game runs on, authored in the nested groups. Behaviour code reads its figures from here and never
/// from a literal at the call site.
/// </summary>
/// <remarks>
/// Authored figures are raw terms (a count, a length, an interval); anything a reader would rather look up is derived
/// on the root from them, never authored and back-solved.
/// </remarks>
public sealed record GameConfig
{
    public static GameConfig Default { get; } = new();

    public ShipFigures Ship { get; init; } = new();

    public CapsuleFigures Capsule { get; init; } = new();

    public ItemFigures Items { get; init; } = new();

    public DeviceFigures Devices { get; init; } = new();

    public StarterFigures Starter { get; init; } = new();

    public HostFigures Host { get; init; } = new();

    public DemoFigures Demo { get; init; } = new();

    /// <summary>The slots in one door: a square <see cref="CapsuleFigures.DoorSlotsAcross"/> on a side.</summary>
    public int DoorSlots => Capsule.DoorSlotsAcross * Capsule.DoorSlotsAcross;
}

/// <summary>The ship's own layout.</summary>
public sealed record ShipFigures
{
    /// <summary>The capsule places across the starter ship.</summary>
    public int Columns { get; init; } = 3;

    /// <summary>The capsule places down the starter ship.</summary>
    public int Rows { get; init; } = 3;
}

/// <summary>One capsule's floor and the doors in its walls.</summary>
public sealed record CapsuleFigures
{
    /// <summary>The cells along one side of a capsule's square floor (GAM-4), its walls' edge cells included (SHP-7), which a neighbour shares (SHP-8).</summary>
    public int CellsAcross { get; init; } = 12;

    /// <summary>The slots along one side of a door's square of slots (GAM-3).</summary>
    public int DoorSlotsAcross { get; init; } = 3;

    /// <summary>The slots in a fixture that runs no way and only holds things: a chest, a locker.</summary>
    public int ChestSlots { get; init; } = 8;
}

/// <summary>Items and the slots they sit in.</summary>
public sealed record ItemFigures
{
    /// <summary>The most of one item a single slot holds.</summary>
    public int StackMost { get; init; } = 10;
}

/// <summary>
/// How a device lays out its slots for the way it runs, and how long a way takes aboard. What a way needs, takes and
/// makes, and its minutes, are the catalogue's; only the slots and the clock's scale are here (DEV-4).
/// </summary>
public sealed record DeviceFigures
{
    /// <summary>The fewest slots each input of a way has, each taking only that input.</summary>
    public int SlotsPerInput { get; init; } = 2;

    /// <summary>The fewest slots each output of a way fills.</summary>
    public int OutputSlots { get; init; } = 2;

    /// <summary>Ship seconds one of a way's catalogue minutes takes aboard.</summary>
    public double CycleSPerWayMinute { get; init; } = 1;
}

/// <summary>What the starter ship lays on each capsule's floor, and what it stocks it with.</summary>
public sealed record StarterFigures
{
    /// <summary>The most devices of its role a capsule is laid with, beside the universal fixtures every capsule has.</summary>
    public int RoleDevicesMost { get; init; } = 4;

    /// <summary>How many of each tool and input of its way each device starts loaded with, up to a stack.</summary>
    public int DeviceStockEach { get; init; } = 3;
}

/// <summary>How the host runs the ship's clock and tells its clients (HST-3).</summary>
public sealed record HostFigures
{
    /// <summary>Real seconds between two advances of the ship, after each of which a client is sent its view if it changed.</summary>
    public double TickS { get; init; } = 0.25;

    /// <summary>The most ship seconds a real second the admin may run ship time at.</summary>
    public double RateMost { get; init; } = 100;

    /// <summary>The longest action a client may send, in bytes; a longer one closes its socket.</summary>
    public int ActionBytesMost { get; init; } = 1024;
}

/// <summary>How the demo (DEM-1) records the host for playing back with none.</summary>
public sealed record DemoFigures
{
    /// <summary>Ship seconds of the starter ship recorded from its start, at the host's tick; the demo plays them in a loop.</summary>
    public double RecordedS { get; init; } = 600;
}
