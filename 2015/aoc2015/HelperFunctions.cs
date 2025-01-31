namespace aoc2015;

public class HelperFunctions {
    public string ReadRealInput(int day, bool example = false) {
        try {
            var basePath = Directory.GetCurrentDirectory();
            var fullPath =
                Path.GetFullPath(Path.Combine(basePath,
                    $"../../../../../aoc-inputs/2015/day{day}/{(example ? "example.txt" : "input.txt")}"));
            Console.WriteLine("Full Path: +" + fullPath);
            return File.ReadAllText(fullPath);
        }
        catch (Exception e) {
            Console.WriteLine(e);
            return "";
        }
    }
}