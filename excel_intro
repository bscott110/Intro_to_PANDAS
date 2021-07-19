import pandas as pd

#I have an excel sheet of real-life expenses. I'm simply trying to sort expenses from low to high
df = pd.read_excel(r"C:\Users\blake\Downloads\2019FoodGasSample.xlsx",sheet_name="2019FoodGasSample")
#print(df), this is a test

#column name where expense total for each item resides
amount = df["Amount"]
sort_amt_col = amount.sort_values(ascending=False)
print(sort_amt_col)

#other interesting statistics pulled
#print(amount.mean())
#print(amount.median())
#print(amount.mode())
