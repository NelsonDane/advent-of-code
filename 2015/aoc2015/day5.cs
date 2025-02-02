// Nelson Dane
// Advent of Code 2015 Day 5

using System.Text.RegularExpressions;

namespace aoc2015;

public class Day5 {
    private static readonly string[] EvilStrings = ["ab", "cd", "pq", "xy"];
    private static readonly char[] Vowels = ['a', 'e', 'i', 'o', 'u'];
    private static bool ContainsAny(string input, string[] searching) {
        return searching.Any(input.Contains);
    }


    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 5, example: false);
        var numNice = 0;
        foreach (var s in input) {
            // Evil strings
            if (ContainsAny(s, EvilStrings)) {
                continue;
            }
            // At least 3 vowels
            if (s.Count(c => Vowels.Contains(c)) < 3) {
                continue;
            }
            // At least 1 repeated letters
            var repeatedRegex = new Regex(@"(.)\1{1}");
            if (!repeatedRegex.IsMatch(s)) {
                continue;
            }
            // It all passes
            numNice++;
        }
        Console.WriteLine($"Number of Nice: {numNice}");
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 5, example: false);
        var numNice = 0;
        foreach (var s in input) {
            // Repeat with 1 letter in-between
            var repeatSpaced = new Regex(@"(\w).\1");
            if (!repeatSpaced.IsMatch(s)) {
                continue;
            }
            // Repeated without overlapping
            var repeatOverlap = new Regex(@"(\w\w).*\1");
            if (!repeatOverlap.IsMatch(s)) {
                continue;
            }
            numNice++;
        }
        Console.WriteLine($"Number of Nice: {numNice}");
    }

    public void Run() {
        Part1();
        Part2();
    }
}
