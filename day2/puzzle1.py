import csv

checks = []
with open('input.txt') as input_file:
    reader = csv.reader(input_file, delimiter='\t')
    for row in reader:
        row = [int(value) for value in row]
        checks.append(max(row) - min(row))

print(sum(checks))