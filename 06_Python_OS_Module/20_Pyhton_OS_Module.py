"""
OS MODULE — Data Engineering Basics

What:
OS module is used to work with files and folders from Python.

Why:
Data Engineers use it to:
- check files before reading
- create folders for pipelines
- list incoming data files
- stop job if file missing
- organize pipeline folders
"""

import os

# ---------- FIXED BASE FOLDER PATH ----------

BASE = "06_Python_OS_Module"


# ---------- SOLVED EXAMPLES ----------

# 1️⃣ Create base folder if not exists
if not os.path.exists(BASE):
    os.mkdir(BASE)


# 2️⃣ Create subfolder: data
data_path = os.path.join(BASE, "data")

if not os.path.exists(data_path):
    os.mkdir(data_path)


# 3️⃣ Check file existence (pipeline safety check)
input_file = os.path.join(BASE, "input.csv")

if os.path.exists(input_file):
    print("Input file found — pipeline can run")
else:
    print("Input file missing — stop pipeline")


# 4️⃣ Create multiple batch folders
for i in range(1, 4):
    folder = os.path.join(BASE, f"batch_{i}")
    if not os.path.exists(folder):
        os.mkdir(folder)


# 5️⃣ List files inside BASE folder
print("\nFiles & folders inside BASE:")
for name in os.listdir(BASE):
    print(name)


# 6️⃣ Create a log file inside BASE
log_file = os.path.join(BASE, "pipeline.log")

with open(log_file, "w") as f:
    f.write("Pipeline started\n")


# 7️⃣ Rename a file (if exists)
old_name = os.path.join(BASE, "old.txt")
new_name = os.path.join(BASE, "new.txt")

if os.path.exists(old_name):
    os.rename(old_name, new_name)


# ---------- PRACTICE TASKS (UNSOLVED) ----------

"""
TASK 1
Create folder inside BASE called:
processed
"""

"""
TASK 2
Check if file exists:
BASE/sales.csv
Print:
found / missing
"""

"""
TASK 3
Create folders:
day1 day2 day3
inside BASE
(using loop)
"""

"""
TASK 4
List only folders inside BASE
(skip files)
"""

"""
TASK 5
Create file:
BASE/report.txt
and write:
job finished
"""


# ---------- INTERVIEW QUESTIONS ----------

"""
Q1: Why os.path.exists() is important in data pipelines?

Q2: Difference between os.mkdir and os.makedirs?

Q3: Why use os.path.join instead of manual path writing?

Q4: What happens if os.mkdir folder already exists?

Q5: How do you list all files in a directory?
"""
