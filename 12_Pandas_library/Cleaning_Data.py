"""
Pandas Transform Phase (Cleaning Data) for Data Engineering

Topic Explanation (Simple):
Real-world data looks like Swiss cheese—it is full of holes (NaN). 
You must either patch the holes (.fillna) or throw the slice away (.dropna).
You also must clean the "Ugly Desk" by renaming robotic database columns 
and throwing away columns you legally shouldn't have (like Passwords).

In Data Engineering, this is used to:
- Standardize column names before saving to a SQL database (.rename).
- Remove PII (Personally Identifiable Information) like credit cards (.drop).
- Ensure math functions don't crash by replacing NaN values with 0 (.fillna).
"""

import pandas as pd
import numpy as np

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Setup our messy data
messy_data = {
    "usr_nm": ["Ali", "Sara", "Zain"],
    "age": [25, np.nan, 22],
    "password": ["pass123", "qwerty", "admin"]
}
df = pd.DataFrame(messy_data)

print("Original Messy DataFrame:")
print(df)
print("-" * 30)

# Example 1: Renaming Columns
# We pass a dictionary {"old_name": "new_name"}
df_renamed = df.rename(columns={"usr_nm": "User_Name"})
print("Example 1: Renamed Columns")
print(df_renamed)
print("-" * 30)

# Example 2: Dropping Garbage/Secure Columns
df_dropped = df_renamed.drop(columns=["password"])
print("Example 2: Dropped Password Column")
print(df_dropped)
print("-" * 30)

# Example 3: Patching Holes (fillna)
df_filled = df_dropped.fillna(0)
print("Example 3: Patched NaN with 0")
print(df_filled)
print("-" * 30)

# Example 4: Throwing Away Holes (dropna)
# Let's recreate a hole just to show how dropna works
df_filled.loc[1, "age"] = np.nan
df_final = df_filled.dropna()
print("Example 4: Dropped the row with NaN")
print(df_final)
print("-" * 30)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# Setup:
messy_sales = {
    "cust_nm": ["Ali", "Sara", "Zain", "Omar"],
    "age": [25, np.nan, 22, 30],
    "credit_card": ["1234", "5678", "9012", "3456"],
    "city": ["Lahore", "Karachi", np.nan, "Islamabad"]
}
df_practice = pd.DataFrame(messy_sales)

# TODO 1: Rename "cust_nm" to "Customer_Name" and save to a new variable.
# TODO 2: Take that NEW variable, and drop the "credit_card" column. Save to another variable.
# TODO 3: Take that NEW variable, and use .fillna(0) to patch the missing data.
# TODO 4: Take the final variable and use .dropna() to clear out any remaining holes.
# Print your final, completely clean DataFrame!


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What does `NaN` stand for in Pandas?
# Ans: Not a Number. It is the default marker Pandas uses for missing or blank data.

# Q2: What is the difference between `dropna()` and `fillna()`?
# Ans: `dropna()` removes the entire row if it contains a missing value. `fillna()` keeps the row but replaces the missing value with a specific substitute (like 0 or "Unknown").

# Q3: If you run `df.drop(columns=["Age"])`, does it permanently delete the column from the original `df`?
# Ans: No. Pandas operations return a *copy* of the DataFrame. You must assign it to a new variable (like `clean_df = df.drop(...)`) or use the `inplace=True` argument to make it permanent.
