"""
Python Data Structures for Data Engineering

About this file:
- Explains List, Tuple, Set, Dictionary in simple words
- Uses real Data Engineering examples
- Contains solved examples
- Contains practice (unsolved) tasks
- Includes only important interview questions
"""

# ==================================================
# 1️⃣ LIST (Mutable, Ordered, Allows Duplicates)
# Used for: files, records, batches
# ==================================================

# ✅ SOLVED EXAMPLES

files = ["sales.csv", "users.csv", "orders.csv"]
print(files)

# Add item at end
files.append("products.csv")
print(files)

# Access by index
print(files[0])

# Loop through list
for file in files:
    print(f"Processing file: {file}")

# Length of list
print(len(files))


# ❓ PRACTICE (UNSOLVED)
# TODO:
# 1. Create a list of table names
# 2. Add a new table
# 3. Print all tables using loop


# ==================================================
# 2️⃣ TUPLE (Immutable, Ordered, No change allowed)
# Used for: constants, environments, fixed configs
# ==================================================

# ✅ SOLVED EXAMPLES

environments = ("dev", "test", "prod")
print(environments)

# Access tuple value
print(environments[2])

# Loop through tuple
for env in environments:
    print(f"Environment: {env}")

# Length
print(len(environments))


# ❓ PRACTICE (UNSOLVED)
# TODO:
# 1. Create a tuple of file formats
# 2. Print each format using loop
# 3. Print total number of formats


# ==================================================
# 3️⃣ SET (Unordered, Unique values only)
# Used for: unique IDs, file types, deduplication
# ==================================================

# ✅ SOLVED EXAMPLES

file_types = {"csv", "json", "csv"}
print(file_types)   # duplicates removed

# Add item
file_types.add("parquet")
print(file_types)

# Remove item
file_types.remove("json")
print(file_types)

# Loop through set
for file_type in file_types:
    print(f"Supported type: {file_type}")


# ❓ PRACTICE (UNSOLVED)
# TODO:
# 1. Create a set of user IDs (include duplicates)
# 2. Print unique IDs
# 3. Add one new ID
# 4. Remove one ID


# ==================================================
# 4️⃣ DICTIONARY (Key - Value pairs)
# Used for: pipeline config, job metadata, logs
# ==================================================

# ✅ SOLVED EXAMPLES

pipeline = {
    "name": "sales_etl",
    "source": "mysql",
    "status": "success"
}

print(pipeline)

# Access value
print(pipeline["source"])

# Add new key
pipeline["records_loaded"] = 5000
print(pipeline)

# Update value
pipeline["status"] = "completed"
print(pipeline)

# Loop key + value
for key, value in pipeline.items():
    print(key, "=>", value)

# Safe access
print(pipeline.get("execution_time"))


# ❓ PRACTICE (UNSOLVED)
# TODO:
# 1. Create dictionary for job:
#    id, name, role
# 2. Add salary
# 3. Update role
# 4. Remove salary
# 5. Print keys only
# 6. Print values only


# ==================================================
# 🎯 IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: Difference between list and tuple?
# Q2: Why use set in data pipelines?
# Q3: When do you use dictionary in ETL?
# Q4: Difference between items(), keys(), values()?
# Q5: Why dictionary is important for configs?

# Interview Tip:
# "I use lists for files and records,
# tuples for constants,
# sets for uniqueness,
# and dictionaries for pipeline metadata."
