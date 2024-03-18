using System;
using System.IO;
using System.Collections.Generic;

namespace day8 {
    class LCM {
        public static long GetLCM(long[] numbers) {
            long lcm = numbers[0];
            for (int i = 1; i < numbers.Length; i++) {
                lcm = GetLCM(lcm, numbers[i]);
            }
            return lcm;
        }

        public static long GetLCM(long a, long b) {
            return Math.Abs(a * b) / GetGCD(a, b);
        }

        public static long GetGCD(long a, long b) {
            return b == 0 ? a : GetGCD(b, a % b);
        }
    }

    class Solutions {
        static string[] getInput(string[] args) {
            string[] input;
            // If e, then use example input
            if (args.Length > 0 && args[0] == "e") {
                input = File.ReadAllLines("example.txt");
            } else {
                input = File.ReadAllLines("input.txt");
            }
            return input;
        }
        static void Main(string[] args) {
            string[] input = getInput(args);
            char[] instructions = new char[0];
            Dictionary<string, Dictionary<string, string>> nodes = new Dictionary<string, Dictionary<string, string>>();
            foreach (string line in input) {
                if (line == "") {
                    continue;
                }
                if (!line.Contains("=") && (line.Contains("R") || line.Contains("L"))) {
                    instructions = line.ToCharArray();
                    continue;
                }
                Dictionary<string, string> temp = new Dictionary<string, string>();
                string[] split = line.Split("=");
                string node = split[0].Trim();
                string[] split2 = split[1].Split(",");
                string value1 = split2[0].Trim().Replace("(", "");
                string value2 = split2[1].Trim().Replace(")", "");
                temp.Add("L", value1);
                temp.Add("R", value2);
                nodes.Add(node, temp);
            }

            // Part 1
            string START = "AAA";
            string END = "ZZZ";
            string current = START;
            bool FINISHED = false;
            int count = 0;
            // Loop through each instruction
            while (!FINISHED) {
                foreach (char instruction in instructions) {
                    // Get current node
                    Dictionary<string, string> temp = nodes[current];
                    // Get next node
                    if (instruction == 'L') {
                        current = temp["L"];
                    } else {
                        current = temp["R"];
                    }
                    count++;
                    if (current == END) {
                        Console.WriteLine("Part 1: " + count);
                        FINISHED = true;
                        break;
                    }
                }
            }

            // Part 2
            List<string> startingNodes = new List<string>();
            foreach (string node in nodes.Keys) {
                if (node.EndsWith("A")) {
                    startingNodes.Add(node);
                }
            }

            List<long> counts = new List<long>();
            foreach (string startNode in startingNodes) {
                string START2 = startNode;
                char END_CHAR = 'Z';
                string current2 = START2;
                bool FINISHED2 = false;
                int count2 = 0;
                // Loop through each instruction
                while (!FINISHED2) {
                    foreach (char instruction in instructions) {
                        // Get current node
                        Dictionary<string, string> temp = nodes[current2];
                        // Get next node
                        if (instruction == 'L') {
                            current2 = temp["L"];
                        } else {
                            current2 = temp["R"];
                        }
                        count2++;
                        if (current2.EndsWith(END_CHAR)) {
                            // Console.WriteLine("{0} DONE: {1}", current2, count2);
                            counts.Add(count2);
                            FINISHED2 = true;
                            break;
                        }
                    }
                }
            }
            // Find LCM of counts
            long[] countsArray = counts.ToArray();
            long lcm = LCM.GetLCM(countsArray);
            Console.WriteLine("Part 2: " + lcm);
        }
    }
}