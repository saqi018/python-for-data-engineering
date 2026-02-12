"""
Python OOP – Property Decorators (@property)
============================================

TOPIC: PROPERTY DECORATORS

------------------------------------------------
WHAT IS @property?
------------------------------------------------
@property allows us to:
- Access a method like a variable
- Protect internal data
- Control how data is read

You READ it like a variable,
but Python RUNS a function internally.

------------------------------------------------
WHY WE USE @property
------------------------------------------------
- To protect data
- To avoid wrong values
- To write clean & professional code

------------------------------------------------
REAL-LIFE EXAMPLE
------------------------------------------------
ATM Machine:
- You see balance
- You cannot change it directly
- ATM controls everything

------------------------------------------------
DATA ENGINEERING EXAMPLE
------------------------------------------------
- Pipeline status
- Job state
- Config values
These should NOT be changed directly.
"""

# ==================================================
# 1️⃣ BASIC @property (SOLVED)
# ==================================================


class User:
    def __init__(self, age):
        self._age = age   # protected variable

    @property
    def age(self):
        return self._age


u = User(25)
print("User age:", u.age)   # looks like variable


# ==================================================
# 2️⃣ WHY @property IS IMPORTANT
# ==================================================

"""
Without @property:
- Anyone can put wrong data
- No control
- Unsafe

With @property:
- Data is protected
- Logic is controlled
"""

# ==================================================
# 3️⃣ ACCOUNT EXAMPLE (SOLVED)
# ==================================================


class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance


acc = Account(1000)
print("Account Balance:", acc.balance)


# ==================================================
# 4️⃣ DATA ENGINEERING REAL-WORLD EXAMPLE (SOLVED)
# ==================================================

class Pipeline:
    def __init__(self):
        self._status = "Stopped"

    @property
    def status(self):
        return self._status


p = Pipeline()
print("Pipeline Status:", p.status)


# ==================================================
# 5️⃣ PROPERTY WITH VALIDATION (READ ONLY)
# ==================================================

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary


e = Employee(50000)
print("Employee Salary:", e.salary)

# ❌ NOT ALLOWED:
# e.salary = 60000


# ==================================================
# 6️⃣ UNSOLVED PRACTICE (TRY YOURSELF)
# ==================================================

# TODO 1:
# Create class Student
# Protected variable: _marks
# Property: marks
# Print marks

# TODO 2 (Data Engineering):
# Create class Job
# Protected variable: _job_status = "Stopped"
# Property: job_status
# Print job status

# TODO 3:
# Create class Product
# Protected variable: _price
# Property: price


# ==================================================
# 7️⃣ COMMON MISTAKES
# ==================================================

"""
❌ Accessing protected variable directly:
print(u._age)

❌ Changing protected data directly:
u._age = -10

✅ Correct way:
Use @property
"""

# ==================================================
# 8️⃣ INTERVIEW QUESTIONS (ENTRY-LEVEL)
# ==================================================

"""
Q1: What is @property in Python?
Answer:
It allows a method to be accessed like a variable.

Q2: Why do we use @property?
Answer:
To protect data and control access.

Q3: Is @property a variable?
Answer:
No, it is a method.

Q4: Where is @property used in Data Engineering?
Answer:
Pipelines, job status, configs, metadata.

Q5: Can we modify data using @property?
Answer:
No, not without a setter.
"""
