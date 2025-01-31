// Nelson Dane
// Advent of Code 2015 Day 2

namespace aoc2015;

public class Day2 {
    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 2, example: false);
        var inputLines = input.Split('\n');
        var totalPaper = 0;
        foreach (var line in inputLines) {
            var l = Int32.Parse(line.Split('x')[0]);
            var w = Int32.Parse(line.Split('x')[1]);
            var h = Int32.Parse(line.Split('x')[2]);
            var surfaces = new int[] { l * w, w * h, h * l };
            var answer = (2 * surfaces.Sum()) + surfaces.Min();
            totalPaper += answer;
        }
        Console.WriteLine("Total Square Feet: " + totalPaper);
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 2, example: false);
        var inputLines = input.Split('\n');
        var totalRibbon = 0;
        foreach (var line in inputLines) {
            var box = Array.ConvertAll(line.Split('x'), int.Parse);
            Array.Sort(box);
            var ribbon = (2 * (box[0] + box[1])) + (box[0] * box[1] * box[2]);
            totalRibbon += ribbon;
        }
        Console.WriteLine("Total Ribbon Feet: " + totalRibbon);
    }

    public void Run() {
        Part1();
        Part2();
    }
}
