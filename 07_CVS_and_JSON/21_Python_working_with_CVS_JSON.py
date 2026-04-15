"""
========================================
WORKING WITH CSV & JSON — PYTHON
Data Engineering Beginner Guide
========================================
"""

# =========================================================
# ===================== CSV SECTION =======================
# =========================================================

"""
WHAT IS CSV?

CSV = Comma Separated Values
It stores table data like Excel:
name,age,city
Ali,25,Lahore

WHY CSV IS USED IN DATA ENGINEERING?

- Raw data often comes as CSV
- Easy to export/import
- Used in ETL pipelines
- Used between systems
"""


# -----------------------------
# CSV — WRITE DATA (Solved)
# -----------------------------

import json
import csv
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "salary"])
    writer.writerow(["ali", 50000])
    writer.writerow(["sara", 70000])
    writer.writerow(["john", 60000])

print("CSV file created")


# -----------------------------
# CSV — READ DATA (Solved)
# -----------------------------

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# -----------------------------
# CSV — DICT READER (Solved)
# Best for Data Engineering
# -----------------------------

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["salary"])


# -----------------------------
# CSV — FILTER DATA (Solved)
# -----------------------------

print("\nHigh salary > 60000")

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["salary"]) > 60000:
            print(row["name"])


# -----------------------------
# CSV — SUM COLUMN (Solved)
# -----------------------------

total = 0

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += int(row["salary"])

print("Total salary =", total)


# =========================================================
# CSV — UNSOLVED QUIZ
# =========================================================

"""
QUIZ 1:
Create products.csv with:
product,price
laptop,800
mouse,20
keyboard,50
"""

"""
QUIZ 2:
Read products.csv
Print only items with price > 100
"""

"""
QUIZ 3:
Calculate total price from products.csv
"""

"""
QUIZ 4:
Convert price column to int and store into list
"""

"""
QUIZ 5:
Append one more product using append mode
"""


# =========================================================
# CSV — INTERVIEW QUESTIONS
# =========================================================

"""
1. What is CSV format?
2. Difference between reader and DictReader?
3. Why newline="" used while writing CSV?
4. When to use DictWriter?
5. Why convert values to int while reading?
6. CSV vs Database — when to use which?
"""


# =========================================================
# ===================== JSON SECTION ======================
# =========================================================

"""
WHAT IS JSON?

JSON = JavaScript Object Notation
It stores data like Python dict:

{
  "name": "Ali",
  "age": 25
}

WHY JSON USED IN DATA ENGINEERING?

- API responses come in JSON
- Web data is JSON
- Config files use JSON
- Pipeline data exchange format
"""


# -----------------------------
# JSON — WRITE (Solved)
# -----------------------------

data = {
    "name": "saqib",
    "skills": ["python", "sql", "etl"]
}

with open("user.json", "w") as file:
    json.dump(data, file, indent=2)

print("JSON file written")


# -----------------------------
# JSON — READ (Solved)
# -----------------------------

with open("user.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["skills"])


# -----------------------------
# JSON — LIST OF RECORDS (Solved)
# -----------------------------

users = [
    {"name": "ali", "age": 25},
    {"name": "sara", "age": 30}
]

with open("users.json", "w") as file:
    json.dump(users, file, indent=2)


# -----------------------------
# JSON — READ LIST (Solved)
# -----------------------------

with open("users.json", "r") as file:
    records = json.load(file)

for row in records:
    print(row["name"], row["age"])


# -----------------------------
# CSV → JSON CONVERSION (Solved)
# Real Data Engineering Task
# -----------------------------

result = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        result.append(row)

with open("employees.json", "w") as file:
    json.dump(result, file, indent=2)

print("CSV converted to JSON")


# =========================================================
# JSON — UNSOLVED QUIZ
# =========================================================

"""
QUIZ 1:
Create JSON with product info (name, price, stock)
"""

"""
QUIZ 2:
Read JSON and print only price
"""

"""
QUIZ 3:
Store list of 3 users in JSON
"""

"""
QUIZ 4:
Read users JSON and print users age > 26
"""

"""
QUIZ 5:
Convert JSON → CSV
"""


# =========================================================
# JSON — INTERVIEW QUESTIONS
# =========================================================

"""
1. What is JSON format?
2. Difference between dump and load?
3. What is indent in json.dump?
4. Why JSON popular for APIs?
5. JSON vs CSV difference?
6. When JSON better than CSV?
"""


print("\nLearning file finished")
