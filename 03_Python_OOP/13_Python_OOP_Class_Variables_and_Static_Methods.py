"""
Python OOP – Class Variables & Static Methods (Beginner Friendly)

==================================================
TOPIC CLASS VARIABLES, STATIC METHODS
==================================================

This file is written for:
- Absolute beginners
- Data Engineering learners
- Practical, real-world understanding

--------------------------------------------------
BASIC IDEA (VERY SIMPLE):

Class Variable:
- Belongs to the CLASS
- Shared by ALL objects
- Used for common data (count, status, config)

Static Method:
- A function inside a class
- Does NOT use self
- Does NOT use object data
- Used for utility / helper logic
--------------------------------------------------
"""

# ==================================================
# 🔵 PART 1: CLASS VARIABLES
# ==================================================

"""
CLASS VARIABLE = shared memory

Real-life example:
- Total students in a school
- Company name for all employees
- Pipeline status shared by all runs
"""

# --------------------------------------------------
# 1️⃣ SOLVED EXAMPLE: Student Counter
# --------------------------------------------------


class Student:
    total_students = 0   # class variable

    def __init__(self, name):
        self.name = name
        Student.total_students += 1


s1 = Student("Ali")
s2 = Student("Ahmed")
s3 = Student("Sara")

print("Total students:", Student.total_students)


# --------------------------------------------------
# 2️⃣ SOLVED EXAMPLE: Company Name (Shared)
# --------------------------------------------------

class Employee:
    company_name = "Amazon"   # class variable

    def show_company(self):
        print("Company:", Employee.company_name)


e1 = Employee()
e2 = Employee()

e1.show_company()
e2.show_company()


# --------------------------------------------------
# 3️⃣ DATA ENGINEERING EXAMPLE: Pipeline Status
# --------------------------------------------------

class Pipeline:
    status = "Stopped"   # shared status

    def show_status(self):
        print("Pipeline status:", Pipeline.status)


p1 = Pipeline()
p2 = Pipeline()

p1.show_status()
p2.show_status()


# --------------------------------------------------
# 4️⃣ UNSOLVED PRACTICE (TRY YOURSELF)
# --------------------------------------------------

"""
TODO 1:
Create class Job
Class variable: job_count
Increase count when object is created

TODO 2:
Create class Company
Class variable: country = "USA"
Print it using class name
"""

# ==================================================
# 🟢 PART 2: STATIC METHODS
# ==================================================

"""
STATIC METHOD = helper function

Used when:
- No object data needed
- No class data needed
- Just logic / calculation / validation

Real-life use:
- Email validation
- File type check
- Math calculation
- String cleaning
"""

# --------------------------------------------------
# 5️⃣ SOLVED EXAMPLE: Math Utility
# --------------------------------------------------


class MathUtils:

    @staticmethod
    def add(a, b):
        print("Sum:", a + b)


MathUtils.add(4, 6)


# --------------------------------------------------
# 6️⃣ SOLVED EXAMPLE: Age Validation
# --------------------------------------------------

class UserUtils:

    @staticmethod
    def check_age(age):
        if age >= 18:
            print("Allowed")
        else:
            print("Not Allowed")


UserUtils.check_age(20)
UserUtils.check_age(15)


# --------------------------------------------------
# 7️⃣ DATA ENGINEERING EXAMPLE: File Checker
# --------------------------------------------------

class FileUtils:

    @staticmethod
    def is_csv(filename):
        if filename.endswith(".csv"):
            print("CSV file detected")
        else:
            print("Not a CSV file")


FileUtils.is_csv("data.csv")
FileUtils.is_csv("data.json")


# --------------------------------------------------
# 8️⃣ SOLVED EXAMPLE: Email Validation (FIXED LOGIC)
# --------------------------------------------------

class EmailUtils:

    @staticmethod
    def is_valid(email):
        if "@" in email:
            print("Email is valid")
        else:
            print("Email is not valid")


EmailUtils.is_valid("@saqib@email.com")
EmailUtils.is_valid("saqibemail.com")


# --------------------------------------------------
# 9️⃣ SOLVED EXAMPLE: String Cleaning
# --------------------------------------------------

class PipelineUtils:

    @staticmethod
    def clean_name(name):
        print(name.lower())


PipelineUtils.clean_name("Sales_Pipeline")


# --------------------------------------------------
# 🔟 UNSOLVED PRACTICE (TRY YOURSELF)
# --------------------------------------------------

"""
TODO 1:
Create static method subtract(a, b)

TODO 2:
Create static method is_success(status)
Print "Job Passed" if status == "success"
Else print "Job Failed"

TODO 3 (Data Engineering):
Create static method clean_column_name(name)
Convert to lowercase
Replace spaces with underscore
"""

# ==================================================
# 🎯 INTERVIEW QUESTIONS (IMPORTANT)
# ==================================================

"""
Q1: What is a class variable?
Answer:
A variable shared by all objects of a class.

Q2: Why use class variables?
Answer:
To store common data like count, config, status.

Q3: What is a static method?
Answer:
A method that does not use self or class data.

Q4: When should we use static methods?
Answer:
For utility logic like validation, calculation, formatting.

Q5: Do static methods need objects?
Answer:
No, they are called using class name.
"""
