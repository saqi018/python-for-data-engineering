"""
Python Variables for Data Engineering
Author: Saqib Khan
Purpose:
- Learn how to use variables in Python for ETL and data pipelines
- Includes solved examples, unsolved practice, and interview questions
- Beginner-friendly explanations inside comments

Topic Explanation:
- A variable is like a "box" to store data
- Variables have a name and a value
- Python variables can store numbers, text, or other data types
- Variables help track metadata, counts, and pipeline info in Data Engineering
"""

# ==================================================
# 1️⃣ TOPIC EXAMPLES (SOLVED)
# ==================================================

# 1. Number of files processed today
file_count = 120   # integer value
print("Number of files processed:", file_count)

# 2. Data source name and record count
source_name = "Sales CSV"   # string value
record_count = 25000        # integer value

print("Data Source:", source_name)
print("Number of records:", record_count)

# 3. Execution time of pipeline in seconds
execution_time_seconds = 45
print("Execution Time (seconds):", execution_time_seconds)

# 4. Total pipelines processed
total_pipelines = 5
print("Total Pipelines Processed:", total_pipelines)


# ==================================================
# 2️⃣ UNSOLVED PRACTICE (TODOs)
# ==================================================

# TODO 1: Create a variable for your favorite data source name

# TODO 2: Create a variable for number of failed records today

# TODO 3: Create a variable for pipeline execution time in minutes

# TODO 4: Print all variables in a formatted way like:
# "Pipeline XYZ processed 500 records in 45 seconds"

# TODO 5: Create two variables:
# - table_name
# - number_of_rows
# Print: "Table ___ has ___ rows"

# TODO 6: Create a variable for file size in MB and print it


# ==================================================
# 3️⃣ INTERVIEW QUIZ
# ==================================================

# Q1: What is a variable and why is it important in Data Engineering?
# Q2: Can a Python variable change its data type? Give an example.
# Q3: What characters are allowed in Python variable names?
# Q4: Why are meaningful variable names important in ETL pipelines?
# Q5: Which data types are most commonly used for:
#      - Number of files processed
#      - Table name
#      - Pipeline execution time


# ==================================================
# 4️⃣ BEST PRACTICES (Beginner + Professional)
# ==================================================

# - Use lowercase letters with underscores: e.g., file_count, pipeline_name
# - Avoid starting variable names with numbers or using special characters
# - Use meaningful names so anyone can understand the code
# - Group related variables together (counts, names, times)
# - Keep variable names short but descriptive for easier reading
