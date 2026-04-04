"""
Python Basic Projects
=========================================

Covers:
- input
- loops
- lists
- functions
- conditions
- error handling

These are small real-life style beginner projects.
"""

# ======================================
# PROJECT 1 — Student Marks Manager
# ======================================

print("\n=== Student Marks Manager ===")

marks = []

for i in range(5):
    while True:
        try:
            m = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)
            break
        except:
            print("Enter a valid number")


def calculate_average(data):
    return sum(data) / len(data)


avg = calculate_average(marks)

print("Marks:", marks)
print("Average:", avg)

if avg >= 50:
    print("Status: PASS")
else:
    print("Status: FAIL")


# =====================================
# PROJECT 2 — Daily Expense Tracker
# =====================================

print("\n=== Daily Expense Tracker ===")

expenses = []

for i in range(5):
    while True:
        try:
            e = int(input(f"Enter expense {i+1}: "))
            expenses.append(e)
            break
        except:
            print("Enter valid number")


def expense_stats(data):
    return sum(data), min(data), max(data)


total, low, high = expense_stats(expenses)

print("Total:", total)
print("Minimum:", low)
print("Maximum:", high)


# =========================================
# PROJECT 3 — Login System (3 Attempts)
# ========================================

print("\n=== Login System ===")

correct_user = "admin"
correct_pass = "1234"

for i in range(3):
    user = input("Username: ")
    pwd = input("Password: ")

    if user == correct_user and pwd == correct_pass:
        print("Login Success")
        break
    else:
        print("Wrong credentials")

else:
    print("Account locked")


# ===================================
# PROJECT 4 — Word Counter
# ===================================

print("\n=== Word Counter ===")

sentence = input("Enter a sentence (min 3 words): ")

words = sentence.split()

print("Word count:", len(words))

if len(words) >= 3:
    print("Valid sentence")
else:
    print("Too short")
