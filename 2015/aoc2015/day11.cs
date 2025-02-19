// Nelson Dane
// Advent of Code 2015 Day 11

namespace aoc2015;

public class Day11 {
    private static List<char> alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

    private static bool IsValidPass(List<int> input) {
        // Check for double letters
        var doublesFound = new List<int>();
        var shouldSkip = false;
        for (var i = 1; i < input.Count; i++) {
            if (shouldSkip) {
                shouldSkip = false;
                continue;
            }
            var current = input[i];
            var prev = input[i - 1];
            if (prev != current) continue;
            // Double found
            shouldSkip = true;
            if (!doublesFound.Contains(current)) doublesFound.Add(current);
            if (doublesFound.Count >= 2) break;
        }
        if (doublesFound.Count < 2) return false;
        // Check for straight
        for (var i = 2; i < input.Count; i++) {
            var twoBehind = input[i - 2];
            var behind = input[i - 1];
            var current = input[i];
            if (twoBehind == behind - 1 &&
                behind == current-1) return true;
        }
        return false;
    }

    private static void Solve(bool example = false, bool part2 = false) {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 11, example: example);
        var skipped = false;
        var currentPassword = input[0].Select(c => alphabet.IndexOf(c)).ToList();
        while (true) {
            // No i, o, l
            var badLetterIndex = -1;
            if (currentPassword.Contains(8)) badLetterIndex = currentPassword.IndexOf(8);
            if (currentPassword.Contains(11)) badLetterIndex = currentPassword.IndexOf(11);
            if (currentPassword.Contains(14)) badLetterIndex = currentPassword.IndexOf(14);
            if (badLetterIndex != -1) {
                // Splice
                var oldLength = currentPassword.Count;
                currentPassword[badLetterIndex]++;
                for (var i = badLetterIndex + 1; i < oldLength; i++) currentPassword[i] = 0;
                continue;
            }
            // Valid?
            if (IsValidPass(currentPassword)) {
                Console.WriteLine(
                    $"Found Valid Pass: {new string(currentPassword.Select(i => alphabet[i]).ToArray())}");
                if (!part2) break;
                if (skipped) break;
                skipped = true;
            }
            // Increment
            var changedLast = false;
            for (var i = currentPassword.Count-1; i > 0; i--) {
                if (currentPassword[i] < 26) {
                    if(!changedLast) currentPassword[i]++;
                    break;
                }
                if (currentPassword[i] != 26) continue;
                currentPassword[i] = 0; // set to a
                currentPassword[i - 1]++; // Digit flipped
                changedLast = true;
            }
        }
    }

    public void Run(bool example=false) {
        Solve(example);
        Solve(example, true);
    }
}
