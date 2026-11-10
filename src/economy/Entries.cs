namespace Shipstick.Economy;

/// <summary>A count of one item, by its catalogue id: what a way needs, takes or makes, or what a use leaves.</summary>
public readonly record struct Counted(int Count, string Item);

/// <summary>What a use or a way does to one stat: <see cref="Amount"/> once, or every hour when <see cref="PerHour"/>.</summary>
public readonly record struct StatChange(string Stat, double Amount, bool PerHour);

/// <summary>The codex's words for an item or a device (ECO-12): what it is, and a line of flavour.</summary>
public readonly record struct CodexWords(string About, string Flavour);

/// <summary>One of the catalogue's items, as its subsection file's row and codex row write it.</summary>
/// <param name="DecayH">The hours it lasts — on the shelf, in use, or fitted, by its kind — or null if it keeps.</param>
/// <param name="DecaysTo">What it becomes when it has decayed, or null if it is gone.</param>
public sealed record ItemEntry(
    string Id,
    string Name,
    string Sub,
    StatChange[] Effects,
    Counted[] Leaves,
    string[] Fits,
    string[] Installs,
    double? DecayH,
    string? DecaysTo,
    CodexWords Words);

/// <summary>One of the catalogue's devices: a role's, or a universal fixture every capsule has.</summary>
public sealed record DeviceEntry(string Id, string Name, string Role, int Columns, int Rows, CodexWords Words);

/// <summary>
/// One way an item is made, ended or a need met: run by <see cref="By"/> — a device's id, or
/// <see cref="Catalogue.ByHand"/> — over <see cref="Minutes"/>, keeping its tools and spending what it takes.
/// </summary>
public sealed record WayEntry(
    string Name,
    string By,
    double Minutes,
    Counted[] Needs,
    Counted[] Takes,
    Counted[] Makes,
    StatChange[] Gives,
    string Sub);

/// <summary>A section: a need, or what the needs stand on.</summary>
public sealed record SectionEntry(string Id, string Name, string Serves);

/// <summary>A subsection: what its hundred items are, under which section, made by which roles.</summary>
public sealed record SubsectionEntry(string Code, string Name, string Section, string[] Roles, string Covers);

/// <summary>A role: the devices a capsule's floor is laid with.</summary>
public sealed record RoleEntry(string Id, string Name);

/// <summary>A stat of a crew member, a cabin or the ship.</summary>
/// <param name="Of">Whose it is: crew, cabin or ship.</param>
/// <param name="HigherIsBetter">Which way an item that helps it moves it.</param>
public sealed record StatEntry(string Id, string Of, bool HigherIsBetter, string Typical, string Means);
