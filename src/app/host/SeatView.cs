using Shipstick.Economy;
using Shipstick.Ship;

namespace Shipstick.App.Host;

/// <summary>
/// What a player is sent (WEB-7, WEB-1): their own cabin, and of every other capsule on the ship its walls and doors
/// alone, for the page to draw shaded round it on the capsule's deck — fog of war.
/// </summary>
/// <remarks>A fogged capsule's deck needs nothing more: the page lays every deck from its door cells.</remarks>
sealed record SeatView(int Columns, int Rows, CabinView Cabin, FoggedView[] Fogged)
{
    public static SeatView Of(Vessel vessel, CapsuleAt seat, WayIndex ways) =>
        new(vessel.Grid.Columns, vessel.Grid.Rows, CabinView.Seated(vessel, seat, ways),
            [.. vessel.Capsules.Where(c => c.At != seat).Select(FoggedView.Of)]);
}

/// <summary>A capsule under fog: where it is, and the cells its walls and doors stand on — nothing it holds.</summary>
sealed record FoggedView(CapsuleAt At, WallView[] Walls)
{
    public static FoggedView Of(Capsule capsule) => new(capsule.At,
        [.. capsule.Fixtures.Where(f => f.Entry is { } e && Catalogue.IsStructure(e.Id)).Select(f => new WallView(f.Area, f.Entry!.Id))]);
}

/// <summary>A wall or door cell; <see cref="Kind"/> is its catalogue device id.</summary>
sealed record WallView(FloorArea Area, string Kind);
