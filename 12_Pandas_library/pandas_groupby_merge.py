"""
Pandas Group By & Merging for Data Engineering

Topic Explanation (Simple):
- Merging: Taking two separate tables and gluing them together based on a matching column (like an ID).
- Group By: Splitting a giant table into smaller piles (like grouping by City), applying math to each pile (like .sum()), and combining it back into a summary table.

In Data Engineering, this is used to:
- Join "Orders" data with "Customer Profiles" to get a complete picture.
- Aggregate daily millions of rows into monthly summaries to save database space.
"""

import pandas as pd

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Table A: Salaries
salaries = pd.DataFrame({
    "EmpID": [101, 102, 103],
    "Salary": [60000, 80000, 55000]
})

# Table B: Departments
departments = pd.DataFrame({
    "EmpID": [101, 102, 103],
    "Dept": ["IT", "Sales", "IT"]
})

# Example 1: Merging (The Puzzle Pieces)
# Glue them together ON the "EmpID" column!
merged_df = pd.merge(salaries, departments, on="EmpID", how="inner")

print("Example 1: Merged Table")
print(merged_df)
print("-" * 30)

# Example 2: Group By (The Box of Receipts)
# Find the total salary cost for EACH department
dept_costs = merged_df.groupby("Dept")["Salary"].sum()

print("Example 2: Total Salary by Department")
print(dept_costs)
print("-" * 30)

# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# Setup:
salaries_df = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Salary": [60000, 80000, 55000, 90000]
})

departments_df = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Name": ["Ali", "Sara", "Zain", "Omar"],
    "Dept": ["IT", "Sales", "IT", "HR"]
})

# TODO 1: Merge the two tables together on "EmpID" using an inner join. Print it.
# TODO 2: Group the merged table by "Dept", grab the "Salary" column, and find the .mean(). Print it.
# TODO 3: Filter the merged table to show ONLY employees making more than 70,000. Print it.

# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is the equivalent of Pandas `.merge()` in SQL?
# Ans: The SQL `JOIN` clause. `how="inner"` is an INNER JOIN, `how="left"` is a LEFT JOIN.

# Q2: Explain the three steps of a `.groupby()` operation.
# Ans: Split (divide data into groups), Apply (perform a function like mean/sum), Combine (put the results back into a new DataFrame).
