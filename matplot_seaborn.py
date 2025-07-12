import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: use a better style
sns.set(style="whitegrid")

# Load data
df = pd.read_csv("sales_data.csv")

# Calculate revenue column
df["revenue"] = df["price"] * df["quantity"]

# Convert order date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# -------------------------------
# 1. Top 10 Best-Selling Products
# -------------------------------
top_products = df.groupby("product_name")["quantity"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Best-Selling Products by Quantity")
plt.xlabel("quantity")
plt.ylabel("product_Name")
plt.tight_layout()
plt.savefig("top_10_products.png")
plt.show()

# -------------------------------
# 2. Revenue Over Time
# -------------------------------
daily_revenue = df.groupby("order_date")["revenue"].sum()

plt.figure(figsize=(14, 6))
daily_revenue.plot()
plt.title("Daily Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue (Rs)")
plt.tight_layout()
plt.savefig("revenue_over_time.png")
plt.show()

# -------------------------------
# 3. Category-wise Revenue
# -------------------------------
category_revenue = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=category_revenue.index, y=category_revenue.values, palette="rocket")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()

# -------------------------------
# 4. Daily Order Volume
# -------------------------------
daily_orders = df.groupby("order_date").size()

plt.figure(figsize=(14, 6))
daily_orders.plot(color="darkcyan")
plt.title("Number of Orders Per Day")
plt.xlabel("Date")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("daily_orders.png")
plt.show()

