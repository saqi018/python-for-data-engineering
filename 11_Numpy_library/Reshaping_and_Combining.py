"""
NumPy Reshaping & Combining for Data Engineering


Topic Explanation (Simple):
Imagine you have 6 LEGO blocks in a straight line (1D array).
You can break them apart and snap them together into a rectangle 
with 2 rows and 3 columns (2D array). It is the exact same data, 
just a new shape!

In Data Engineering, this is used to:
- Turn flat database lists into 2D tables (Reshaping).
- Stack new daily data on top of old data (Vertical Stacking / vstack).
- Add new columns of data next to old columns (Horizontal Stacking / hstack).
"""

import numpy as np

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Reshape a flat list into a table
flat_data = np.array([1, 2, 3, 4, 5, 6])
table_data = flat_data.reshape(2, 3)

print("Example 1: Reshape to 2x3 Table")
print(table_data)
print("-" * 30)


# Example 2: The Magic "-1" Trick (Automatic rows)
# We have 8 items. We want 2 columns. We use -1 to let NumPy calculate the rows (4).
data_8 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
magic_table = data_8.reshape(-1, 2)

print("Example 2: Magic -1 Trick")
print(magic_table)
print("-" * 30)


# Example 3: Vertical Stack (vstack)
# Gluing arrays on top of each other (like adding rows to a database)
user1 = np.array([1, 2, 3])
user2 = np.array([4, 5, 6])
v_combined = np.vstack((user1, user2))

print("Example 3: Vertical Stack")
print(v_combined)
print("-" * 30)


# Example 4: Horizontal Stack (hstack)
# Gluing arrays side-by-side (like adding a new column)
ids = np.array([101, 102])
ages = np.array([24, 45])
h_combined = np.hstack((ids, ages))

print("Example 4: Horizontal Stack")
print(h_combined)
print("-" * 30)


# Example 5: Flattening a 2D table
# Double brackets [[ ]] mean a 2D table. .flatten() destroys the table.
table = np.array([[1, 2],
                  [3, 4]])
flat_again = table.flatten()

print("Example 5: Flattening")
print(flat_again)
print("-" * 30)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# TODO 1:
# You have an array: arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# Reshape this array into a table with 4 rows and 2 columns. Print it.

# TODO 2:
# You have an array of 12 numbers: array = np.arange(1, 13)
# You want exactly 3 columns. Use the magic -1 trick to let NumPy figure
# out how many rows you need: array.reshape(-1, 3). Print it.

# TODO 3:
# group_a = np.array([1, 2, 3])
# group_b = np.array([4, 5, 6])
# Use .vstack() to stack group_b directly underneath group_a. Print it.

# TODO 4:
# names = np.array(["Ali", "Sara"])
# city = np.array(["Lahore", "Karachi"])
# Use .hstack() to put them side-by-side. Print it.

# TODO 5: (Mini Data Engineer Task)
# db_data = np.array([[100, 200], [300, 400], [500, 600]])
# Use .flatten() to smash this 2D database extract back into a 1D list. Print it.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is the rule for reshaping an array?
# Ans: The total number of items must remain the same (e.g., 6 items can be 2x3, but not 2x4).

# Q2: What does the -1 do in .reshape(-1, 2)?
# Ans: It acts as a placeholder. It tells NumPy to automatically calculate that dimension based on the length of the data.

# Q3: What is the difference between vstack and hstack?
# Ans: vstack stacks arrays vertically (adding rows), while hstack stacks them horizontally (adding columns).

# Q4: Why do we use double brackets `[[ ]]` when creating an array?
# Ans: The outer brackets represent the entire table, and the inner brackets represent individual rows, creating a 2D array.

# Q5: What does the .flatten() function do?
# Ans: It takes a multi-dimensional array (like a 2D table) and collapses it down into a single 1D flat list.
