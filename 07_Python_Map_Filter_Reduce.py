"""
Python Map, Filter, Reduce
For Data Engineering (Beginner Friendly)

Definitions (Easy Words):
- map    -> change or transform every item in a list
- filter -> remove items you do not want (keep only good ones)
- reduce -> combine many items into a single result (sum, total, etc.)
"""

from functools import reduce

# ==================================================
# 1️⃣ MAP: Transform each value
# ==================================================
print("MAP EXAMPLES")

numbers = [1, 2, 3, 4, 5]


def multiply_by_five(x):
    return x * 5


mapped_result = list(map(multiply_by_five, numbers))
print("Original:", numbers)
print("After map:", mapped_result)

# Real-life example: add processing fee
prices = [100, 200, 300]


def add_fee(price):
    return price + 10


final_prices = list(map(add_fee, prices))
print("Final Prices:", final_prices)


# ==================================================
# 2️⃣ FILTER: Remove bad data
# ==================================================
print("\nFILTER EXAMPLES")

records = [0, 50, 200, 0, 150]


def is_valid_record(value):
    return value > 0


filtered_records = list(filter(is_valid_record, records))
print("Original:", records)
print("After filter:", filtered_records)

# Real-life example: remove empty rows
data = [0, 20, 40, 0, 60]


def remove_empty(row):
    return row > 0


clean_data = list(filter(remove_empty, data))
print("Clean Data:", clean_data)


# ==================================================
# 3️⃣ REDUCE: Combine everything into ONE value
# ==================================================
print("\nREDUCE EXAMPLES")

values = [10, 20, 30]


def add_values(a, b):
    return a + b


total = reduce(add_values, values)
print("Values:", values)
print("Total:", total)

# Real-life example: total records processed
records_processed = [100, 200, 300, 400]


def total_records(x, y):
    return x + y


grand_total = reduce(total_records, records_processed)
print("Total Records Processed:", grand_total)


# ==================================================
# 4️⃣ COMBINED PIPELINE (REAL DATA ENGINEERING)
# ==================================================
print("\nCOMBINED PIPELINE")

raw_data = [0, 100, 200, 0, 300]


def clean_data_step(x):
    return x > 0


def transform_data_step(x):
    return x * 2


def aggregate_data_step(a, b):
    return a + b


# Step 1: filter bad data
cleaned = list(filter(clean_data_step, raw_data))
print("Cleaned:", cleaned)

# Step 2: transform data
transformed = list(map(transform_data_step, cleaned))
print("Transformed:", transformed)

# Step 3: aggregate data
final_result = reduce(aggregate_data_step, transformed)
print("Final Result:", final_result)


# ==================================================
# 5️⃣ UNSOLVED PRACTICE TASKS
# ==================================================

# TODO 1: MAP
# List of numbers: [2, 4, 6, 8]
# Multiply each number by 3 using map

# TODO 2: FILTER
# List of records: [0, 120, 0, 300, 50]
# Keep only non-zero records using filter

# TODO 3: REDUCE
# List of sales: [100, 200, 300]
# Find total sales using reduce

# TODO 4: COMBINED
# Raw data: [0, 10, 20, 0, 30]
# Steps:
# 1. Remove zeros using filter
# 2. Multiply remaining by 5 using map
# 3. Calculate final total using reduce


# ==================================================
# 6️⃣ INTERVIEW QUESTIONS
# ==================================================

# Q1: What is the difference between map, filter, and reduce?
# Q2: Where would you use map in an ETL pipeline?
# Q3: Where would you use filter in real data pipelines?
# Q4: Why reduce returns only one value?
# Q5: Can you use map and filter together? Give a simple example.
# Q6: Why do we often avoid lambda in production code for beginners?
# Tip: Answer Example:
# "I use map to transform data, filter to clean invalid data,
# and reduce to aggregate results in ETL pipelines."
