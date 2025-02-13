// Nelson Dane
// Advent of Code 2015 Day 9

namespace aoc2015;

public class Day9 {
    // https://stackoverflow.com/a/12249225
    private static IEnumerable<IEnumerable<T>> GetPermutations<T>(IEnumerable<T> items, int count) {
        // Unique permutations
        var i = 0;
        foreach (var item in items) {
            if (count == 1) {
                yield return new T[] { item };
            }
            else {
                foreach (var result in GetPermutations(items.Except(new[] { item }), count - 1)) {
                    yield return new T[] { item }.Concat(result);
                }
            }
            i++;
        }
    }

    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 9, example: false);
        var distancesList = new List<(string, string, int)>();
        foreach (var line in input) {
            var distance = line.Split(" = ");
            var cities = distance[0].Split(" to ");
            distancesList.Add((cities[0], cities[1], int.Parse(distance[1])));
        }
        // Get all cities from Item1 + Item2 then dedupe
        var citiesList = distancesList.Select(x => x.Item1).ToList();
        citiesList.AddRange(distancesList.Select(x => x.Item2).ToList());
        citiesList = citiesList.Distinct().ToList();
        // Get all combinations
        var allPermutations = GetPermutations(citiesList, citiesList.Count);
        var listPerms = allPermutations.Select(x => x.ToList()).ToList();
        var shortestRoute = int.MaxValue; // lol
        var longestRoute = 0;
        foreach (var route in listPerms) {
            var routeDistance = 0;
            var possiblePerm = true;
            for (var i = 0; i < route.Count - 1; i++) {
                var city1 = route[i];
                var city2 = route[i + 1];
                // Find the distance
                var found = false;
                foreach (var distance in distancesList) {
                    if ((distance.Item1 == city1 && distance.Item2 == city2) || (distance.Item1 == city2 && distance.Item2 == city1)) {
                        routeDistance += distance.Item3;
                        found = true;
                    }
                }
                if (found) continue;
                // Invalid route, impossible perm
                possiblePerm = false;
                break;
            }
            // End loop calculations
            if (!possiblePerm) break;
            if (routeDistance < shortestRoute) shortestRoute = routeDistance;
            if (routeDistance > longestRoute) longestRoute = routeDistance;
        }
        Console.WriteLine($"Part 1 Shortest: {shortestRoute}");
        Console.WriteLine($"Part 2 Longest: {longestRoute}");
    }

    public void Run() {
        Part1();
    }
}
