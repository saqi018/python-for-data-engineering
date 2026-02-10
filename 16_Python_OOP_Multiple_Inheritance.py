"""
Python OOP — Multiple Inheritance (Beginner Friendly)

==================================================
TOPIC: MULTIPLE INHERITANCE
==================================================

Multiple Inheritance means:
- One child class inherits from MORE THAN ONE parent class.

Simple meaning:
Child = gets features from many parents.

Real-life example:
SmartPhone:
- Can call (Phone feature)
- Can take photo (Camera feature)

Data Engineering example:
ETL Job:
- Can extract data
- Can log status
Both features come from different parent classes.
"""

# ==================================================
# 1️⃣ BASIC EXAMPLE (SOLVED)
# ==================================================


class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def call(self):
        print("Calling...")


class SmartPhone(Camera, Phone):
    pass


s = SmartPhone()
s.take_photo()
s.call()


# ==================================================
# 2️⃣ DATA ENGINEERING EXAMPLE (SOLVED)
# ==================================================

class Extract:
    def extract_data(self):
        print("Extracting data from source")


class Load:
    def load_data(self):
        print("Loading data to warehouse")


class ETLJob(Extract, Load):
    pass


job = ETLJob()
job.extract_data()
job.load_data()


# ==================================================
# 3️⃣ ANOTHER SIMPLE EXAMPLE (SOLVED)
# ==================================================

class Fly:
    def fly(self):
        print("Flying")


class Swim:
    def swim(self):
        print("Swimming")


class Duck(Fly, Swim):
    pass


d = Duck()
d.fly()
d.swim()


# ==================================================
# 4️⃣ isinstance CHECK (IMPORTANT)
# ==================================================

print(isinstance(s, SmartPhone))  # True
print(isinstance(s, Camera))      # True
print(isinstance(s, Phone))       # True


# ==================================================
# 5️⃣ WHY USE MULTIPLE INHERITANCE
# ==================================================

"""
We use it when:
- We want to reuse features from many classes
- We want to combine behaviors
- Useful in real systems (pipelines + logging + validation)

But:
Too much multiple inheritance can make code confusing.
Use only when needed.
"""


# ==================================================
# 6️⃣ UNSOLVED PRACTICE (TRY YOURSELF)
# ==================================================

# TODO 1:
# Create class Writer → write()
# Create class Saver → save()
# Create class Report → inherit both
# Create object and call both methods


# TODO 2:
# Create class Validator → validate()
# Create class Logger → log()
# Create class DataTask → inherit both
# Call both methods


# TODO 3 (with isinstance):
# After creating object, check:
# isinstance(obj, Parent1)
# isinstance(obj, Parent2)


# ==================================================
# 7️⃣ INTERVIEW QUESTIONS (ENTRY LEVEL)
# ==================================================

"""
Q1: What is Multiple Inheritance?
Answer:
When one class inherits from more than one parent class.

Q2: How do we write multiple inheritance in Python?
Answer:
class Child(Parent1, Parent2):

Q3: Does child get methods from both parents?
Answer:
Yes.

Q4: Where is it useful?
Answer:
When we need to combine behaviors like logging + processing.

Q5: What is a risk of multiple inheritance?
Answer:
Code can become complex if overused.
"""
