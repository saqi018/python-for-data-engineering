"""
NumPy Axis (axis=0 vs axis=1) for Data Engineering


Topic Explanation (Simple):
A 2D array is just a table with rows and columns.
When you want to sum, average, or find the max of that table:
- axis=0 (The Elevator Drop): Crushes DOWN across the rows. It gives you the total for each COLUMN.
- axis=1 (The Train Smash): Crushes ACROSS the columns. It gives you the total for each ROW.

In Data Engineering, this is used to:
- Calculate daily revenue across all stores (axis=0).
- Calculate total monthly spending for a single customer (axis=1).
"""

import numpy as np

# Database table of sales.
# 3 stores (Rows) selling 2 products: Apples and Bananas (Columns).
sales_table = np.array([
    [10, 20],  # Store 1
    [30, 40],  # Store 2
    [50, 60]   # Store 3
])

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Sum Everything (No axis)
total_sales = np.sum(sales_table)
print("Example 1: Total of everything (No axis)")
print(total_sales)  # 210
print("-" * 30)

# Example 2: axis=0 (Crush DOWN) -> Column Totals
col_totals = np.sum(sales_table, axis=0)
print("Example 2: axis=0 (Total Apples, Total Bananas)")
print(col_totals)  # [90, 120]
print("-" * 30)

# Example 3: axis=1 (Crush ACROSS) -> Row Totals
row_totals = np.sum(sales_table, axis=1)
print("Example 3: axis=1 (Total for Store 1, Store 2, Store 3)")
print(row_totals)  # [30, 70, 110]
print("-" * 30)

# Example 4: Max value with axis=0 (Highest in each Column)
highest_in_cols = np.max(sales_table, axis=0)
print("Example 4: Max with axis=0 (Biggest Apple sale, Biggest Banana sale)")
print(highest_in_cols)  # [50, 60]
print("-" * 30)

# Example 5: Mean (Average) with axis=1 (Average for each Row)
average_per_store = np.mean(sales_table, axis=1)
print("Example 5: Mean with axis=1 (Average sales per store)")
print(average_per_store)  # [15. 35. 55.]
print("-" * 30)

# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# Database table representing 3 students and their scores in [Math, English, Science]
scores = np.array([
    [80, 90, 85],  # Student 1
    [60, 70, 65],  # Student 2
    [95, 95, 90]   # Student 3
])

# TODO 1: Find the overall total sum of EVERY score in the entire school. (Hint: no axis)
# TODO 2: Find the average (np.mean) score for EACH SUBJECT. (Hint: look DOWN the columns)
# TODO 3: Find the TOTAL sum (np.sum) of scores for EACH STUDENT. (Hint: look ACROSS the rows)
# TODO 4: Find the absolute lowest score (np.min) inside EACH SUBJECT.

# TODO 5: (Mini Data Engineer Task)
# You have a tiny table of website clicks. Rows = Days, Columns = Buttons.
clicks = np.array([
    [100, 5],
    [150, 8]
])
# Find the highest number of clicks (np.max) EACH DAY.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: In a 2D NumPy array, what does axis=0 represent?
# Ans: It represents operations moving vertically DOWN across the rows, resulting in column summaries.

# Q2: In a 2D NumPy array, what does axis=1 represent?
# Ans: It represents operations moving horizontally ACROSS the columns, resulting in row summaries.

# Q3: If I run `np.sum(array)` without an axis argument, what happens?
# Ans: NumPy will flatten the entire array and give you the sum of every single element inside it.
