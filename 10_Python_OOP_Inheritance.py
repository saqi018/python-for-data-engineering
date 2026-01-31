"""
Python OOP – Inheritance (Beginner Friendly)

==================================================
TOPIC: INHERITANCE
==================================================

Inheritance means:
One class (child) can use the features of another class (parent).

Why we use inheritance:
- To reuse code
- To avoid writing the same logic again
- To keep code clean and professional
- Very useful in real Data Engineering projects

Simple idea:
Parent class = base / common features
Child class  = special version of parent

Real-life example:
- Vehicle (parent)
- Car, Bike (child)

Data Engineering example:
- Pipeline (parent)
- ETLPipeline, SalesPipeline (child)
"""

# ==================================================
# 1️⃣ BASIC INHERITANCE (SOLVED)
# ==================================================


class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog = Dog()
dog.eat()   # inherited from Animal


# ==================================================
# 2️⃣ INHERITANCE WITH CHILD METHOD (SOLVED)
# ==================================================

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


bike = Bike()
bike.move()   # parent method
bike.ride()   # child method


# ==================================================
# 3️⃣ DATA ENGINEERING REAL-WORLD EXAMPLE (SOLVED)
# ==================================================

class Pipeline:
    def start(self):
        print("Pipeline started")


class ETLPipeline(Pipeline):
    def run_etl(self):
        print("Running ETL job")


etl = ETLPipeline()
etl.start()     # inherited
etl.run_etl()   # own method


# ==================================================
# 4️⃣ IMPORTANT RULE (VERY IMPORTANT)
# ==================================================

"""
RULE:
Child object can use:
- Parent methods
- Child methods

Parent object can use:
- ONLY parent methods
"""

# Example (WRONG – will cause error):
# p = Pipeline()
# p.run_etl()   ❌ Pipeline does not know run_etl()


# ==================================================
# 5️⃣ UNSOLVED PRACTICE (DO YOURSELF)
# ==================================================

# TODO 1:
# Create a parent class Employee
# Method: work() -> prints "Employee is working"

# Create a child class Developer
# Method: code() -> prints "Developer is coding"

# Create object of Developer
# Call both methods


# TODO 2 (Data Engineering):
# Parent class: Job
# Method: start_job()

# Child class: DataJob
# Method: process_data()

# Create DataJob object and call both methods


# ==================================================
# 6️⃣ INTERVIEW QUESTIONS (ENTRY LEVEL)
# ==================================================

"""
Q1: What is inheritance in Python?
Answer:
Inheritance allows a child class to reuse the methods and attributes
of a parent class.

Q2: Why is inheritance useful?
Answer:
It reduces code duplication and makes code clean and reusable.

Q3: Can a child class use parent methods without rewriting them?
Answer:
Yes.

Q4: Can a parent object use child methods?
Answer:
No.

Q5: Where is inheritance used in Data Engineering?
Answer:
In pipelines, jobs, connectors, ETL workflows, and reusable components.
"""
