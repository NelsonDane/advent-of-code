// Nelson Dane
// Advent of Code 2015 Day 8

using System.Text.RegularExpressions;

namespace aoc2015;

public class Day8 {
    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 8, example: false);
        var totalStringCode = input.Sum(s => s.Length);
        var totalStringMemory = 0;
        foreach(var line in input) {
            // Removing first/last quotes
            var newLine = line.Substring(1, line.Length - 2);
            // Convert \\ to /
            newLine = newLine.Replace(@"\\", "/");
            // Convert \" to "
            newLine = newLine.Replace("\\\"", "\"");
            // Hex replace \x + 2 chars
            newLine = Regex.Replace(newLine, @"\\x[0-9a-f]{2}", "?");
            totalStringMemory += newLine.Length;
        }
        Console.WriteLine($"Part 1 Difference: {totalStringCode - totalStringMemory}");
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 8, example: false);
        var totalStringCode = input.Sum(s => s.Length);
        var totalStringMemory = 0;
        foreach(var line in input) {
            // Convert \\ to \\\\
            var newLine = line.Replace("\\", @"\\");
            // Convert \" to \\\"
            newLine = newLine.Replace("\"", "\\\"");
            // Add quotes to front and end
            newLine = "\"" + newLine + "\"";
            totalStringMemory += newLine.Length;
        }
        Console.WriteLine($"Part 2 Difference: {totalStringMemory - totalStringCode}");
    }

    public void Run() {
        Part1();
        Part2();
    }
}
