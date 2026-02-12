"""
Python OOP – isinstance() Function (Beginner Friendly)

==================================================
TOPIC: isinstance()
==================================================

Simple Meaning:
isinstance() checks:
"Is this object made from this class?"

It returns:
True  → yes
False → no

Real-life idea:
If Dog comes from Animal class,
then Dog is also an Animal.

So check can be true for BOTH.

Why we use it:
- To safely check object type
- To run correct logic based on object
- Used in real software and data pipelines
"""

# ==================================================
# 1️⃣ SOLVED EXAMPLES
# ==================================================

# Example 1 — Basic check


class Car:
    pass


c = Car()

print(isinstance(c, Car))   # True


# ------------------------------

# Example 2 — With inheritance
class Vehicle:
    pass


class Bike(Vehicle):
    pass


b = Bike()

print(isinstance(b, Bike))      # True
print(isinstance(b, Vehicle))   # True (child is also parent)


# ------------------------------

# Example 3 — Data Engineering style
class Pipeline:
    pass


class ETLPipeline(Pipeline):
    pass


job = ETLPipeline()

print(isinstance(job, ETLPipeline))  # True
print(isinstance(job, Pipeline))     # True


# ------------------------------

# Example 4 — Another inheritance chain
class Animal:
    pass


class Cat(Animal):
    pass


cat_obj = Cat()

print(isinstance(cat_obj, Cat))     # True
print(isinstance(cat_obj, Animal))  # True


# ------------------------------

# Example 5 — Wrong type check
class Bus:
    pass


class Train:
    pass


bus_obj = Bus()

print(isinstance(bus_obj, Train))  # False


# ==================================================
# 2️⃣ UNSOLVED PRACTICE (TRY YOURSELF)
# ==================================================

# Q1:
# Create class User
# Create object u
# Check if u is instance of User


# Q2:
# Create class Job
# Create class SalesJob inherits Job
# Create object from SalesJob
# Check against BOTH classes


# Q3:
# Create class File
# Create class CSVFile inherits File
# Create object from File
# Check if it is CSVFile (should be what?)


# Q4:
# Create class Database
# Create class MySQL inherits Database
# Create MySQL object
# Check against Database


# ==================================================
# 3️⃣ INTERVIEW QUESTIONS (ENTRY LEVEL)
# ==================================================

"""
Q1: What does isinstance() do?
Answer:
It checks whether an object belongs to a specific class.

Q2: What does isinstance() return?
Answer:
True or False.

Q3: If Child inherits Parent, and we check child object with Parent — result?
Answer:
True.

Q4: Why is isinstance() useful?
Answer:
To safely run logic based on object type.

Q5: Where used in real projects?
Answer:
When handling different job types, pipelines,
file types, or data source objects.
"""

# ==================================================
# END
# ==================================================
