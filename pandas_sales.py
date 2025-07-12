# Step 2: Analysis using pandas
import pandas as pd

# Load CSV again (for pandas analysis)
df = pd.read_csv("sales_data.csv")

# Total Revenue
df['revenue'] = df['quantity'] * df['price']
total_revenue = df['revenue'].sum()
print(f"\nTotal Revenue: Rs.{total_revenue:,.2f}")

# Top 10 selling products
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Selling Products:\n", top_products)
