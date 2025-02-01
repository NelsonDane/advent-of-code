// Nelson Dane
// Advent of Code 2015 Day 1

namespace aoc2015;

public class Day1 {
    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 1, example: false);
        // ( is Up, ) is Down
        var numUp = input[0].Count(c => c == '(');
        var numDown = input[0].Count(c => c == ')');
        Console.WriteLine("Resulting Floor: " + (numUp - numDown));
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 1, example: false);
        var floor = 0;
        var index = 1;
        foreach(var c in input[0]) {
            if (c == '(') floor++;
            if (c == ')') floor--;
            if (floor == -1) break;
            index++;
        }
        Console.WriteLine("Resulting basement index: " + index);
    }

    public void Run() {
        Part1();
        Part2();
    }
}
