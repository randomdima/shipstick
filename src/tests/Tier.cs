namespace Shipstick.Tests;

/// <summary>
/// What a test class costs to answer, and therefore when it is run. Every test class carries exactly one as
/// <c>[Trait(Tier.Key, …)]</c>, and the suite is selected by tier (<c>qq tests</c>).
/// </summary>
/// <remarks>
/// <b>The cut is by what a class asks its question of, never by which feature it belongs to.</b> The folders mirror
/// <c>src/</c>; the cost lives in this trait. A tier is not a place. A new tier is a constant here, a row in
/// <c>.qq/tests.py</c>'s <c>TIERS</c> and a line in <c>docs/verification.md</c>.
/// </remarks>
public static class Tier
{
    /// <summary>The trait key. One key for every tier, so a tier can be selected and excluded by name.</summary>
    public const string Key = "Tier";

    /// <summary>Engine-free arithmetic over the game's own types: no page, no server, no clock. Run after every edit.</summary>
    public const string Unit = "Unit";

    /// <summary>Every tier, cheapest first — what <c>TierTests</c> checks a class against.</summary>
    public static readonly string[] All = [Unit];
}
