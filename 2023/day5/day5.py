# Nelson Dane
# Advent of Code 2023 Day 5

import sys
import time

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


# Part 1
def seed_transformer(seed, stage_dict):
    # Brute force this mf
    for stage_map in stage_dict['maps']:
        if seed < stage_map['source_start'] or seed > stage_map['source_end']:
            continue
        seed = (seed - stage_map['source_start']) + stage_map['dest_start']
        break
    return seed

# Parsing
seeds = data[0].replace('seeds: ', '').split(' ')
seeds = [int(x) for x in seeds]
print_and_log(f"Found {len(seeds)} seeds: {seeds}", always_print=True)
# create stages
all_stages = []
stages = []
for line in data[2:]:
    stages.append(line)
    if line == '':
        all_stages.append(stages)
        stages = []
all_stages.append(stages)
print_and_log(f"Found {len(all_stages)} stages", always_print=True)
# process stages
stage_dicts = []
for stage_list in all_stages:
    stage_list = [x for x in stage_list if x != '']
    stage_dict = {
        'stage': stage_list[0].split(' ')[0],
        'maps': []
    }
    for map in stage_list[1:]:
        ranges = map.split(' ')
        stage_map = {
            'dest_start': int(ranges[0]),
            'source_start': int(ranges[1]),
            'range': int(ranges[2]),
            'dest_end': int(ranges[0]) + int(ranges[2]) - 1,
            'source_end': int(ranges[1]) + int(ranges[2]) - 1,
        }
        stage_dict['maps'].append(stage_map)
    stage_dicts.append(stage_dict)

# move seeds through stages
p1_start_time = time.time()
location_seeds = []
for seed in seeds:
    for stage_dict in stage_dicts:
        seed = seed_transformer(seed, stage_dict)
    location_seeds.append(seed)

print_and_log(f"Time: {time.time() - p1_start_time} seconds", always_print=True)
print_and_log(f"Part 1: Lowest Location Seed: {min(location_seeds)}", always_print=True)

# Part 2
# create ranges from seeds pairs
seed_ranges = []
for i, seed in enumerate(seeds):
    if i == len(seeds) - 1:
        break
    if i % 2 == 0: 
        seed_ranges.append([seed, seeds[i+1]])

location_seeds = []
p2_start_time = time.time()
for i, seed_range in enumerate(seed_ranges):
    print_and_log(f"Seed Range: {i+1}/{len(seed_ranges)}")
    seed_range = (seed_range[0], seed_range[0] + seed_range[1] - 1, 0)
    print_and_log(f"Seed Range: {seed_range}")
    ranges_list = [seed_range]
    new_ranges_list = []
    location_results = []
    for j, stage_dict in enumerate(stage_dicts):
        print_and_log(f"Stage: {stage_dict['stage']} ({j+1}/{len(stage_dicts)})")
        for stage_map in stage_dict['maps']:
            stage_range = (stage_map['source_start'], stage_map['source_end'])
            print_and_log(f"Stage Range: {stage_range}")
            print_and_log(f"Ranges List: {ranges_list}")
            new_ranges_list = []
            print_and_log(f"Processing {len(ranges_list)} ranges")
            for k, ranges in enumerate(ranges_list):
                if ranges[2] == 1:
                    print_and_log(f"Skipping {ranges} because it's already been processed")
                    new_ranges_list.append(ranges)
                    continue
                # 3 cases: ranges inside stage_range, ranges outside stage_range, ranges overlap stage_range
                outside_stage_range = (ranges[0] < stage_range[0] and ranges[1] < stage_range[0]) or (ranges[0] > stage_range[-1] and ranges[1] > stage_range[-1])
                inside_stage_range = ranges[0] >= stage_range[0] and ranges[1] <= stage_range[-1]
                if outside_stage_range:
                    # ranges outside stage_range
                    print_and_log(f"{ranges} outside {stage_range}")
                    ranges = (ranges[0], ranges[1], 0)
                    new_ranges_list.append(ranges)
                    continue
                elif inside_stage_range:
                    # ranges inside stage_range
                    print_and_log(f"{ranges} inside {stage_range}")
                    shift = stage_map['dest_start'] - stage_map['source_start']
                    new_range = (ranges[0], ranges[1])
                    new_range_shift = (new_range[0] + shift, new_range[-1] + shift, 1)
                    new_ranges_list.append(new_range_shift)
                    print_and_log(f"New Range: {new_range_shift} (Shifted by {shift}))")
                else:
                    # ranges overlap stage_range (only shift the overlapping part)
                    # 3 cases: ranges overlap stage_range on left, ranges overlap stage_range on right, ranges overlap stage_range on both sides
                    overlap_left = (ranges[0] < stage_range[0] and ranges[1] <= stage_range[-1])
                    overlap_right = (ranges[0] >= stage_range[0] and ranges[1] > stage_range[-1])
                    if overlap_left:
                        # ranges overlap stage_range on left
                        print_and_log(f"{ranges} overlaps {stage_range} on left")
                        shift = stage_map['dest_start'] - stage_map['source_start']
                        overlap = (stage_range[0], ranges[1])
                        overlap_shift = (overlap[0] + shift, overlap[-1] + shift, 1)
                        left_side = (ranges[0], stage_range[0] - 1, 0) # Maybe????
                        new_ranges_list.append(overlap_shift)
                        new_ranges_list.append(left_side)
                        print_and_log(f"Left: {left_side}, Overlap: {overlap_shift}, Shift: {shift}")
                    elif overlap_right:
                        # ranges overlap stage_range on right
                        print_and_log(f"{ranges} overlaps {stage_range} on right")
                        shift = stage_map['dest_start'] - stage_map['source_start']
                        overlap = (ranges[0], stage_range[-1])
                        overlap_shift = (overlap[0] + shift, overlap[-1] + shift, 1)
                        right_side = (stage_range[-1] + 1, ranges[1], 0) # Maybe?????
                        new_ranges_list.append(overlap_shift)
                        new_ranges_list.append(right_side)
                        print_and_log(f"Right: {right_side}, Overlap: {overlap_shift}, Shift: {shift}")
                    else:
                        # ranges overlap stage_range on both sides
                        print_and_log(f"{ranges} overlaps {stage_range} on both sides")
                        shift = stage_map['dest_start'] - stage_map['source_start']
                        overlap = (stage_range[0], stage_range[-1])
                        overlap_shift = (overlap[0] + shift, overlap[-1] + shift, 1)
                        left_side = (ranges[0], stage_range[0] - 1, 0) # Maybe????
                        right_side = (stage_range[-1] + 1, ranges[1], 0) # Maybe????
                        new_ranges_list.append(overlap_shift)
                        new_ranges_list.append(left_side)
                        new_ranges_list.append(right_side)
                        print_and_log(f"Left: {left_side}, Overlap: {overlap_shift}, Right: {right_side}, Shift: {shift}")
            ranges_list = new_ranges_list
        # reset modified flag
        ranges_list = [(x[0], x[1], 0) for x in ranges_list]
    location_results += ranges_list
    # Get smallest seed from location results
    location_results.sort(key=lambda tup: tup[0])
    print_and_log(location_results)
    print_and_log(f"Smallest seed: {location_results[0][0]}")
    location_seeds.append(location_results[0][0])

print_and_log(f"Time: {time.time() - p2_start_time} seconds", always_print=True)
print_and_log(f"Part 2: Lowest Location Seed: {min(location_seeds)}", always_print=True)
