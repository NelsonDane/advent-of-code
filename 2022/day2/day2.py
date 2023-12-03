# Nelson Dane
# Advent of Code 2022 Day 2

# Read in the input file
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# Part 1

# Convert from single letter to word
def input_to_word(input):
    input = input.upper()
    if input == 'A' or input == 'X':
        return 'rock'
    elif input == 'B' or input == 'Y':
        return 'paper'
    elif input == 'C' or input == 'Z':
        return 'scissors'

# Logic for rock paper scissors game
def rock_paper_scissors(mine, theirs):
    mine = mine.lower()
    theirs = theirs.lower()
    if mine == theirs:
        return 'draw'
    elif mine == 'rock' and theirs == 'paper':
        return 'loss'
    elif mine == 'rock' and theirs == 'scissors':
        return 'win'
    elif mine == 'paper' and theirs == 'rock':
        return 'win'
    elif mine == 'paper' and theirs == 'scissors':
        return 'loss'
    elif mine == 'scissors' and theirs == 'rock':
        return 'loss'
    elif mine == 'scissors' and theirs == 'paper':
        return 'win'
    else:
        print('Error: Invalid input')

def score(shape, outcome):
    shape = shape.lower()
    outcome = outcome.lower()
    score = 0
    if shape == 'rock':
        score += 1
    elif shape == 'paper':
        score += 2
    elif shape == 'scissors':
        score += 3
    if outcome == 'win':
        score += 6
    elif outcome == 'draw':
        score += 3
    return score

# Loop through data
myScore = 0

for i in range(len(data)):
    # Get play and strategy
    play = data[i].split(' ')[0]
    strategy = data[i].split(' ')[1]

    print(f'Play: {play}, Strategy: {strategy}')

    # Convert play to word
    play = input_to_word(play)
    strategy = input_to_word(strategy)

    # Get outcome
    outcome = rock_paper_scissors(strategy, play)

    # Get score
    temp_score = score(strategy, outcome)

    print(f'Outcome: {outcome}, Score: {temp_score}')

    # Add to total score
    myScore += temp_score

print(f'Total Score Part 1: {myScore}')

# Part 2

# Returns what I should play to get the desired outcome
def needed_for_outcome(play, outcome):
    play = play.lower()
    outcome = outcome.lower()
    if outcome == 'win':
        if play == 'rock':
            return 'paper'
        elif play == 'paper':
            return 'scissors'
        elif play == 'scissors':
            return 'rock'
    elif outcome == 'loss':
        if play == 'rock':
            return 'scissors'
        elif play == 'paper':
            return 'rock'
        elif play == 'scissors':
            return 'paper'
    elif outcome == 'draw':
        return play

# Loop through data
myScore2 = 0

for i in range(len(data)):
    # Get play and strategy
    play = data[i].split(' ')[0]
    strategy = data[i].split(' ')[1]

    print(f'Play: {play}, Strategy: {strategy}')

    # Convert play to word
    play = input_to_word(play)

    # Convert strategy needed play for outcome
    if strategy.lower() == 'x':
        future_play = needed_for_outcome(play, 'loss')
    elif strategy.lower() == 'y':
        future_play = needed_for_outcome(play, 'draw')
    elif strategy.lower() == 'z':
        future_play = needed_for_outcome(play, 'win')
    else:
        print(f'Error: Invalid strategy input {strategy}')

    print(f'Future Play for {strategy}: {future_play}')

    # Get outcome
    outcome = rock_paper_scissors(future_play, play)

    # Get score
    temp_score = score(future_play, outcome)

    print(f'Outcome: {outcome}, Score: {temp_score}')

    # Add to total score
    myScore2 += temp_score

print(f'Total Score Part 2: {myScore2}')
