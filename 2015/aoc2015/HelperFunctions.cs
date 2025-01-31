namespace aoc2015;

public class HelperFunctions {
    public string ReadRealInput(int day, bool example = false) {
        try {
            var basePath = Directory.GetCurrentDirectory();
            var fullPath =
                Path.GetFullPath(Path.Combine(basePath,
                    $"../../../../../aoc-inputs/2015/day{day}/{(example ? "example.txt" : "input.txt")}"));
            return File.ReadAllText(fullPath);
        }
        catch (Exception e) {
            Console.WriteLine(e);
            return "";
        }
    }

    public static void Main() {
        Console.Write("Day to Run: ");
        var day = Int32.Parse(Console.ReadLine());
        switch (day) {
            case 1:
                var day1 = new Day1();
                day1.Run();
                break;
            case 2:
                var day2 = new Day2();
                day2.Run();
                break;
            default:
                return;
        }
    }
}
