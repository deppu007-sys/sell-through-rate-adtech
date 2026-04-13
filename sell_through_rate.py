import pandas as pd

# Product dataset
data = {
    "Product": ["Product_A", "Product_B", "Product_C", "Product_D"],
    "Units_Available": [100, 200, 150, 120],
    "Units_Sold": [70, 50, 120, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Sell Through Rate
df["Sell_Through_Rate"] = df["Units_Sold"] / df["Units_Available"]

# Convert to percentage
df["STR (%)"] = df["Sell_Through_Rate"] * 100

# Print data
print("📦 Product Sell Through Data:\n")
print(df)

# Best selling product
best_product = df.loc[df["Sell_Through_Rate"].idxmax()]

print("\n🏆 Best Selling Product:")
print(best_product)
