import mysql.connector
import pandas as pd

# Load CSV data
data = pd.read_csv("sales_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="H@rsh8319",  # Replace with your MySQL root password
    database="ecommerce"
)
cursor = conn.cursor()

# Insert each row into the orders table
for index, row in data.iterrows():
    sql = """
    INSERT INTO orders (order_date, product_id, product_name, category, price, quantity, revenue)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    # Convert NaN to None
    values = tuple(None if pd.isna(val) else val for val in row)
    cursor.execute(sql, values)

# Commit changes and close
conn.commit()
conn.close()

print("Data inserted successfully.")
