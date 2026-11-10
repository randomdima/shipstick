using Shipstick.App.Host;

namespace Shipstick.Tests.App.Host;

/// <summary>The art the host says it serves (GAM-9, GAM-10): what a page may ask for, by the path it asks by.</summary>
[Trait(Tier.Key, Tier.Unit)]
[Trait(Priority.Key, Priority.P8)]
public sealed class AssetListTests : IDisposable
{
    readonly DirectoryInfo root = Directory.CreateTempSubdirectory("shipstick-assets-");

    public void Dispose() => root.Delete(recursive: true);

    void Touch(string path)
    {
        var file = Path.Combine(root.FullName, path);
        Directory.CreateDirectory(Path.GetDirectoryName(file)!);
        File.WriteAllBytes(file, []);
    }

    [Fact]
    public void ListsEveryImageUnderAssetsByItsPathFromTheWebRoot()
    {
        Touch("assets/devices/any_bench.png");
        Touch("assets/ship/floor/deck_plate.png");
        Touch("assets/app/web/fonts/Michroma-Regular.ttf");
        Touch("style.css");

        Assert.Equal(["assets/devices/any_bench.png", "assets/ship/floor/deck_plate.png"], AssetList.Of(root.FullName));
    }

    [Fact]
    public void ListsADeviceModelByItsMeshAloneAmongTheImages()
    {
        Touch("assets/devices/any_bench.png");
        Touch("assets/devices/any_bench.mesh.json");
        Touch("assets/devices/any_bench.mesh.bin");

        Assert.Equal(["assets/devices/any_bench.mesh.json", "assets/devices/any_bench.png"], AssetList.Of(root.FullName));
    }
}
