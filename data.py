import csv
import pandas as pd

file = open('mailingList_full.csv')
df = pd.read_csv('mailingList_full.csv')

# for i in range(3436):
#     df.loc[i, 'ID'] = df.loc[i, 'ID'] + 'P'

# df['ID'] = df['ID'].astype(str) + 'P'

print(df.iloc[:,0])

# df.to_csv('mailingList_full.csv', index = False)

csvreader = csv.reader(file)

rows = []

for row in csvreader:
    rows.append(row)

# print(rows)