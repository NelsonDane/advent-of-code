# Nelson Dane
# Advent of Code 2022 Day 1

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

# Set up largest and current sums
largest = 0
currentSum = 0

# Sum data until blank line
for i in range(len(data)):
    if data[i] == '':
        # If greater than largest, set largest to current sum
        if currentSum > largest:
            largest = currentSum
        currentSum = 0
    else:
        # Add to current sum
        currentSum += int(data[i])

# Print largest sum
print(largest)

# Part 2

# Set up largest and current sums
largest3 = [0, 0, 0]
currentSum3 = 0

# Sum top 3 data until blank line
for i in range(len(data)):
    if data[i] != '':
        # Add to current sum
        currentSum3 += int(data[i])
    else:
        # If greater than largest, set largest to current sum
        if currentSum3 > largest3[0]:
            largest3[0] = currentSum3
            largest3.sort()
            #print(largest3)
        currentSum3 = 0

# Print largest sum
print(largest3[0] + largest3[1] + largest3[2])