"""
Python Exception Handling for Data Engineering

About this file:
- Explains try, except, finally in very simple words
- Uses functions (real Data Engineering style)
- Contains solved examples
- Contains unsolved practice tasks
- Contains only important interview questions

Simple Definitions:
- try     : write code that may cause an error
- except  : handle the error so program does not crash
- finally : code that always runs (cleanup, logs, close files)

Why Data Engineers use it:
To keep pipelines running even if one file or record fails.
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Safe division using function


def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Division checked\n")


safe_divide(10, 2)
safe_divide(5, 0)


# Example 2: File reading with exception handling
def load_file(file_name):
    try:
        file = open(file_name)
        data = file.read()
        file.close()
        print(f"{file_name} loaded successfully")
    except FileNotFoundError:
        print(f"{file_name} not found")
    finally:
        print("File read attempt finished\n")


load_file("users.csv")
load_file("missing.csv")


# Example 3: Real Data Engineering pipeline
def run_pipeline(file_list):
    for file_name in file_list:
        try:
            file = open(file_name)
            data = file.read()
            file.close()
            print(f"{file_name} processed successfully")
        except FileNotFoundError:
            print(f"Skipping {file_name}")
        finally:
            print(f"Done with {file_name}\n")


files = ["users.csv", "orders.csv", "sales.csv"]
run_pipeline(files)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED – DO YOURSELF)
# ==================================================

# TODO 1:
# Create function: divide_numbers(a, b)
# Handle ZeroDivisionError
# Use finally to print "Division completed"

# TODO 2:
# Create function: read_any_file(file_name)
# Handle FileNotFoundError
# Use finally to print "Read finished"

# TODO 3:
# Create function: process_files(files)
# Loop through files
# Try opening each file
# If missing → print "File missing"
# Always print "Finished file"


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: Why is try-except better than if-else for error handling?
# Q2: What is the purpose of finally?
# Q3: Where do you use exception handling in data pipelines?
# Q4: Can a program continue after an exception?
# Q5: What happens if no exception occurs in try block?

# Interview Tip Answer:
# "In data engineering, try-except prevents pipeline crashes.
# It allows handling unexpected errors like missing files,
# bad data, or divide-by-zero while keeping the pipeline running."
