with open('input.txt', 'r') as puzzle_input:
    jumps = [int(line.strip()) for line in puzzle_input.readlines()]

steps = 0
curr_idx = 0
while curr_idx < len(jumps):
    move = jumps[curr_idx]
    jumps[curr_idx] += -1 if jumps[curr_idx] >= 3 else 1
    curr_idx += move
    steps += 1

print('{} steps taken'.format(steps))