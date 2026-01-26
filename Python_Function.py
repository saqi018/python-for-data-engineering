"""
Python Functions for Data Engineering

About this file:
- Explains Python functions in very simple words
- Uses real-world Data Engineering examples
- Includes solved examples, practice tasks, and interview questions
- Helps build strong logic for ETL and data pipelines

Topic Explanation (Simple):
A function is a reusable block of code.
Instead of writing the same code again and again,
we put it inside a function and call it when needed.

In Data Engineering, functions are used to:
- Load data
- Process files
- Validate records
- Check pipeline status
- Reuse ETL logic
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Simple function


def show_pipeline_status():
    print("Pipeline completed successfully")


show_pipeline_status()


# Example 2: Function with input (parameter)
def process_file(file_name):
    print(f"Processing file: {file_name}")


process_file("sales.csv")
process_file("users.csv")


# Example 3: Function with multiple inputs
def load_records(table_name, record_count):
    print(f"Loaded {record_count} records into {table_name} table")


load_records("orders", 5000)


# Example 4: Function that returns a value
def calculate_total_records(a, b):
    return a + b


total = calculate_total_records(200, 300)
print(total)


# Example 5: Function with condition
def check_pipeline_status(status):
    if status == "success":
        return "Pipeline Passed"
    else:
        return "Pipeline Failed"


print(check_pipeline_status("success"))
print(check_pipeline_status("failed"))


# Example 6: Function with default value
def process_batch(batch_number=1):
    print(f"Processing batch {batch_number}")


process_batch()
process_batch(5)


# Example 7: Function calling another function
def log_file_processing(file_name):
    process_file(file_name)
    print("Finished processing")


log_file_processing("sales.csv")


# Example 8: Real ETL-style function
def etl_pipeline(file_name, table_name, record_count):
    print(f"Processing file: {file_name}")
    print(f"Loading {record_count} records into {table_name}")
    return f"ETL completed for {table_name}"


result = etl_pipeline("sales.csv", "orders", 5000)
print(result)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# TODO 1:
# Create a function show_environment
# Print: "Running in production"

# TODO 2:
# Create a function process_table(table_name)
# Print: "Processing table ___"

# TODO 3:
# Create a function add_numbers(x, y)
# Return the sum of x and y

# TODO 4:
# Create a function validate_data(record_count)
# If record_count > 0 return "Data Valid"
# Else return "No Data Found"

# TODO 5:
# Create a function pipeline_summary(name, status)
# Print: "Pipeline ___ finished with status ___"


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is a function in Python?
# Q2: Why are functions important in Data Engineering?
# Q3: Difference between print and return?
# Q4: What are parameters and arguments?
# Q5: Can one function call another function?
#
# Interview Tip:
# "I use functions to reuse ETL logic, keep pipelines clean,
# and make debugging easier."
