import pandas as pd
df=pd.read_csv("messy_sales_data.csv")
# data frame structure
#print(df.to_string())
# data type
#print(df.dtypes)
# duplication check
#print(df.duplicated().sum())
#df=df.dropna()
#print(df.to_string())
text_cols = ["Product", "Category", "Region", "Salesperson"]

for col in text_cols:
    df[col] = df[col].str.strip().str.title()
#print(df[text_cols].to_string())
df=df.fillna({"Category":"Unknown","Region":"Unknown"})
#print(df["Category"])
df=df.dropna(subset=["Price"])
#print(df)
df=df[df["Quantity"]>0]
#print(df["Quantity"].to_string())

# conversion of  order_date into datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

#print(df["Order_Date"])
#Adding new column
df["Revenue"]=(df["Quantity"])*(df["Price"])
#print(df["Revenue"])
df["Order_Year"]=df["Order_Date"].dt.year
df["Order_Month"]=df["Order_Date"].dt.month_name()
#print(df[["Order_Year","Order_Month"]])
df["Is_valid_Order"]=df["Quantity"]>0
#print(df["Is_valid_Order"].to_string())

#Total Revune
#print("Total Revenue")
#print(df["Revenue"].sum())
# total revenue for ech product
group_Product=df.groupby("Product")
#print("Revenue by Product")
#print(group_Product["Revenue"].sum())

#revenue by category
#print("Revenue by Category")
group_Category=df.groupby("Category")
#print(group_Category["Revenue"].sum())

#revenue by region
#print("Revenue by Category")
group_Region=df.groupby("Region")
#print(group_Region["Revenue"].sum())

#monthly revenue trend
#print("Reevenue trend by month")
group_Month=df.groupby("Order_Month")
#print(group_Month["Revenue"].sum())

#top3 product by revenue
top_product=group_Product["Revenue"].sum()
print("The top 3 product by product : ")
print(top_product.sort_values().head(3))

#avg order value
print("Average order value : ")
print(f'{df["Revenue"].mean():.2f}' )

#best salesmanq
group_salesperson = df.groupby("Salesperson")["Revenue"].sum()

print(" Best Salesperson:")
print(group_salesperson.sort_values(ascending=False).head(1))

print("\nSalesperson with Least Sales:")
print(group_salesperson.sort_values(ascending=True).head(1))
