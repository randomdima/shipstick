using Shipstick.Ship;

namespace Shipstick.Tests.Ship;

[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P3)]
public class ShipGridTests
{
    [Fact]
    public void ACapsuleMeetsOnlyTheCapsulesOnItsFourSides()
    {
        var ship = Full(3, 3);
        Span<CapsuleAt> beside = stackalloc CapsuleAt[ShipGrid.MostNeighbours];

        var count = ship.NeighboursOf(new CapsuleAt(1, 1), beside);

        Assert.Equal([new(1, 0), new(2, 1), new(1, 2), new(0, 1)], beside[..count].ToArray());
    }

    [Fact]
    public void AnEmptyPlaceIsNoNeighbour()
    {
        var ship = new ShipGrid(2, 1);
        ship.Place(new CapsuleAt(0, 0));
        Span<CapsuleAt> beside = stackalloc CapsuleAt[ShipGrid.MostNeighbours];

        Assert.Equal(0, ship.NeighboursOf(new CapsuleAt(0, 0), beside));
    }

    static ShipGrid Full(int columns, int rows)
    {
        var ship = new ShipGrid(columns, rows);
        for (var row = 0; row < rows; row++)
            for (var column = 0; column < columns; column++)
                ship.Place(new CapsuleAt(column, row));
        return ship;
    }
}
