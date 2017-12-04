valid = 0

def sort_word(word):
    return ''.join(sorted([c for c in word]))

with open('input.txt', 'r') as puzzle_input:
    for line in puzzle_input.readlines():
        words = [sort_word(word) for word in line.strip().split(' ')]
        if len(set(words)) == len(words):
            valid += 1

print('{} valid'.format(valid))