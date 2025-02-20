// Nelson Dane
// Advent of Code 2015 Day 12

namespace aoc2015;

using System.Text.Json;

public class Day12 {
    // I should've done this for part 1 but it's fine...
    private static int sumNodes(JsonElement node) {
        // We love recursion
        if (node.ValueKind.Equals(JsonValueKind.Object)) {
            // Child object
            if (node.EnumerateObject().Any(m => m.Value.ToString() == "red")) return 0;
            return node.EnumerateObject().Sum(n => sumNodes(n.Value));
        }
        if (node.ValueKind.Equals(JsonValueKind.Array)) {
            // "red" in arrays is ok
            return node.EnumerateArray().Sum(m => sumNodes(m));
        }
        return node.ValueKind.Equals(JsonValueKind.Number) ? node.GetInt32() : 0;
    }

    private static void Solve(bool example = false, bool part2 = false) {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 12, example: example);
        var jsonInput = input[0];
        var sum = 0;
        var currentNum = "";
        for (var i = 0; i < jsonInput.Length; i++) {
            if (int.TryParse(jsonInput[i].ToString(), out var n)) {
                // Check for minus sign
                if (i != 0 && currentNum == "" && jsonInput[i-1] == '-') currentNum = "-" + currentNum;
                currentNum += n.ToString();
            }
            else if (currentNum != "") {
                // Not an int
                sum += int.Parse(currentNum);
                currentNum = "";
            }
        }
        if (!part2) Console.WriteLine($"Part 1 Sum: {sum}");
        // Part 2
        if (part2) {
            // Remove nodes with a member value = "red"
            var jsonObject = JsonDocument.Parse(jsonInput);
            var root = jsonObject.RootElement;
            Console.WriteLine($"Part 2 Sum: {sumNodes(root)}");
        }
    }

    public void Run(bool example=false) {
        Solve(example);
        Solve(example, true);
    }
}
