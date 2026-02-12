"""
Python OOP – Encapsulation (Beginner Friendly)

==================================================
TOPIC: ENCAPSULATION
==================================================

Encapsulation means:
- Protecting important data inside a class
- Not allowing direct access to sensitive variables
- Accessing or changing data only using methods

Why we use Encapsulation:
- To protect data from wrong changes
- To control how data is accessed
- To write safe, clean, professional code

Real-life example:
ATM Machine
- You cannot touch the money directly
- You use buttons (methods) to withdraw

Data Engineering example:
- Pipeline status
- Job execution state
- Error counts
These should not be changed directly.
"""

# ==================================================
# 1️⃣ BASIC ENCAPSULATION (SOLVED)
# ==================================================


class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password   # private variable

    def show_name(self):
        print("User name:", self.name)

    def check_password(self):
        print("Password is protected and cannot be shown")


u = User("Ali", "1234")
u.show_name()
u.check_password()

# ❌ This is NOT allowed:
# print(u.__password)


# ==================================================
# 2️⃣ MODIFY PRIVATE DATA USING METHODS (SOLVED)
# ==================================================

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Current Balance:", self.__balance)

    def add_money(self, amount):
        self.__balance += amount
        print("Money added successfully")


acc = Account(1000)
acc.show_balance()
acc.add_money(500)
acc.show_balance()


# ==================================================
# 3️⃣ DATA ENGINEERING REAL-WORLD EXAMPLE (SOLVED)
# ==================================================

class Pipeline:
    def __init__(self):
        self.__status = "Stopped"

    def start_pipeline(self):
        self.__status = "Running"

    def stop_pipeline(self):
        self.__status = "Stopped"

    def get_status(self):
        print("Pipeline Status:", self.__status)


p = Pipeline()
p.get_status()
p.start_pipeline()
p.get_status()
p.stop_pipeline()
p.get_status()


# ==================================================
# 4️⃣ WHY DIRECT ACCESS IS BAD
# ==================================================

"""
We do NOT allow:
p.__status = "Running"

Because:
- It breaks control
- It can cause bugs
- It is unsafe in real systems
"""


# ==================================================
# 5️⃣ UNSOLVED PRACTICE (TRY YOURSELF)
# ==================================================

# TODO 1:
# Create a class Employee
# Private variable: __salary
# Method: show_salary()
# Method: increase_salary(amount)


# TODO 2 (Data Engineering):
# Create class Job
# Private variable: __job_status ("Stopped")
# Method: start_job()
# Method: get_status()


# ==================================================
# 6️⃣ INTERVIEW QUESTIONS (IMPORTANT ONLY)
# ==================================================

"""
Q1: What is Encapsulation?
Answer:
Encapsulation is the process of protecting data by restricting
direct access and allowing access through methods.

Q2: How do we make a variable private in Python?
Answer:
By using double underscore ( __variable ).

Q3: Why is Encapsulation important?
Answer:
It protects data, improves security, and avoids unwanted changes.

Q4: Can we access private variables directly?
Answer:
No, we should use methods.

Q5: Where is Encapsulation used in Data Engineering?
Answer:
In pipelines, job status, logs, credentials, and configuration handling.
"""
