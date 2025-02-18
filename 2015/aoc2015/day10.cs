using System.Text;

namespace aoc2015;

public class Day10 {
    private static string LookAndSay(string line) {
        var sb = new StringBuilder();
        var count = 1;
        // Start at 1 so we don't go negative
        for (var i = 1; i < line.Length; i++) {
            if (line[i] == line[i - 1]) {
                count++;
            } else {
                sb.Append(count).Append(line[i - 1]);
                count = 1;
            }
        }
        // Append last sequence
        sb.Append(count).Append(line[^1]);
        return sb.ToString();
    }

    private static void Solve(bool example = false, bool part2 = false) {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 10, example: example);

        // Run example input
        if (example) {
            foreach (var line in input) {
                Console.WriteLine($"{line} -> {LookAndSay(line)}");
            }
            return;
        }

        // Run real input
        var loop = part2 ? 50 : 40;
        var answer = input[0];

        for (var i = 0; i < loop; i++) {
            answer = LookAndSay(answer);
        }

        Console.WriteLine($"Final Length: {answer.Length}");
    }

    public void Run(bool example=false) {
        Solve(example);
        Solve(example, true);
    }
}