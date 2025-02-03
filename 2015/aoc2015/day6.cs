// Nelson Dane
// Advent of Code 2015 Day 6

namespace aoc2015;

public class Day6 {
    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 6, example: false);
        // Probably a better way but whatever
        var lightGrid = new int[1000, 1000];
        Array.Clear(lightGrid);
        foreach(var instruction in input) {
            // Decode instruction
            var parts = instruction.Split(' ');
            var instructionStart = parts[0] == "toggle" ? 1 : 2;
            var startX = int.Parse(parts[instructionStart].Split(',')[0]);
            var startY = int.Parse(parts[instructionStart].Split(',')[1]);
            var endX = int.Parse(parts[^1].Split(',')[0]);
            var endY = int.Parse(parts[^1].Split(',')[1]);
            for (var i = startY; i <= endY; i++) {
                for (var j = startX; j <= endX; j++) {
                    if (parts[0] == "toggle") {
                        lightGrid[i, j] = lightGrid[i, j] == 1 ? 0 : 1;
                    } else if (parts[1] == "on") {
                        lightGrid[i, j] = 1;
                    }
                    else {
                        lightGrid[i, j] = 0;
                    }
                }
            }
        }
        // Count all 1's. Could be done above but it's ok
        var totalOn = 0;
        for (var k = 0; k < lightGrid.GetLength(0); k++) {
            for (var l = 0; l < lightGrid.GetLength(1); l++) {
                if (lightGrid[k, l] == 1) {
                    totalOn++;
                }
            }
        }
        Console.WriteLine($"Lights on: {totalOn}");
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 6, example: false);
        var lightGrid = new int[1000, 1000];
        Array.Clear(lightGrid);
        var lightSum = 0;
        foreach(var instruction in input) {
            // Decode instruction
            var parts = instruction.Split(' ');
            var instructionStart = parts[0] == "toggle" ? 1 : 2;
            var startX = int.Parse(parts[instructionStart].Split(',')[0]);
            var startY = int.Parse(parts[instructionStart].Split(',')[1]);
            var endX = int.Parse(parts[^1].Split(',')[0]);
            var endY = int.Parse(parts[^1].Split(',')[1]);
            for (var i = startY; i <= endY; i++) {
                for (var j = startX; j <= endX; j++) {
                    if (parts[0] == "toggle") {
                        lightGrid[i, j] += 2;
                        lightSum += 2;
                    } else if (parts[1] == "on") {
                        lightGrid[i, j]++;
                        lightSum++;
                    }
                    else if (lightGrid[i, j] != 0) {
                        lightGrid[i, j]--;
                        lightSum--;
                    }
                }
            }
        }
        Console.WriteLine($"Total Brightness: {lightSum}");
    }

    public void Run() {
        Part1();
        Part2();
    }
}
