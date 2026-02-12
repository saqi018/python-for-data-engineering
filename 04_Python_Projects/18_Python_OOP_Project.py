"""
Python OOP Mini Projects – Beginner Friendly
============================================

Covers:
- Classes
- Attributes
- Methods
- Encapsulation thinking
- Real-world modeling

Projects simulate real systems like Data Engineering objects.
"""

# =====================================================
# PROJECT 1 — Employee Manager
# =====================================================


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def increase_salary(self, amount):
        self.salary += amount
        print("Salary increased")


e1 = Employee("Saqib", 50000)

e1.show_info()
e1.increase_salary(5000)
e1.show_info()


# =====================================================
# PROJECT 2 — Database Table Simulator
# =====================================================

class Table:

    def __init__(self, table_name):
        self.table_name = table_name
        self.rows = 0

    def insert_row(self):
        self.rows += 1
        print("Row inserted")

    def delete_row(self):
        if self.rows > 0:
            self.rows -= 1
            print("Row deleted")
        else:
            print("No rows to delete")

    def show_rows(self):
        print("Table:", self.table_name)
        print("Rows:", self.rows)


t = Table("Users")

t.insert_row()
t.insert_row()
t.delete_row()
t.show_rows()


# =====================================================
# PROJECT 3 — Data Pipeline Job Tracker
# =====================================================

class PipelineJob:

    def __init__(self, job_name):
        self.job_name = job_name
        self.status = "Stopped"

    def start(self):
        self.status = "Running"
        print(self.job_name, "started")

    def stop(self):
        self.status = "Stopped"
        print(self.job_name, "stopped")

    def show_status(self):
        print("Job:", self.job_name)
        print("Status:", self.status)


job = PipelineJob("Sales_ETL")

job.show_status()
job.start()
job.show_status()
job.stop()


# =====================================================
# PROJECT 4 — Bank Account (Encapsulation Style)
# =====================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)


acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.show_balance()
