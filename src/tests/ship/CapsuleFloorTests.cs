using Shipstick.Items;
using Shipstick.Ship;

namespace Shipstick.Tests.Ship;

/// <summary>Fixtures on a capsule's floor (SHP-5).</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P3)]
public class CapsuleFloorTests
{
    const int CellsAcross = 4;

    [Fact]
    public void AFixtureCoversEveryCellOfItsArea()
    {
        var area = new FloorArea(1, 1, 3, 2);

        var covered = Cells().Count(cell => area.Covers(cell.Column, cell.Row));

        Assert.Equal(area.Columns * area.Rows, covered);
    }

    [Fact]
    public void AnAreaSharingOneCellWithAFixtureDoesNotFit()
    {
        var capsule = WithFixtureAt(new FloorArea(0, 0, 2, 2));

        Assert.False(capsule.Fits(new FloorArea(1, 1, 2, 1)));
    }

    [Fact]
    public void AnAreaTouchingAFixtureEdgeToEdgeFits()
    {
        var capsule = WithFixtureAt(new FloorArea(0, 0, 2, 2));

        Assert.True(capsule.Fits(new FloorArea(2, 0, 2, 2)));
    }

    [Fact]
    public void AnAreaOverhangingTheFloorDoesNotFit()
    {
        var capsule = new Capsule(new CapsuleAt(0, 0), CellsAcross);

        Assert.False(capsule.Fits(new FloorArea(CellsAcross - 1, 0, 2, 1)));
    }

    static Capsule WithFixtureAt(FloorArea area)
    {
        var vessel = new Vessel(new ShipGrid(1, 1), CellsAcross);
        var capsule = vessel.Place(new CapsuleAt(0, 0));
        vessel.Install(capsule.At, area, Inventory.Open(1, 1), TestItems.Chest);
        return capsule;
    }

    static IEnumerable<(int Column, int Row)> Cells() =>
        Enumerable.Range(0, CellsAcross).SelectMany(row => Enumerable.Range(0, CellsAcross).Select(column => (column, row)));
}
