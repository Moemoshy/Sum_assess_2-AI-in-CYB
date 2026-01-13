import pandas as pd

# Create a simple dataset
data = {
    "Fruit": ["Apple", "Banana", "Orange", "Mango"],
    "Weight (g)": [180, 120, 150, 200],
    "Sweetness": [7, 9, 6, 9]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Show the whole table
print(df)

print("\nAverage weight:")
print(df["Weight (g)"].mean())

print("\nFruits with sweetness >= 8:")
print(df[df["Sweetness"] >= 8])
