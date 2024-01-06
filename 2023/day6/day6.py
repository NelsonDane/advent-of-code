# Nelson Dane
# Advent of Code 2023 Day 6

import sys
import math

# Get input args
filename = 'input.txt'
if len(sys.argv) == 2 and "e" in sys.argv[1]:
    filename = 'example.txt'
if len(sys.argv) == 2 and "p" in sys.argv[1]:
    SHOULD_PRINT = True
else:
    SHOULD_PRINT = False
if len(sys.argv) == 2 and "l" in sys.argv[1]:
    DEBUG_LOG = True
else:
    DEBUG_LOG = False

# Read in the input file
with open(filename, 'r') as f:
    data = f.read().splitlines()

def print_and_log(message, always_print=False):
    if SHOULD_PRINT or always_print:
        print(message)
    if DEBUG_LOG:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f"{message}\n")


def get_little_t(big_t, big_d):
    # Quadratic formula for time bounds
    plus = (big_t + math.sqrt(big_t**2 - 4*big_d)) / 2
    plus = math.ceil(plus - 1)
    minus = (big_t - math.sqrt(big_t**2 - 4*big_d)) / 2
    minus = math.floor(minus + 1)
    return plus, minus

times = []
distances = []
time_str = data[0].split(':')[-1].split(' ')
distance_str = data[1].split(':')[-1].split(' ')
# Loop through times/distances and add to lists
for i in range(len(time_str)):
    if time_str[i] != '':
        times.append(int(time_str[i]))
for i in range(len(distance_str)):
    if distance_str[i] != '':
        distances.append(int(distance_str[i]))

# Part 1
margin = 1
for i in range(len(times)):
    plus, minus = get_little_t(times[i], distances[i])
    print_and_log(f"t = {times[i]}, d = {distances[i]}")
    print_and_log(f"plus = {plus}, minus = {minus}")
    difference = plus - (minus - 1)
    print_and_log(f"difference = {difference}")
    margin *= difference

print(f"Part 1: {margin}")

# Part 2
times = int("".join([str(x) for x in times]))
distances = int("".join([str(x) for x in distances]))
print_and_log(times)
print_and_log(distances)

plus, minus = get_little_t(times, distances)
print_and_log(f"t = {times}, d = {distances}")
print_and_log(f"plus = {plus}, minus = {minus}")
difference = plus - (minus - 1)
print_and_log(f"difference = {difference}")

print(f"Part 2: {difference}")