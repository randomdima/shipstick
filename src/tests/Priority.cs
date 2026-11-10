namespace Shipstick.Tests;

/// <summary>
/// <b>What breaks if this class goes red and nobody notices.</b> Every test class carries exactly one as
/// <c>[Trait(Priority.Key, …)]</c>, beside its <see cref="Tier"/>.
/// </summary>
/// <remarks>
/// <para>
/// <b>A tier is what a question costs; a priority is what its answer is worth.</b> The two are orthogonal, and neither
/// is read off the other. <c>qq tests --upto=4</c> cuts by this one.
/// </para>
/// <para>
/// <b>A ladder of consequence.</b> Each rung answers <em>what is the ship if this is wrong?</em> A class that could be
/// argued into two rungs takes the lower-numbered one. When the suite's budget is spent, what gives way is chosen from
/// the bottom.
/// </para>
/// </remarks>
public static class Priority
{
    /// <summary>The trait key. One key for all ten, so a run can be cut at a rung.</summary>
    public const string Key = "P";

    /// <summary><b>The game is not one.</b> Its state cannot be trusted: an event lost, applied twice or out of order.</summary>
    public const string P0 = "P0";

    /// <summary><b>A player is wronged.</b> An item lost or duplicated, a door that lets through what it must not.</summary>
    public const string P1 = "P1";

    /// <summary><b>A device does not do its job.</b> It consumes and produces nothing, or the wrong amounts.</summary>
    public const string P2 = "P2";

    /// <summary><b>The ship is laid wrong.</b> Capsules, doors and grids that disagree with what the ship is.</summary>
    public const string P3 = "P3";

    /// <summary><b>Something derived disagrees with what it was derived from.</b></summary>
    public const string P4 = "P4";

    /// <summary><b>What is drawn is in the wrong place.</b> The game is right and the picture of it is not.</summary>
    public const string P5 = "P5";

    /// <summary><b>The player cannot do something</b>: open, drag, act.</summary>
    public const string P6 = "P6";

    /// <summary><b>An instrument lies.</b> A log, a caption or a meter reporting other than what happened.</summary>
    public const string P7 = "P7";

    /// <summary><b>Authored data is malformed.</b> A catalogue or JSON file that does not say what its reader expects.</summary>
    public const string P8 = "P8";

    /// <summary><b>A detail is off</b> — noticed on a second look, depended on by nothing.</summary>
    public const string P9 = "P9";

    /// <summary>Every rung, most severe first — what <c>TierTests</c> checks a class against.</summary>
    public static readonly string[] Ladder = [P0, P1, P2, P3, P4, P5, P6, P7, P8, P9];
}
