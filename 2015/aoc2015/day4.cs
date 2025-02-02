// Nelson Dane
// Advent of Code 2015 Day 4

namespace aoc2015;

using System.Security.Cryptography;

public class Day4 {
    private static string GenerateMd5Hash(string input)
    {
        var inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
        var hashBytes = MD5.HashData(inputBytes);
        return Convert.ToHexString(hashBytes);
    }

    private static void Part1() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 4, example: false);
        var count = 0;
        while (true) {
            var firstFiveHash = GenerateMd5Hash(input[0] + count).Substring(0, 5);
            if (firstFiveHash == "00000") {
                break;
            }
            count++;
        }
        Console.WriteLine($"AdventCoins 5 Zeroes Answer: {count}");
    }

    private static void Part2() {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 4, example: false);
        var count = 0;
        // I really thought this would be a lot scarier
        while (true) {
            var firstFiveHash = GenerateMd5Hash(input[0] + count).Substring(0, 6);
            if (firstFiveHash == "000000") {
                break;
            }
            count++;
        }
        Console.WriteLine($"AdventCoins 6 Zeroes Answer: {count}");

    }

    public void Run() {
        Part1();
        Part2();
    }
}
