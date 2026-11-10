using Shipstick.Core.Config;
using Shipstick.Ship;

namespace Shipstick.Tests.Ship;

/// <summary>A capsule meets only the capsules on its four sides, through the doors between them (GAM-2).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P3)]
public class ShipGridTests
{
    static readonly GameConfig Config = GameConfig.Default;

    [Fact]
    public void ACapsuleMeetsOnlyTheCapsulesOnItsFourSides()
    {
        var ship = Full(3, 3);
        var middle = new CapsuleAt(1, 1);

        var met = ship.Doors.Where(d => d.First == middle || d.Second == middle).Select(d => d.Across(middle));

        Assert.Equivalent(new CapsuleAt[] { new(1, 0), new(2, 1), new(1, 2), new(0, 1) }, met.ToArray(), strict: true);
    }

    [Fact]
    public void AnEmptyPlaceIsNoNeighbour()
    {
        var ship = new Vessel(new ShipGrid(2, 1), Config.Capsule.CellsAcross);
        ship.Place(new CapsuleAt(0, 0));

        ship.HangDoors(Config.DoorSlots, Config.Items.StackMost);

        Assert.Empty(ship.Doors);
    }

    static Vessel Full(int columns, int rows)
    {
        var ship = new Vessel(new ShipGrid(columns, rows), Config.Capsule.CellsAcross);
        for (var row = 0; row < rows; row++)
            for (var column = 0; column < columns; column++)
                ship.Place(new CapsuleAt(column, row));
        ship.HangDoors(Config.DoorSlots, Config.Items.StackMost);
        return ship;
    }
}
