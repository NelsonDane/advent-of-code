namespace aoc2015;

public class HelperFunctions {
    public string[] ReadRealInput(int day, bool example = false) {
        try {
            var basePath = Directory.GetCurrentDirectory();
            var fullPath =
                Path.GetFullPath(Path.Combine(basePath,
                    $"../../../../../aoc-inputs/2015/day{day}/{(example ? "example.txt" : "input.txt")}"));
            return (File.ReadAllText(fullPath)).Split('\n');
        }
        catch (Exception e) {
            Console.WriteLine(e);
            return [];
        }
    }

    public static void Main() {
        Console.Write("Day to Run: ");
        if (!int.TryParse(Console.ReadLine(), out var day)) return;
        var days = new Dictionary<int, Action> {
            { 1, () => new Day1().Run() },
            { 2, () => new Day2().Run() },
            { 3, () => new Day3().Run() },
            { 4, () => new Day4().Run() },
            { 5, () => new Day5().Run() },
            { 6, () => new Day6().Run() },
            { 7, () => new Day7().Run() },
            { 8, () => new Day8().Run() },
            { 9, () => new Day9().Run() }
        };
        if (days.TryGetValue(day, out var action)) {
            action(); // Run the corresponding day's logic
        }
    }
}
