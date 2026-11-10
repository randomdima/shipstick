using Shipstick.App.Demo;

// The demo (DEM-1): writes the static site into the folder named, which must be empty or not yet made.
if (args is not [var target])
{
    Console.Error.WriteLine("usage: shipstick-demo <site folder>");
    return 2;
}

var site = Path.GetFullPath(target);
if (Directory.Exists(site) && Directory.EnumerateFileSystemEntries(site).Any())
{
    Console.Error.WriteLine($"{site} is not empty");
    return 2;
}

DemoSite.Write(Path.Combine(AppContext.BaseDirectory, "client"), site);
Console.WriteLine($"demo written to {site}");
return 0;
