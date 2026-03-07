"""
NumPy Filtering, Masking & np.where for Data Engineering

Topic Explanation (Simple):
Imagine an array as a line of people waiting to get into a club. The rule is "Must be 18+".
1. Masking: The bouncer walks down the line and puts a True/False sticker on everyone.
2. Filtering: The door only opens for people with a "True" sticker.
3. np.where: Instead of kicking people out, the bouncer hands out "Adult" or "Kid" wristbands based on the rule.

In Data Engineering, this is used to:
- Remove bad data (like negative prices or ages over 200).
- Find specific records (like all users from "Peshawar").
- Create new columns based on rules (if sales > 1000, label as "High Value").
"""

import numpy as np

# A simple array of ages
ages = np.array([15, 20, 12, 25, 30])

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Creating a Mask (True/False Array)
# The bouncer checks the rule but doesn't kick anyone out yet.
mask = ages >= 18
print("Example 1: The Boolean Mask")
print(mask)  # [False  True False  True  True]
print("-" * 30)

# Example 2: Filtering (Applying the Mask)
# Put the condition inside brackets [ ] to keep only the True values.
adults = ages[ages >= 18]
print("Example 2: Filtered Array (Only Adults)")
print(adults)  # [20 25 30]
print("-" * 30)

# Example 3: Multiple Conditions (& for AND, | for OR)
# Rule: Must be 18 or older AND younger than 26.
# You MUST put parentheses () around each condition!
college_ages = ages[(ages >= 18) & (ages < 26)]
print("Example 3: Multiple Conditions")
print(college_ages)  # [20 25]
print("-" * 30)

# Example 4: np.where (The If-Else Machine)
# np.where(Condition, Do_This_If_True, Do_This_If_False)
labels = np.where(ages >= 18, "Allowed", "Denied")
print("Example 4: np.where labels")
print(labels)  # ['Denied' 'Allowed' 'Denied' 'Allowed' 'Allowed']
print("-" * 30)

# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# You are checking the prices of items in an online store (in Rupees).
prices = np.array([100, 500, 250, 800, 50])

# TODO 1:
# Create a mask (just the True/False array) for prices greater than 300. Print it.

# TODO 2:
# Filter the array to print ONLY the prices that are greater than 300.

# TODO 3:
# Use multiple conditions to filter and print prices that are greater than 100 AND less than 600.

# TODO 4:
# Use np.where() to create a new array. If the price is greater than 400, label it "Expensive".
# Else, label it "Cheap". Print the new array.

# TODO 5: (Mini Data Engineer Task)
# 1. Filter the array to find all prices greater than 200. Store this in a variable.
# 2. Find the average (np.mean) of those expensive items. Print the average.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is a "Boolean Mask" in NumPy?
# Ans: It is an array of True and False values used to filter another array based on a specific condition.

# Q2: Why do we use NumPy filtering instead of a normal Python `for` loop?
# Ans: NumPy filtering is vectorized (written in C underneath), meaning it applies the rule to the entire array instantly. A Python `for` loop is incredibly slow for millions of rows.

# Q3: What happens if you forget the parentheses when using multiple conditions like `arr > 10 & arr < 20`?
# Ans: Python will throw an error because it gets confused by the order of operations. You must always use `(arr > 10) & (arr < 20)`.

# Q4: Explain the three parts of the `np.where()` function.
# Ans: 1. The condition to check. 2. The value to return if the condition is True. 3. The value to return if the condition is False.
