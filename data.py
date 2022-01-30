import csv

file = open('mailingList_full.csv')

csvreader = csv.reader(file)

rows = []

for row in csvreader:
    rows.append(row)

print(rows)