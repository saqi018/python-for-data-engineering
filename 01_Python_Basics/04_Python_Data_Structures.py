"""
Python Data Structures for Data Engineering

# ==================================================
# 1️⃣ LIST (Mutable, Ordered, Allows Duplicates)
# Used for: files, records, batches
# ==================================================
"""
# ✅ SOLVED EXAMPLES

files = ["sales.csv", "users.csv", "orders.csv"]
print("Original List:", files)

# Add item at end
files.append("products.csv")
print("After Append:", files)

# Access by index
print("Index 0:", files[0])

# Loop through list
for file in files:
    print(f"Processing file: {file}")

# Length of list
print("Total files:", len(files))
print("-" * 30)


# 🟢 SOLVED PRACTICE
# 1. Create a list of table names
tables = ["raw_users", "raw_sales"]
# 2. Add a new table
tables.append("raw_inventory")
# 3. Print all tables using loop
for table in tables:
    print(f"Uploading to: {table}")
print("-" * 30)


# ==================================================
# 2️⃣ TUPLE (Immutable, Ordered, No change allowed)
# Used for: constants, environments, fixed configs
# ==================================================

# ✅ SOLVED EXAMPLES

environments = ("dev", "test", "prod")
print("Environments:", environments)

# Access tuple value
print("Production is at index 2:", environments[2])

# Loop through tuple
for env in environments:
    print(f"Environment: {env}")

# Length
print("Total envs:", len(environments))
print("-" * 30)


# 🟢 SOLVED PRACTICE
# 1. Create a tuple of file formats
formats = ("csv", "json", "parquet", "avro")
# 2. Print each format using loop
for fmt in formats:
    print(f"Supported format: {fmt}")
# 3. Print total number of formats
print("Total formats supported:", len(formats))
print("-" * 30)


# ==================================================
# 3️⃣ SET (Unordered, Unique values only)
# Used for: unique IDs, file types, deduplication
# ==================================================

# ✅ SOLVED EXAMPLES

file_types = {"csv", "json", "csv"}
print("Set removes duplicates:", file_types)

# Add item
file_types.add("parquet")
print("After adding:", file_types)

# Remove item
file_types.remove("json")
print("After removing:", file_types)

# Loop through set
for file_type in file_types:
    print(f"Supported type: {file_type}")
print("-" * 30)


# 🟢 SOLVED PRACTICE
# 1. Create a set of user IDs (include duplicates)
user_ids = {101, 102, 101, 103, 104, 102}
# 2. Print unique IDs
print("Unique IDs:", user_ids)
# 3. Add one new ID
user_ids.add(105)
# 4. Remove one ID
user_ids.remove(103)
print("Final unique IDs:", user_ids)
print("-" * 30)


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

print("Pipeline Dict:", pipeline)

# Access value
print("Source DB:", pipeline["source"])

# Add new key
pipeline["records_loaded"] = 5000
print("Added records:", pipeline)

# Update value
pipeline["status"] = "completed"
print("Updated status:", pipeline)

# Loop key + value
for key, value in pipeline.items():
    print(key, "=>", value)

# Safe access
print("Safe access missing key:", pipeline.get("execution_time"))
print("-" * 30)


# 🟢 SOLVED PRACTICE
# 1. Create dictionary for job
job = {"id": 99, "name": "daily_extract", "role": "worker"}
# 2. Add salary
job["salary"] = 75000
# 3. Update role
job["role"] = "admin"
# 4. Remove salary
job.pop("salary")
# 5. Print keys only
print("Job Keys:", job.keys())
# 6. Print values only
print("Job Values:", job.values())
print("-" * 30)

"""
# ==================================================
# 🎯 IMPORTANT INTERVIEW QUESTIONS (SOLVED)
# ==================================================

# Q1: Difference between list and tuple?
# Ans: Lists are mutable (you can add/remove items after creating them). Tuples are immutable (locked permanently once created).

# Q2: Why use set in data pipelines?
# Ans: Sets automatically filter out duplicates in milliseconds. It is the fastest way to get a list of unique Customer IDs or drop duplicate records.

# Q3: When do you use dictionary in ETL?
# Ans: When parsing JSON data from Web APIs, or when creating a configuration file where you need to look up a value by its name (like looking up "database_password").

# Q4: Difference between items(), keys(), values()?
# Ans: .keys() gives you just the names on the left. .values() gives you just the data on the right. .items() gives you both together in pairs.

# Q5: Why dictionary is important for configs?
# Ans: Because looking up a value by its specific string key (like `config["host"]`) is much safer and easier to read than trying to remember an index number (like `config[4]`).
"""
