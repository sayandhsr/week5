import pandas as pd
import matplotlib.pyplot as plt

# Load data
sales = pd.read_csv(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week5\sales_data (1).csv")
customers = pd.read_csv(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week5\customer_churn.csv")

# Clean columns
sales.columns = sales.columns.str.strip().str.lower()
customers.columns = customers.columns.str.strip().str.lower()

print("Sales Columns:", sales.columns)
print("Customer Columns:", customers.columns)

# ✅ FORCE SAME COLUMN NAME (THIS SOLVES EVERYTHING)
customers['customer_id'] = customers['customerid']

# Convert date
sales['date'] = pd.to_datetime(sales['date'])

# New columns
sales['month'] = sales['date'].dt.month
sales['year'] = sales['date'].dt.year
sales['total_sales'] = sales['quantity'] * sales['price']

# ✅ SIMPLE MERGE (NOW WILL WORK 100%)
df = pd.merge(sales, customers, on='customer_id', how='left')

# Metrics
total_revenue = df['total_sales'].sum()
total_customers = df['customer_id'].nunique()
avg_order_value = df['total_sales'].mean()

customer_sales = df.groupby('customer_id')['total_sales'].sum()
top_customer = customer_sales.idxmax()
top_value = customer_sales.max()

print("\nREPORT")
print("="*40)
print("Revenue:", total_revenue)
print("Customers:", total_customers)
print("Avg Order:", avg_order_value)
print("Top Customer:", top_customer, top_value)

# Charts
monthly_sales = df.groupby('month')['total_sales'].sum()

plt.figure()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales")
plt.savefig(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week5\monthly_sales.png")

region_sales = df.groupby('region')['total_sales'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Region Sales")
plt.savefig(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week5\region_sales.png")

top5 = customer_sales.nlargest(5)

plt.figure()
top5.plot(kind='bar')
plt.title("Top Customers")
plt.savefig(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week5\top_customers.png")

print("\nDONE ✅")