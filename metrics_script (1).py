
import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv", parse_dates=["Order Date"])

# Clean data
df.dropna(inplace=True)
df["Order Amount"] = pd.to_numeric(df["Order Amount"], errors="coerce")

# Daily Revenue
daily_revenue = df.groupby("Order Date")["Order Amount"].sum().reset_index()
daily_revenue.columns = ["Date", "Total Revenue"]

# Average Order Value (AOV)
aov = df.groupby("Order Date")["Order Amount"].mean().reset_index()
aov.columns = ["Date", "Average Order Value"]

# Customer Repeat Rate
repeat_rate = df.groupby("Customer ID").size().reset_index(name="Order Count")
repeat_customers = repeat_rate[repeat_rate["Order Count"] > 1].shape[0]
repeat_rate_percent = (repeat_customers / df["Customer ID"].nunique()) * 100

# Save metrics
daily_revenue.to_csv("daily_revenue.csv", index=False)
aov.to_csv("average_order_value.csv", index=False)

print("Repeat Customer Rate: {:.2f}%".format(repeat_rate_percent))
print("Metrics files saved: daily_revenue.csv, average_order_value.csv")
