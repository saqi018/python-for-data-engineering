"""
Pandas Searching & Filtering (loc, iloc, masks) for Data Engineering

Topic Explanation (Simple):
- .iloc (Integer Location): Used when you know the exact row NUMBER (like Row 0).
- .loc (Location): Used when you want to look up a specific row and COLUMN NAME.
- Filtering: You create a rule (like Price > 500). Pandas checks every row, gives it a True/False sticker, and only keeps the True rows.

In Data Engineering, this is used to:
- Find specific corrupted rows by their index number.
- Filter out bad data (e.g., keep only users where Status == "Active").
- Extract specific subsets of data to send to different databases.
"""

import pandas as pd

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Setup our database table
data = {
    "Name": ["Ali", "Sara", "Zain", "Omar"],
    "Department": ["IT", "HR", "IT", "Sales"],
    "Salary": [60000, 50000, 75000, 45000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("-" * 30)

# Example 1: .iloc (Finding by Row Number)
first_employee = df.iloc[0]
print("Example 1: First row using .iloc[0]")
print(first_employee)
print("-" * 30)

# Example 2: .loc (Finding by Row Number AND Column Name)
zain_dept = df.loc[2, "Department"]
print("Example 2: Zain's Department using .loc")
print(zain_dept)
print("-" * 30)

# Example 3: Filtering with one rule (The VIP Bouncer)
high_earners = df[df["Salary"] > 55000]
print("Example 3: Employees making more than 55k")
print(high_earners)
print("-" * 30)

# Example 4: Filtering with multiple rules (& for AND)
# Must use parentheses () around each rule!
top_it = df[(df["Department"] == "IT") & (df["Salary"] > 65000)]
print("Example 4: IT employees making more than 65k")
print(top_it)
print("-" * 30)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# Setup:
orders_data = {
    "OrderID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Laptop", "Keyboard", "Monitor"],
    "Price": [1200, 25, 1200, 45, 300],
    "Status": ["Delivered", "Pending", "Delivered", "Delivered", "Pending"]
}
orders_df = pd.DataFrame(orders_data)

# TODO 1: Use .iloc to extract and print the very last row (Row 4).
# TODO 2: Use .loc to print the exact "Status" of the order at Row 1.
# TODO 3: Filter the table to show ONLY the rows where Status == "Pending". Print it.
# TODO 4: Filter the table to show rows where Product == "Laptop" AND Price > 1000. Print it.

# TODO 5: (Mini Data Engineer Task)
# 1. Filter the table for only "Delivered" orders and save it to a variable.
# 2. Grab the "Price" column from that new variable and use .mean() to find the average. Print it.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is the exact difference between `.iloc` and `.loc`?
# Ans: `.iloc` is strictly integer-based (you must use numbers for rows and columns). `.loc` is label-based (you use the actual names of the rows or columns).

# Q2: When writing a Pandas filter with multiple conditions, why do you get an error if you forget the parentheses `()`?
# Ans: Python gets confused by the order of operations between the comparison operators (like `>`) and the bitwise operator (`&`). The parentheses force Python to evaluate the rules first.

# Q3: How do you calculate the average of a specific column after filtering a DataFrame?
# Ans: You must isolate the column first before calling the function. Example: `filtered_df["ColumnName"].mean()`.
