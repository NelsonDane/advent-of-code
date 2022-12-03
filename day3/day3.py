# Nelson Dane
# Advent of Code 2022 Day 3

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

# Return the priority of each letter
def get_priority(input):
    # Convert to ASCII then subtract to find priority
    if not input.isupper():
        return ord(input)-96
    else:
        return ord(input)-64+26

# Split lines in half
def split_input(input):
    return input[:len(input)//2], input[len(input)//2:]

# Declare priority and dupes
prioritySum = 0
dupes = []

# Loop through data
for i in range(len(data)):
    temp_dupes = []
    first_half, second_half = split_input(data[i])
    # Find duplicate letters
    for j in range(len(first_half)):
        if first_half[j] in second_half and first_half[j] not in temp_dupes:
            temp_dupes.append(first_half[j])
    dupes += temp_dupes

# Find priority of each letter
for i in range(len(dupes)):
    prioritySum += get_priority(dupes[i])

print(f'Part 1 Sum of Item Priorities: {prioritySum}')

# Part 2

# Priority and badges
prioritySum2 = 0
badges = []

# Variables for lists of 3
temp3 = []
count = 0
# Loop through data and split into lists of 3
for i in range(len(data)+1):
    if count % 3 == 0 and count != 0:
        temp_dupes = []
        # Find duplicate letters
        for j in range(len(temp3[0])):
            if temp3[0][j] in temp3[1] and temp3[0][j] in temp3[2] and temp3[0][j] not in temp_dupes:
                temp_dupes.append(temp3[0][j])
        badges += temp_dupes
        temp3 = []
    if i != len(data):
        temp3.append(data[i])
    count += 1

# Find priority of each letter
for i in range(len(badges)):
    prioritySum2 += get_priority(badges[i])

print(f'Part 2 Sum of Badge Priorities: {prioritySum2}')

