
#change directory to directory where file is located prior to parsing csv file: cd C:\Users\Cynthia\Desktop\Python\portfolioEarnings

#read CSV file to ensure values are as expected
import csv
rows = []
with open("Stock_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

#import csv
import csv
rows = []
with open("Stock_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

#import pandas
import pandas as pd

# Creating a DataFrame
df = pd.file(d)

# Creating a list of values
list = []
for i in range(len(df['numberOfShares'])):
    a = (df['numberOfShares'][i]*df['averageCost'][i])
    list.append(a)

# Creating a new column and assigning 
# its values as the list defined above
df['totalCost'] = list

# Display modified DataFrame
print("Modified DataFrame:\n",df)
    
