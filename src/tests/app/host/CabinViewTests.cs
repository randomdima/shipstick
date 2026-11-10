using System.Text.Json;
using Shipstick.App.Host;
using Shipstick.Core.Config;
using Shipstick.Economy;
using Shipstick.Ship;

namespace Shipstick.Tests.App.Host;

/// <summary>
/// What the host sends of the ship (WEB-7, WEB-1, WEB-2): a player their own cabin and of every other capsule its walls
/// alone, never the capsule beyond a door; the admin every cabin, and the capsule beyond each door.
/// </summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P1)]
public class CabinViewTests
{
    static readonly Vessel Ship = StarterShip.Lay(GameConfig.Default, Catalogue.Embedded);
    static readonly WayIndex Ways = new(Catalogue.Embedded);
    static readonly CapsuleAt Middle = new(1, 1);

    [Fact]
    public void APlayersDoorsNameNoCapsuleBeyond()
    {
        var doors = Sent(CabinView.Seated(Ship, Middle, Ways)).GetProperty("doors");

        Assert.All(doors.EnumerateArray(), door => Assert.False(door.TryGetProperty("beyond", out _)));
    }

    [Fact]
    public void APlayerIsSentEveryOtherCapsuleFogged()
    {
        var fogged = SeatView.Of(Ship, Middle, Ways).Fogged.Select(f => f.At);

        Assert.Equal(Ship.Capsules.Select(c => c.At).Where(at => at != Middle), fogged);
    }

    [Fact]
    public void AFoggedCapsuleIsSentItsWallsAndDoorsAlone()
    {
        var fogged = SeatView.Of(Ship, Middle, Ways).Fogged;

        Assert.All(fogged.SelectMany(f => f.Walls), wall => Assert.True(Catalogue.IsStructure(wall.Kind)));
        Assert.All(fogged, f => Assert.Equal(Ship.CapsuleOn(f.At)!.Fixtures.Count(x => Catalogue.IsStructure(x.Entry?.Id ?? "")),
            f.Walls.Length));
    }

    [Fact]
    public void TheAdminIsSentEveryCabin()
    {
        var cabins = ShipView.Of(Ship, Middle, GameConfig.Default.Items.StackMost, Ways).Cabins.Select(c => c.At);

        Assert.Equal(Ship.Capsules.Select(c => c.At), cabins);
    }

    [Fact]
    public void TheAdminsDoorsNameTheCapsuleBeyond()
    {
        var doors = Sent(CabinView.Entered(Ship, Middle, Ways)).GetProperty("doors");

        Assert.All(doors.EnumerateArray(), door => Assert.True(door.TryGetProperty("beyond", out _)));
    }

    static JsonElement Sent(CabinView cabin) =>
        JsonDocument.Parse(JsonSerializer.SerializeToUtf8Bytes(cabin, HostJson.Default.CabinView)).RootElement;
}
