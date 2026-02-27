import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("Total Sales:")
print(df["Total_Sales"].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Total_Sales"].sum())

print("\nSales by Product:")
print(df.groupby("Product")["Total_Sales"].sum())
