namespace Shipstick.Tests;

/// <summary>
/// The suite's own gate: every test class names a tier and a priority, and names ones that exist.
/// </summary>
/// <remarks>
/// An untiered class is the failure that reads as a pass: it is in no tier's filter, so no run takes it again. A class
/// with no priority is dropped from every <c>qq tests --upto</c> run the same way.
/// </remarks>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P0)]
public class TierTests
{
    [Fact]
    public void EveryTestClassNamesItsTier() => EveryTestClassNames(Tier.Key, Tier.All);

    [Fact]
    public void EveryTestClassNamesItsPriority() => EveryTestClassNames(Priority.Key, Priority.Ladder);

    static void EveryTestClassNames(string key, string[] known)
    {
        var unnamed = new List<string>();
        var wrong = new List<string>();
        foreach (var type in typeof(Tier).Assembly.GetTypes())
        {
            if (!HoldsTests(type)) continue;

            switch (TraitOf(type, key))
            {
                case null: unnamed.Add(type.FullName!); break;
                case { } named when Array.IndexOf(known, named) < 0: wrong.Add($"{type.FullName} says '{named}'"); break;
            }
        }

        Assert.True(unnamed.Count == 0, $"no [Trait({key}, …)] on: {string.Join(", ", unnamed)}");
        Assert.True(wrong.Count == 0, $"unknown {key}: {string.Join(", ", wrong)}");
    }

    /// <summary>Theories included: <c>TheoryAttribute</c> is a <c>FactAttribute</c>.</summary>
    static bool HoldsTests(Type type)
    {
        if (!type.IsClass || type.IsAbstract) return false;
        foreach (var method in type.GetMethods())
            if (method.IsDefined(typeof(FactAttribute), inherit: true)) return true;
        return false;
    }

    static string? TraitOf(Type type, string key)
    {
        foreach (var attribute in type.GetCustomAttributesData())
        {
            if (attribute.AttributeType != typeof(TraitAttribute)) continue;
            if (attribute.ConstructorArguments.Count == 2 && (string?)attribute.ConstructorArguments[0].Value == key)
                return (string?)attribute.ConstructorArguments[1].Value;
        }

        return null;
    }
}
