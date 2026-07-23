






import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------
# MYSQL CONNECTION
# ---------------------------------------

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="vikki1507",
    database="RetailSales"
)

print("Database Connected Successfully")

# ---------------------------------------
# Create Folder
# ---------------------------------------

if not os.path.exists("charts"):
    os.makedirs("charts")

sns.set(style="whitegrid")

# =======================================
# CHART 1
# Sales by Product Category
# =======================================

query = """
SELECT
p.category,
SUM(p.price*o.quantity) AS TotalSales
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY p.category
ORDER BY TotalSales DESC;
"""

df = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,x="category",y="TotalSales")
plt.title("Sales by Category")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.show()

# =======================================
# CHART 2
# Orders by Status
# =======================================

query="""
SELECT
order_status,
COUNT(*) TotalOrders
FROM orders
GROUP BY order_status;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(7,5))
plt.pie(df["TotalOrders"],
labels=df["order_status"],
autopct="%1.1f%%",
startangle=90)
plt.title("Orders by Status")
plt.savefig("charts/order_status.png")
plt.show()

# =======================================
# CHART 3
# Payment Method
# =======================================

query="""
SELECT
payment_method,
COUNT(*) Total
FROM orders
GROUP BY payment_method;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,
x="payment_method",
y="Total")
plt.title("Orders by Payment Method")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("charts/payment_method.png")
plt.show()

# =======================================
# CHART 4
# Customer Distribution
# =======================================

query="""
SELECT
city,
COUNT(*) Customers
FROM customers
GROUP BY city;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,
x="city",
y="Customers")
plt.title("Customers by City")
plt.tight_layout()
plt.savefig("charts/customer_city.png")
plt.show()

# =======================================
# CHART 5
# Top Products
# =======================================

query="""
SELECT
p.product_name,
SUM(o.quantity) Qty
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY p.product_name
ORDER BY Qty DESC
LIMIT 10;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(10,6))
sns.barplot(data=df,
y="product_name",
x="Qty")
plt.title("Top 10 Selling Products")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.show()

# =======================================
# CHART 6
# Monthly Revenue
# =======================================

query="""
SELECT
MONTH(order_date) Month,
SUM(p.price*o.quantity) Revenue
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY MONTH(order_date)
ORDER BY MONTH(order_date);
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(9,5))
sns.lineplot(data=df,
x="Month",
y="Revenue",
marker="o")
plt.title("Monthly Revenue")
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.show()

# =======================================
# CHART 7
# Brand Wise Revenue
# =======================================

query="""
SELECT
brand,
SUM(price*quantity) Revenue
FROM orders o
JOIN products p
ON o.product_id=p.product_id
GROUP BY brand;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,
x="brand",
y="Revenue")
plt.title("Revenue by Brand")
plt.tight_layout()
plt.savefig("charts/brand_revenue.png")
plt.show()

# =======================================
# CHART 8
# Average Rating by Brand
# =======================================

query="""
SELECT
brand,
AVG(rating) Rating
FROM products
GROUP BY brand;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,
x="brand",
y="Rating")
plt.title("Average Rating")
plt.tight_layout()
plt.savefig("charts/brand_rating.png")
plt.show()

# =======================================
# CHART 9
# Stock by Category
# =======================================

query="""
SELECT
category,
SUM(stock_quantity) Stock
FROM products
GROUP BY category;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(8,5))
sns.barplot(data=df,
x="category",
y="Stock")
plt.title("Available Stock")
plt.tight_layout()
plt.savefig("charts/stock_category.png")
plt.show()

# =======================================
# CHART 10
# Age Distribution
# =======================================

query="""
SELECT age
FROM customers;
"""

df=pd.read_sql(query,conn)

plt.figure(figsize=(8,5))
sns.histplot(df["age"],bins=10)
plt.title("Customer Age Distribution")
plt.tight_layout()
plt.savefig("charts/customer_age.png")
plt.show()

conn.close()

print("Analysis Completed")