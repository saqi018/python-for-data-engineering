"""
Python OOP – Polymorphism (Beginner Friendly)

==================================================
TOPIC: POLYMORPHISM
==================================================

Polymorphism means:
- Same method name
- Different behavior
- Different objects respond in their own way

Simple meaning:
One action → many forms

Real-life example:
Start button
- Car starts
- Bike starts
- Bus starts
Same button, different result

Data Engineering example:
run()
- Sales pipeline runs ETL
- User pipeline runs ETL
Same method name, different job
"""

# ==================================================
# 1️⃣ BASIC POLYMORPHISM (SOLVED)
# ==================================================

class Car:
    def start(self):
        print("Car is starting")


class Bike:
    def start(self):
        print("Bike is starting")


vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()

"""
Explanation:
- Car and Bike both have start()
- Python does NOT care about class name
- It only cares: does object have start() ?
"""


# ==================================================
# 2️⃣ ANIMAL EXAMPLE (VERY EASY)
# ==================================================

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for a in animals:
    a.sound()

"""
Same method name: sound()
Different output
This is polymorphism
"""


# ==================================================
# 3️⃣ DATA ENGINEERING REAL-WORLD EXAMPLE (SOLVED)
# ==================================================

class SalesPipeline:
    def run(self):
        print("Running sales ETL pipeline")


class UserPipeline:
    def run(self):
        print("Running user ETL pipeline")


pipelines = [SalesPipeline(), UserPipeline()]

for p in pipelines:
    p.run()

"""
Why this is important in Data Engineering:
- Scheduler calls run()
- It doesn't care which pipeline
- Every pipeline runs its own logic
"""


# ==================================================
# 4️⃣ TRANSPORT EXAMPLE (CLEAR)
# ==================================================

class Bus:
    def move(self):
        print("Bus is moving")


class Train:
    def move(self):
        print("Train is moving")


transport = [Bus(), Train()]

for t in transport:
    t.move()


# ==================================================
# 5️⃣ POLYMORPHISM WITHOUT INHERITANCE
# ==================================================

"""
IMPORTANT:
Polymorphism does NOT require inheritance

Rule:
If method name is same → polymorphism works
"""

class ETLJob:
    def run(self):
        print("ETL job running")


class ReportJob:
    def run(self):
        print("Report job running")


jobs = [ETLJob(), ReportJob()]

for j in jobs:
    j.run()


# ==================================================
# 6️⃣ WHY POLYMORPHISM IS POWERFUL
# ==================================================

"""
Without polymorphism:
- Too many if/else
- Messy code

With polymorphism:
- Clean loops
- Easy extension
- Professional code
"""


# ==================================================
# 7️⃣ UNSOLVED PRACTICE (TRY YOURSELF)
# ==================================================

# TODO 1:
# Create class EmailNotification
# Method: send()
# Print: "Sending email notification"

# Create class SMSNotification
# Method: send()
# Print: "Sending SMS notification"

# Put objects in a list and call send() using loop


# TODO 2 (Data Engineering):
# Create class IngestJob
# Method: execute()
# Print: "Ingesting data"

# Create class TransformJob
# Method: execute()
# Print: "Transforming data"

# Call execute() using polymorphism


# ==================================================
# 8️⃣ INTERVIEW QUESTIONS (IMPORTANT ONLY)
# ==================================================

"""
Q1: What is Polymorphism?
Answer:
Polymorphism means same method name with different behavior.

Q2: Does polymorphism need inheritance?
Answer:
No. Only method name must be same.

Q3: Why is polymorphism useful?
Answer:
It removes if/else, makes code clean and scalable.

Q4: How is polymorphism used in Data Engineering?
Answer:
In pipelines, jobs, schedulers, and ETL execution.

Q5: What does Python check in polymorphism?
Answer:
Python checks method existence, not class type.
"""
