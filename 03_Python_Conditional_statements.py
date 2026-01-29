"""
Python Conditional Statements for Data Engineering

About this file:
- Explains conditional statements in simple words
- Uses real-world Data Engineering examples
- Contains solved examples and practice tasks
- Includes only important interview questions

Topic Explanation (Simple):
Conditional statements help Python make decisions.
In Data Engineering, we use them to:
- Check pipeline status
- Validate data
- Control ETL flow
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Pipeline status check
pipeline_status = "success"

if pipeline_status == "success":
    print("Pipeline completed successfully")
else:
    print("Pipeline failed")


# Example 2: Record availability check
record_count = 0

if record_count > 0:
    print("Records available for processing")
else:
    print("No records found")


# Example 3: File batch size decision
file_count = 120

if file_count > 100:
    print("Large batch processing")
elif file_count > 0:
    print("Small batch processing")
else:
    print("No files to process")


# Example 4: Execution time check
execution_time_seconds = 45

if execution_time_seconds <= 30:
    print("Pipeline is fast")
else:
    print("Pipeline is slow")


# ==================================================
# 2️⃣ PRACTICE TASKS (DO YOURSELF)
# ==================================================

# TODO 1:
# Create variable:
# - failed_records
# If failed_records > 0 → print "Data quality issue"
# Else → print "Data is clean"

# TODO 2:
# Create variable:
# - environment
# If environment is "prod" → print "Running production pipeline"
# Else → print "Running test pipeline"

# TODO 3:
# Create variable:
# - rows
# If rows >= 1000 → print "High volume data"
# Else → print "Low volume data"

# TODO 4:
# Create variable:
# - job_status
# If job_status is "success" → print "Job passed"
# Else → print "Job failed"


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is the purpose of if-else in Python?
# Q2: What does == operator do?
# Q3: Where do we use conditions in Data Engineering?
# Q4: What happens if no condition is true?
# Tip for interview:
# "I use conditional statements to control ETL flow,
# validate data, and handle pipeline failures."
