// Nelson Dane
// Advent of Code 2015 Day 7

namespace aoc2015;

public class Day7 {
    private static readonly SortedDictionary<string, ushort> FinalWireValues = new();

    private static int Part1(int changeB = 0) {
        var helpers = new HelperFunctions();
        var input = helpers.ReadRealInput(day: 7, example: false).ToList();
        if (changeB != 0) {
            // Change for Part 2
            var bIndex = input.FindIndex(x => x.Contains("-> b"));
            input.RemoveAt(bIndex);
            input.Add($"{changeB} -> b");
            FinalWireValues.Clear();
        }
        while (true) {
            for (var i = 0; i < input.Count; i++) {
                var instruction = input[i];
                var bothHalves = instruction.Split(" ->");
                var beingDefined = bothHalves[1].Trim();
                var dependsList = bothHalves[0].Split(" ");

                // Static Assignment (wire or int)
                if (dependsList.Length == 1) {
                    if (ushort.TryParse(dependsList[0], out var result) ||
                        FinalWireValues.TryGetValue(dependsList[0], out result)) {
                        FinalWireValues.Add(beingDefined, result);
                        input.Remove(instruction);
                        continue;
                    }
                }

                // Depends on 1 value
                if (dependsList.Contains("NOT")) {
                    // Not only needs 1
                    if (!FinalWireValues.TryGetValue(dependsList[1], out var notResult)) continue;
                    FinalWireValues.Add(beingDefined, (ushort)~notResult);
                    input.Remove(instruction);
                }
                // Shifted by int
                else if (dependsList.Contains("LSHIFT")) {
                    if (!FinalWireValues.TryGetValue(dependsList[0], out var lShiftResult)) continue;
                    FinalWireValues.Add(beingDefined,
                        (ushort)(lShiftResult << int.Parse(dependsList[2])));
                    input.Remove(instruction);
                }
                else if (dependsList.Contains("RSHIFT")) {
                    if (!FinalWireValues.TryGetValue(dependsList[0], out var rShiftResult)) continue;
                    FinalWireValues.Add(beingDefined,
                        (ushort)(rShiftResult >> int.Parse(dependsList[2])));
                    input.Remove(instruction);
                }
                // Combine with wire or constant
                else if (dependsList.Contains("AND") || dependsList.Contains("OR")) {
                    // Continue if not known or int (1 or 0)
                    if (!ushort.TryParse(dependsList[0], out var andResult1) &&
                        !FinalWireValues.TryGetValue(dependsList[0], out andResult1)) continue;
                    if (!ushort.TryParse(dependsList[2], out var andResult2) &&
                        !FinalWireValues.TryGetValue(dependsList[2], out andResult2)) continue;
                    // AND or OR
                    if (dependsList.Contains("AND")) {
                        FinalWireValues.Add(beingDefined, (ushort)(andResult1 & andResult2));
                    } else {
                        FinalWireValues.Add(beingDefined, (ushort)(andResult1 | andResult2));
                    }
                    input.Remove(instruction);
                }
            }

            if (input.Count == 0) break;
        }
        //FinalWireValues.Select(i => $"{i.Key}: {i.Value}").ToList().ForEach(Console.WriteLine);
        Console.WriteLine($"\na: {FinalWireValues["a"]}");
        return FinalWireValues["a"];
    }

    private static void Part2(int aValue) {
        Part1(changeB: aValue);
    }

    public void Run() {
        var aValue = Part1();
        Part2(aValue);
    }
}
