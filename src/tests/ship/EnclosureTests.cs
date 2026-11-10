using Shipstick.Economy;
using Shipstick.Ship;

namespace Shipstick.Tests.Ship;

/// <summary>Each capsule walled round on its edge cells, a door where a neighbour is, one wall between two (SHP-7, SHP-8).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P2)]
public class EnclosureTests
{
    const int CellsAcross = 6;
    const int StackMost = 10;
    static readonly CapsuleAt Left = new(0, 0);
    static readonly CapsuleAt Right = new(1, 0);
    static readonly DeviceEntry Wall = new("test.wall", "Wall", "any", 1, 1, default);
    static readonly DeviceEntry DoorEntry = new("test.door", "Door", "any", 1, 1, default);

    [Fact]
    public void EveryEdgeCellIsAWallButTheDoorCell()
    {
        var left = Enclosed().CapsuleOn(Left)!;
        var door = left.DoorCell(Side.East);

        for (var row = 0; row < CellsAcross; row++)
            for (var column = 0; column < CellsAcross; column++)
            {
                var standing = left.FixtureAt(column, row)?.Entry;
                var expected = !left.OnEdge(column, row) ? null : (column, row) == door ? DoorEntry : Wall;
                Assert.Same(expected, standing);
            }
    }

    [Fact]
    public void BothDoorCellsHoldTheOneDoorsSlots()
    {
        var vessel = Enclosed();
        var (lc, lr) = vessel.CapsuleOn(Left)!.DoorCell(Side.East);
        var (rc, rr) = vessel.CapsuleOn(Right)!.DoorCell(Side.West);

        Assert.Same(vessel.Doors[0].Inventory, vessel.CapsuleOn(Left)!.FixtureAt(lc, lr)!.Inventory);
        Assert.Same(vessel.Doors[0].Inventory, vessel.CapsuleOn(Right)!.FixtureAt(rc, rr)!.Inventory);
    }

    [Fact]
    public void TheWallTwoCapsulesFaceIsOneSection()
    {
        var vessel = Enclosed();

        Assert.Same(vessel.CapsuleOn(Left)!.FixtureAt(CellsAcross - 1, 0)!.Inventory,
            vessel.CapsuleOn(Right)!.FixtureAt(0, 0)!.Inventory);
    }

    [Fact]
    public void AWallOnTheShipsOuterEdgeIsItsCapsulesAlone()
    {
        var vessel = Enclosed();

        Assert.NotSame(vessel.CapsuleOn(Left)!.FixtureAt(0, 0)!.Inventory,
            vessel.CapsuleOn(Right)!.FixtureAt(CellsAcross - 1, 0)!.Inventory);
    }

    [Fact]
    public void AWallHoldsNothing()
    {
        var wall = Enclosed().CapsuleOn(Left)!.FixtureAt(0, 0)!;

        Assert.Equal(0, wall.Inventory.Slots);
    }

    static Vessel Enclosed()
    {
        var vessel = new Vessel(new ShipGrid(2, 1), CellsAcross);
        vessel.Place(Left);
        vessel.Place(Right);
        vessel.HangDoors(1, StackMost);
        vessel.Enclose(Wall, DoorEntry, StackMost);
        return vessel;
    }
}
