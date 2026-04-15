# ...existing code...
"""
Python File Handling – Full Practice (Beginner Friendly)

Topics Covered:
- Write file
- Read file
- Append file
- Read line by line
- Write list data
- Safe file handling
- Folder-based file paths (important for Data Engineers)

"""

print("=== FILE HANDLING PRACTICE ===")


# =====================================================
# 1️⃣ WRITE FILE
# =====================================================

with open("19_Python_File_Handling/demo1.txt", "w") as f:
    f.write("Data Engineering is fun")

print("demo1.txt created")


# =====================================================
# 2️⃣ READ FILE
# =====================================================

with open("19_Python_File_Handling/demo1.txt", "r") as f:
    data = f.read()
    print("demo1 content:", data)


# =====================================================
# 3️⃣ WRITE MULTIPLE LINES
# =====================================================

with open("19_Python_File_Handling/demo2.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3")

print("demo2.txt created")


# =====================================================
# 4️⃣ READ LINE BY LINE
# =====================================================

with open("19_Python_File_Handling/demo2.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())


# =====================================================
# 5️⃣ WRITE NUMBERS LIST
# =====================================================

numbers = [10, 20, 30, 40]

with open("19_Python_File_Handling/numbers.txt", "w") as f:
    for n in numbers:
        f.write(str(n) + "\n")

print("numbers.txt created")


# =====================================================
# 6️⃣ APPEND MODE
# =====================================================

with open("19_Python_File_Handling/log.txt", "a") as f:
    f.write("Job started\n")
    f.write("Job finished\n")

print("log.txt updated")


# =====================================================
# 7️⃣ SAFE READ (TRY / EXCEPT)
# =====================================================

try:
    with open("19_Python_File_Handling/log.txt", "r") as f:
        print("LOG FILE:")
        print(f.read())
except FileNotFoundError:
    print("log.txt not found")


# =====================================================
# 8️⃣ DATA ENGINEERING STYLE FILE
# =====================================================

pipeline_status = [
    "extract started",
    "transform running",
    "load completed"
]

with open("19_Python_File_Handling/pipeline_status.txt", "w") as f:
    for step in pipeline_status:
        f.write(step + "\n")

print("pipeline_status.txt created")


print("=== DONE ===") 