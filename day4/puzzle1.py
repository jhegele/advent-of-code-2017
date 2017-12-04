valid = 0

with open('input.txt', 'r') as puzzle_input:
    for line in puzzle_input.readlines():
        if len(set(line.strip().split(' '))) == len(line.strip().split(' ')):
            print(line.strip())
            valid += 1

print('{} valid'.format(valid))