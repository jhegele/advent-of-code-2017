import csv

def get_check(val, row):
    divisors = [v for v in row if v != val and val % v == 0]
    if len(divisors) == 0:
        return 0
    return val / divisors[0]

checks = []
with open('input.txt') as input_file:
    reader = csv.reader(input_file, delimiter='\t')
    for row in reader:
        row = [int(value) for value in row]
        for value in row:
            checks.append(get_check(value, row))

print([c for c in checks if c > 0])
print(sum(checks))