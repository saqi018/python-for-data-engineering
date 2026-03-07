"""
Pandas Series vs DataFrames for Data Engineering

Topic Explanation (Simple):
- A DataFrame is a 2D table (like an Excel spreadsheet or SQL table) with rows and columns.
- A Series is a 1D list. It is literally just a single column ripped out of a DataFrame.

In Data Engineering, this is used to:
- Load entire database tables into Python as DataFrames.
- Extract a single Series (like the "Salary" column) to clean it or apply math to it.
"""

import pandas as pd

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Creating a Series (1D Column)
# Notice how Pandas automatically adds an Index (row numbers) to the left side!
ages = pd.Series([25, 30, 45, 22])
print("Example 1: A Pandas Series")
print(ages)
print("-" * 30)

# Example 2: Creating a DataFrame (2D Table)
# We use a Python Dictionary. Keys = Column Names. Lists = The Data.
user_data = {
    "Name": ["Ali", "Sara", "Zain"],
    "Age": [25, 30, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(user_data)

print("Example 2: A Pandas DataFrame")
print(df)
print("-" * 30)

# Example 3: Extracting a Series from a DataFrame
# Just put the column name in brackets like a dictionary!
cities_only = df["City"]

print("Example 3: Extracting just the City column")
print(cities_only)
print("Type:", type(cities_only))  # Proves it is a Series!
print("-" * 30)

# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# TODO 1:
# Create a Series for three product prices: 150, 300, 500. Print it.

# TODO 2:
# Create a dictionary with "Product" (Mouse, Keyboard, Monitor) and "Price" (150, 300, 500).
# Turn it into a DataFrame called `items_df` and print it.

# TODO 3:
# Extract ONLY the "Product" column from `items_df` and print it.

# TODO 4: (Mini Data Engineer Task)
# Every DataFrame hides a raw NumPy array underneath.
# Print `items_df.values` to see the pure NumPy data without the pretty formatting.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is the main difference between a Series and a DataFrame?
# Ans: A Series is a 1-dimensional array (a single column), while a DataFrame is a 2-dimensional table made up of multiple Series glued together.

# Q2: How does Pandas relate to NumPy?
# Ans: Pandas is built directly on top of NumPy. Every column (Series) in a Pandas DataFrame is actually a NumPy array under the hood, which means it inherits all of NumPy's speed and vectorization capabilities.

# Q3: If you have a DataFrame named `df`, how do you extract a column named "Revenue"?
# Ans: You use bracket notation: `df["Revenue"]`.
