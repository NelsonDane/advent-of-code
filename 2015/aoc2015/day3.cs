// Nelson Dane
// Advent of Code 2015 Day 3

namespace aoc2015;

public class Day3 {
    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 3, example: false);
        // Keep track of coordinates like 0x0y
        HashSet<string> visitedHouses = new HashSet<string>();
        visitedHouses.Add("0x0y");
        var previousHouse = "0x0y";
        foreach (var c in input[0]) {
            var newX = int.Parse(previousHouse.Split('x')[0]);
            var newY = int.Parse(previousHouse.Split('x')[1].TrimEnd('y'));
            switch (c) {
                case '^':
                    // Increment x by 1
                    newY++;
                    break;
                case 'v':
                    newY--;
                    break;
                case '>':
                    newX++;
                    break;
                case '<':
                    newX--;
                    break;
            }
            visitedHouses.Add($"{newX}x{newY}y");
            previousHouse = $"{newX}x{newY}y";
        }
        Console.WriteLine($"Total Houses Visited: {visitedHouses.Count}");
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 3, example: false);
        // Keep track of coordinates like 0x0y
        HashSet<string> visitedHouses = new HashSet<string>();
        bool santaTurn = true; // Santa starts
        visitedHouses.Add("0x0y");
        var santaPreviousHouse = "0x0y";
        var roboPreviousHouse = "0x0y";
        foreach (var c in input[0]) {
            var previousHouse = santaTurn ? santaPreviousHouse : roboPreviousHouse;
            var newX = int.Parse(previousHouse.Split('x')[0]);
            var newY = int.Parse(previousHouse.Split('x')[1].TrimEnd('y'));
            switch (c) {
                case '^':
                    // Increment x by 1
                    newY++;
                    break;
                case 'v':
                    newY--;
                    break;
                case '>':
                    newX++;
                    break;
                case '<':
                    newX--;
                    break;
            }

            visitedHouses.Add($"{newX}x{newY}y");
            if (santaTurn) {
                santaPreviousHouse = $"{newX}x{newY}y";
            }
            else {
                roboPreviousHouse = $"{newX}x{newY}y";
            }

            santaTurn = !santaTurn;
        }
        Console.WriteLine($"Total Houses By Santa and Robo: {visitedHouses.Count}");
    }

    public void Run() {
        Part1();
        Part2();
    }
}
