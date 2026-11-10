namespace Shipstick.App.Host;

/// <summary>
/// The art the host serves under <c>assets/</c>, by the path a page asks for it by: every image, and every device
/// model the page draws live (GAM-10) — its <c>.mesh.json</c>, which names the rest of what it needs.
/// </summary>
static class AssetList
{
    const string Folder = "assets";
    static readonly string[] Listed = ["*.png", "*.mesh.json"];

    /// <summary>Every listed file under <paramref name="webRoot"/>'s <c>assets/</c>, relative to the web root, with forward slashes.</summary>
    public static string[] Of(string webRoot)
    {
        var root = Path.Combine(webRoot, Folder);
        if (!Directory.Exists(root)) return [];
        return [.. Listed.SelectMany(pattern => Directory.EnumerateFiles(root, pattern, SearchOption.AllDirectories))
            .Select(file => Path.GetRelativePath(webRoot, file).Replace('\\', '/'))
            .Order(StringComparer.Ordinal)];
    }
}
