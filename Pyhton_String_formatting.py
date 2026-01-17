"""
Python String Formatting for Data Engineering

About this file:
- Explains string formatting in simple words
- Shows real-world Data Engineering examples
- Contains solved examples and practice tasks
- Includes only important interview questions

Topic Explanation (Simple):
String formatting means putting variable values inside text.
In Data Engineering, we use it to create logs, status messages,
and record-processing information.
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Pipeline status message
pipeline_name = "Daily Sales ETL"
status = "Success"

print(f"Pipeline {pipeline_name} completed with status {status}")


# Example 2: Record loading message
table_name = "orders"
record_count = 5000

print(f"Loaded {record_count} records into {table_name} table")


# Example 3: File processing log
file_name = "sales.csv"
rows = 1200

print(f"Processing file {file_name} with {rows} rows")


# Example 4: Execution time log
execution_time_seconds = 45
print(f"Pipeline finished in {execution_time_seconds} seconds")


# ==================================================
# 2️⃣ PRACTICE TASKS (DO YOURSELF)
# ==================================================

# TODO 1:
# Create variables:
# - source_name
# - total_files
# Print:
# "Source ___ has ___ files"

# TODO 2:
# Create variables:
# - pipeline_name
# - execution_time
# Print:
# "Pipeline ___ finished in ___ seconds"

# TODO 3:
# Create variables:
# - table_name
# - records_loaded
# Print:
# "Successfully loaded ___ records into ___ table"

# TODO 4:
# Create variable:
# - failed_records
# Print:
# "Pipeline failed for ___ records"


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is string formatting in Python?
# Q2: Why are f-strings preferred in Data Engineering logs?
# Q3: What happens if a variable inside {} is not defined?
# Q4: Where do we use string formatting in ETL pipelines?
# Tip for interview:
# "I use f-strings because they make logs clean, readable,
# and easy to maintain in data pipelines."
