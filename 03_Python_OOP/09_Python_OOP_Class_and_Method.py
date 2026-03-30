"""
Python OOP – Class and Method (Beginner Friendly)

Simple Definitions:
- Class: A design / template.
- Object: A real thing made from the class.
- Method: A function inside a class (an action).

Example:
- Car has data (brand)
- Car can do action (start)
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES
# ==================================================

# Example 1: Simple Car class with method


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting")


c1 = Car("Toyota")
c2 = Car("Honda")

c1.start()
c2.start()


# Example 2: Data Engineering – Pipeline
class Pipeline:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Pipeline {self.name} is running")


p1 = Pipeline("Daily Sales ETL")
p2 = Pipeline("User Events ETL")

p1.run()
p2.run()


# Example 3: File processing example
class DataFile:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        print(f"Loading file: {self.filename}")


f1 = DataFile("sales.csv")
f2 = DataFile("users.csv")

f1.load()
f2.load()


# ==================================================
# 2️⃣ UNSOLVED PRACTICE (DO IT YOURSELF)
# ==================================================

# TODO 1:
# Create a class Employee
# Attribute: name
# Method: work() → print "Employee is working"
# Create one object and call method


# TODO 2:
# Create a class Database
# Attribute: db_name
# Method: connect() → print "Connected to database"
# Create one object and call method


# TODO 3 (thinking):
# Why do we call method using object?
# Example: car.start()
# Write answer in comment


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ENTRY LEVEL)
# ==================================================

"""
Q1: What is a class?
Answer:
A class is a blueprint or template used to create objects.

Q2: What is a method?
Answer:
A method is a function inside a class.

Q3: How do we call a method?
Answer:
Using object name and dot (object.method()).

Q4: Why do methods use self?
Answer:
To access data of the current object.

Q5: Difference between function and method?
Answer:
Function is outside a class.
Method is inside a class.
"""
