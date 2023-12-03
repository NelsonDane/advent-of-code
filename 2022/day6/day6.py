# Nelson Dane
# Advent of Code 2022 Day 6

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

def check_for_duplicates(input):
    # Check for duplicates in list
    for i in range(len(input)):
        if input.count(input[i]) > 1:
            return True
    return False

# Loop through data
for i in range(len(data)):
    count = 0
    past_data = []
    # Move through each character
    for j in range(len(data[i])):
        print(count, past_data)
        if len(past_data) < 4:
            past_data.append(data[i][j])
            count += 1
            continue
        else:
            # Remove first element and add new one
            past_data.pop(0)
            past_data.append(data[i][j])
        # Check for duplicates
        if not check_for_duplicates(past_data):
            print(f'Part 1: Line {i+1} has no duplicates at {count+1}: {past_data}')
            break
        count += 1

# Part 2

# Loop through data
for i in range(len(data)):
    count = 0
    past_data = []
    # Move through each character
    for j in range(len(data[i])):
        print(count, past_data)
        if len(past_data) < 14:
            past_data.append(data[i][j])
            count += 1
            continue
        else:
            # Remove first element and add new one
            past_data.pop(0)
            past_data.append(data[i][j])
        # Check for duplicates
        if not check_for_duplicates(past_data):
            print(f'Part 2: Line {i+1} has no duplicates at {count+1}: {past_data}')
            break
        count += 1


