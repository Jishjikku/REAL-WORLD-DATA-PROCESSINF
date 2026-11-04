# Task 4: Real-world Data Project — Retail Sales Analysis
# This project uses a clearly labelled sample retail dataset for demonstration.
# Run: python task4_retail_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "retail_sales_raw.csv"
OUT = Path(__file__).resolve().parent
df = pd.read_csv(DATA).drop_duplicates()
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["region"] = df["region"].fillna("Unknown")
df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].median())
df = df.dropna(subset=["date","sales_amount"])
category = df.groupby("category").agg(total_sales=("sales_amount","sum"), units=("units_sold","sum"), avg_rating=("customer_rating","mean")).sort_values("total_sales", ascending=False)
region = df.groupby("region")["sales_amount"].sum().sort_values(ascending=False)
monthly = df.groupby(df["date"].dt.to_period("M"))["sales_amount"].sum()

print("RETAIL SALES BUSINESS REPORT")
print("\nCategory performance:\n", category.round(2))
print("\nRegional sales:\n", region.round(2))
print("\nMonthly sales:\n", monthly.round(2))
print("\nRecommendations:")
print("1. Prioritize inventory for categories with the highest total sales.")
print("2. Compare regional sales before allocating advertising budgets.")
print("3. Monitor customer ratings alongside sales to identify service issues.")
print("4. Review monthly trends when planning promotions and stock.")
category["total_sales"].plot(kind="bar", title="Retail Sales by Category")
plt.ylabel("Total sales"); plt.tight_layout(); plt.savefig(OUT/"retail_category_performance.png", dpi=150); plt.close()
monthly.plot(kind="line", marker="o", title="Monthly Retail Sales")
plt.ylabel("Total sales"); plt.tight_layout(); plt.savefig(OUT/"retail_monthly_sales.png", dpi=150); plt.close()
category.to_csv(OUT/"category_summary.csv")
region.to_csv(OUT/"region_summary.csv")
print("\nSummary files and charts saved to:", OUT)
