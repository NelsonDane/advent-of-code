# Nelson Dane
# Advent of Code 2022 Day 4

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

def fully_contains(first, second):
    # Split the ranges by the dash
    first_start, first_end = first.split('-')
    second_start, second_end = second.split('-')
    # Check if the first range is fully contained in the second range
    if int(first_start) <= int(second_start) and int(first_end) >= int(second_end):
        return True
    else:
        return False

# Sum of fully contained ranges
contains = 0

# Loop through data
for i in range(len(data)):
    # Split by comma
    first, second = data[i].split(',')
    # Check if fully contained in other range
    if fully_contains(first, second) or fully_contains(second, first):
        contains += 1

# Print the answer
print(contains)

# Part 2

def partially_contains(first, second):
    # Split the ranges by the dash
    first_start, first_end = first.split('-')
    second_start, second_end = second.split('-')
    # Check if the first range is partially contained in the second range
    if int(first_start) <= int(second_start) and int(first_end) >= int(second_start):
        return True
    elif int(first_start) <= int(second_end) and int(first_end) >= int(second_end):
        return True
    else:
        return False

# Sum of partially contained ranges
contains2 = 0

# Loop through data
for i in range(len(data)):
    # Split by comma
    first, second = data[i].split(',')
    # Check if partially contained in other range
    if partially_contains(first, second) or partially_contains(second, first):
        contains2 += 1

# Print the answer
print(contains2)
