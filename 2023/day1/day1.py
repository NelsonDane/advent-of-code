# Nelson Dane
# Advent of Code 2023 Day 1

# Read in the input file
with open('example.txt', 'r') as f:
    data = f.read().splitlines()

def get_first_last_digit(data):
    solution = []
    for line in data:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        if len(digits) == 0:
            continue
        elif len(digits) == 1:
            solution.append(int(f"{digits[0]}{digits[0]}"))
        else:
            solution.append(int(f"{digits[0]}{digits[-1]}"))
    return solution

# Part 1
print(f"Part 1: {sum(get_first_last_digit(data))}")

# Part 2
written_numbers = {
    # Account for overlap
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}
        
# Replace written numbers with digits
for i, line in enumerate(data):
    old_line = line
    for word in written_numbers:
        if word in line:
            line = line.replace(word, str(written_numbers[word]))
    # print(f"Old Line: {old_line}")
    # print(f"New Line: {line}")
    data[i] = line

print(f"Part 2: {sum(get_first_last_digit(data))}")