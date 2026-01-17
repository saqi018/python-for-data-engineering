"""
Python Loops (for & while) for Data Engineering

About this file:
- Explains loops in simple words
- Uses real-world Data Engineering examples
- Contains solved examples and practice tasks
- Includes only important interview questions

Topic Explanation (Simple):
Loops repeat tasks again and again.
In Data Engineering, loops are used to:
- Process multiple files
- Handle batch jobs
- Retry failed pipelines
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: for loop – processing multiple files
files = ["sales.csv", "users.csv", "orders.csv"]

for file in files:
    print(f"Processing file: {file}")


# Example 2: for loop – batch processing
for batch_number in range(1, 6):
    print(f"Processing batch {batch_number}")


# Example 3: for loop – filtering record counts
record_counts = [100, 200, 300]

for count in record_counts:
    if count > 100:
        print(f"Records processed: {count}")


# Example 4: while loop – retry logic
retry_count = 0

while retry_count < 3:
    print("Retrying pipeline")
    retry_count = retry_count + 1


# Example 5: while loop – waiting for data
records_loaded = 0

while records_loaded == 0:
    print("Waiting for data")
    records_loaded = 500


# ==================================================
# 2️⃣ PRACTICE TASKS (DO YOURSELF)
# ==================================================

# TODO 1:
# Create a list of table names
# Use a for loop to print:
# "Loading table: ___"

# TODO 2:
# Use range() to print numbers from 1 to 10

# TODO 3:
# Create variable attempt = 0
# Use while loop to print "Attempting job execution"
# Stop after 5 attempts

# TODO 4:
# Create a list of record counts
# Print only values greater than 100


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is a loop in Python?
# Q2: Difference between for loop and while loop?
# Q3: Where are loops used in Data Engineering?
# Q4: What is an infinite loop?
# Tip for interview:
# "I use loops to process multiple files,
# handle retries, and run batch jobs in ETL pipelines."
