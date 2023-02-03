# Importing pandas package
import pandas as pd

# Creating a Dictionary
d = {
    'stockTicker':["FLWS","BMBL","COUP","GPS","GTLB","PHG","LYFT","MTCH","META","OKTA","PTON","PINS","ROKU","SOFI","PATH","U","W","WIX","ZG"],
    'numberOfShares':[55,13,4,10,5,37,87,16,10,33,132,69,11,81,109,7,41,46,16],
    'averageCost': [6.38,16.26,65.78,11.7,37.05,13.73,13.92,44.84,94.13,56.21,13.08,24.63,63.69,5.31,16.08,33.33,46.43,72.38,29.65],
    'projectedValue': [17.84,40.45,186,24.87,125,47.08,62.79,103.65,328.73,137,49.22,51.64,139.61,10.69,26.21,78.86,131,162.87,55.2]
}

# Creating a DataFrame
df = pd.DataFrame(d)

# Display original DataFrame
print("Original DataFrame:\n",df,"\n")

# Creating a list of total share cost values
list = []
for i in range(len(df['numberOfShares'])):
    a = (df['numberOfShares'][i]*df['averageCost'][i])
    list.append(a)

# Creating a new column and assigning 
# its values as the list defined above
df['totalCost'] = list

# Creating a list of project stock values
list = []
for i in range(len(df['numberOfShares'])):
    b = (df['numberOfShares'][i]*df['projectedValue'][i])
    list.append(b)

# Creating a new column and assigning 
# its values as the list defined above
df['totalValue'] = list

# Creating a list of project stock values
list = []
for i in range(len(df['numberOfShares'])):
    c = (df['totalValue'][i]-df['totalCost'][i])
    list.append(c)

# Creating a new column and assigning 
# its values as the list defined above
df['projectedEarnings'] = list

# Creating a list of percentage changes
list = []
for i in range(len(df['numberOfShares'])):
    d = round(((df['totalValue'][i]-df['totalCost'][i])/df['totalCost'][i])*100)
    list.append(d)

# Creating a new column and assigning 
# its values as the list defined above
df['projectedChange(%)'] = list

#Summing projected earnings 
totalCosts = df['totalCost'].sum()

#Summing projected earnings 
totalProjectedEarnings = df['projectedEarnings'].sum()

#Averaging projected change
totalProjectedChange = round(df['projectedChange(%)'].mean())

# Display modified DataFrame
print("Modified DataFrame:\n",df)
print("Total costs of this portfolio ($):")
print (totalCosts)
print("Total projected earnings for this portfolio ($):")
print (totalProjectedEarnings)
print("Average projected change for this portfolio (%):")
print(totalProjectedChange)

