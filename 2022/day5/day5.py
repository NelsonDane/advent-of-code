# Nelson Dane
# Advent of Code 2022 Day 5

import numpy as np

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Too much data parsing =(

# Make a needed array
across = len(data[0])
col = 0
# Find number of columns
for i in range(len(data)):
    if "[" in data[i]:
        col += 1
crates = np.zeros((col, across), dtype=str)

# Fill array with all crates
for i in range(len(data)):
    if "move" not in data[i] and "[" in data[i]:
        for j in range(len(data[i])):
            crates[i][j] = data[i][j]

# Remove [ and ] from array
for i in range(len(crates)):
    for j in range(len(crates[i])):
        current = crates[i][j]
        # If [ or ] then delete
        if current == '[' or current == ']':
            crates[i][j] = ' '

# Remove columns with only spaces
crates = crates[:, ~np.all(crates == ' ', axis=0)]

# Rotate by -90 degrees
crates = np.rot90(crates, -1)
print('Rotated crates')
print(crates)

# Convert to list of strings
crates_list = []
for i in range(len(crates)):
    temp = ''
    for j in range(len(crates[i])):
        if crates[i][j] != ' ':
            temp += crates[i][j]
    crates_list.append(temp)

crates_list2 = crates_list.copy()

# Print final answer (top crates)
def print_ends(crates_list, PART=1):
    answer = ''
    for i in range(len(crates_list)):
        answer += crates_list[i][-1]
    print(f'Final answer Part {PART}: {answer}')

# Prettier print function
def print_crates(crates_list):
    for i in range(len(crates_list)):
        print(crates_list[i])

def get_instructions(line):
    # First int is amount
    amount = line.split(' ')[1]
    # Second int is from
    from_pos = line.split(' ')[3]
    # Third int is to
    to_pos = line.split(' ')[5]
    #print(f'Instructions: Amount: {amount}, From: {from_pos}, To: {to_pos}')
    return amount, from_pos, to_pos
    
def move(amount, from_pos, to_pos, crates_l, PART=1):
    # Convert to int
    amount, from_pos, to_pos = int(amount), int(from_pos), int(to_pos)
    # Arrays start at 0, not 1
    from_pos -= 1
    to_pos -= 1
    # Get end characters to move
    value_to_move = crates_l[from_pos][-amount:]
    # Reverse string if part 2
    if PART == 1:
        value_to_move = value_to_move[::-1]
    # Remove from string
    crates_l[from_pos] = crates_l[from_pos][:-amount]
    # Add to desired string
    crates_l[to_pos] += value_to_move
    return crates_l

# Part 1

# Loop through data
for i in range(len(data)):
    # Only process instructions
    if "move" in data[i]:
        amount, from_pos, to_pos = get_instructions(data[i])
        crates_list = move(amount, from_pos, to_pos, crates_list)

# Print final answer
print('Final crates Part 1:')
print_crates(crates_list)
print_ends(crates_list)

# Part 2

# Loop through data
for i in range(len(data)):
    # Only process instructions
    if "move" in data[i]:
        amount, from_pos, to_pos = get_instructions(data[i])
        crates_list2 = move(amount, from_pos, to_pos, crates_list2, PART=2)

# Print final answer
print('Final crates Part 2:')
print_crates(crates_list2)
print_ends(crates_list2, PART=2)
        