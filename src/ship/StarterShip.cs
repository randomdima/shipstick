using Shipstick.Core.Config;
using Shipstick.Devices;
using Shipstick.Economy;
using Shipstick.Items;

namespace Shipstick.Ship;

/// <summary>The ship a new game starts on, laid from <see cref="GameConfig"/> and the catalogue.</summary>
/// <remarks>
/// <para>
/// Every place on the grid is held, every shared wall has a door, and every capsule is walled round on its floor's edge
/// cells (SHP-7), so what is furnished stands inside. Every capsule stands the universal fixtures, life
/// support first, then up to <see cref="StarterFigures.RoleDevicesMost"/> devices of one role, taken a subsection at a
/// time so a role spread over several makes a little of each. Each goes in the first free cells, reading the floor row
/// by row; one that no longer fits is left out.
/// </para>
/// <para>
/// Roles are dealt in reading order, a step across the ship one along the catalogue's roles and a step down a row's
/// worth, so no two neighbours share a role while there are more roles than columns (SHP-4), and a ship no larger
/// than the roles has each once. A device starts running its first way, loaded with
/// <see cref="StarterFigures.DeviceStockEach"/> of each tool and input it needs.
/// </para>
/// </remarks>
public static class StarterShip
{
    public static Vessel Lay(GameConfig config) => Lay(config, Catalogue.Embedded);

    public static Vessel Lay(GameConfig config, Catalogue catalogue)
    {
        var vessel = new Vessel(new ShipGrid(config.Ship.Columns, config.Ship.Rows), config.Capsule.CellsAcross);
        for (var row = 0; row < vessel.Grid.Rows; row++)
            for (var column = 0; column < vessel.Grid.Columns; column++)
                vessel.Place(new CapsuleAt(column, row));
        vessel.HangDoors(config.DoorSlots, config.Items.StackMost);
        vessel.Enclose(catalogue.Device(Catalogue.Wall)!, catalogue.Device(Catalogue.Door)!, config.Items.StackMost);

        var roles = catalogue.Roles.Where(role => RoleDevices(catalogue, role.Id).Any()).ToArray();
        var universal = catalogue.Devices.Where(d => d.Role == Catalogue.Universal && !Catalogue.IsStructure(d.Id))
            .OrderBy(d => d.Id != Catalogue.LifeSupport);
        for (var row = 0; row < vessel.Grid.Rows; row++)
            for (var column = 0; column < vessel.Grid.Columns; column++)
            {
                var role = roles[(column + row * vessel.Grid.Columns) % roles.Length];
                var own = RoleDevices(catalogue, role.Id).Take(config.Starter.RoleDevicesMost);
                foreach (var entry in universal.Concat(own))
                    Furnish(vessel, new CapsuleAt(column, row), entry, config, catalogue);
            }

        return vessel;
    }

    /// <summary>A role's devices that run a way, a subsection's first of each, then each one's second, and so on.</summary>
    static IEnumerable<DeviceEntry> RoleDevices(Catalogue catalogue, string role)
    {
        var bySub = catalogue.Devices.Where(d => d.Role == role && catalogue.WaysBy(d.Id).Count > 0)
            .GroupBy(d => d.Id[..d.Id.IndexOf('.')]).Select(g => g.ToArray()).ToArray();
        for (var round = 0; bySub.Any(g => round < g.Length); round++)
            foreach (var group in bySub)
                if (round < group.Length) yield return group[round];
    }

    static void Furnish(Vessel vessel, CapsuleAt at, DeviceEntry entry, GameConfig config, Catalogue catalogue)
    {
        var capsule = vessel.CapsuleOn(at)!;
        if (FirstFree(capsule, entry.Columns, entry.Rows) is not { } area) return;
        var ways = catalogue.WaysBy(entry.Id);
        if (ways.Count == 0)
        {
            vessel.Install(at, area, Inventory.Open(config.Capsule.ChestSlots, config.Items.StackMost), entry);
            return;
        }

        var device = new Device(entry, ways, config, vessel.NowS);
        foreach (var group in device.Layout)
            if (group.Use is SlotUse.Tool or SlotUse.Input)
                device.Inventory.TryAddTo(group.Slots, group.Item, Math.Min(config.Starter.DeviceStockEach * group.Count, config.Items.StackMost));
        vessel.Install(at, area.Column, area.Row, device);
    }

    static FloorArea? FirstFree(Capsule capsule, int columns, int rows)
    {
        for (var row = 0; row < capsule.CellsAcross; row++)
            for (var column = 0; column < capsule.CellsAcross; column++)
                if (capsule.Fits(new FloorArea(column, row, columns, rows))) return new FloorArea(column, row, columns, rows);
        return null;
    }
}
