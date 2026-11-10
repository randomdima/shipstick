using Shipstick.Core.Config;
using Shipstick.Economy;
using Shipstick.Ship;

namespace Shipstick.Tests.Ship;

/// <summary>The ship a game starts on (SHP-4), laid from the catalogue.</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P3)]
public class StarterShipTests
{
    static readonly Vessel Starter = StarterShip.Lay(GameConfig.Default);

    [Fact]
    public void EverySharedWallHasOneDoor()
    {
        var grid = Starter.Grid;
        var shared = (grid.Columns - 1) * grid.Rows + grid.Columns * (grid.Rows - 1);

        Assert.Equal(shared, Starter.Doors.Count);
    }

    [Fact]
    public void EveryCapsuleHasALifeSupportThatRuns()
    {
        var without = Starter.Capsules.Where(c => !c.Fixtures.Any(f => f.Entry.Id == Catalogue.LifeSupport && f.Device is not null));

        Assert.Empty(without);
    }

    [Fact]
    public void EveryCapsuleIsLaidWithItsRolesDevices()
    {
        Assert.All(Starter.Capsules, c => Assert.NotNull(RoleOf(c.At)));
    }

    [Fact]
    public void NoTwoNeighboursShareARole()
    {
        var twins = Starter.Doors.Where(d => RoleOf(d.First) == RoleOf(d.Second));

        Assert.Empty(twins);
    }

    static string? RoleOf(CapsuleAt at) =>
        Starter.CapsuleOn(at)!.Fixtures.Select(f => f.Entry.Role).FirstOrDefault(r => r != Catalogue.Universal);
}
