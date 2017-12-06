with open('input.txt', 'r') as input_file:
    puzzle_input = list(map(int, input_file.readline().split('\t')))

prior_states = []
curr_state = puzzle_input
cycles = 0
while curr_state not in prior_states:
    prior_states.append(curr_state[:])
    blocks = max(curr_state)
    idx = curr_state.index(blocks) + 1
    curr_state[curr_state.index(blocks)] = 0
    while blocks > 0:
        idx = 0 if idx >= len(curr_state) else idx
        curr_state[idx] += 1
        idx += 1
        blocks -= 1
    cycles += 1

print('{} cycles'.format(cycles))
print('{} loop size'.format(cycles - prior_states.index(curr_state)))
