"""

================================================
MULTITHREADING IN PYTHON 
================================================

WHAT IS MULTITHREADING?
Running multiple tasks at the same time inside one process.
Best for IO tasks (API calls, file reading, downloads).

================================================
BASIC EXAMPLE
================================================
"""
import threading
import time


def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")


t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")

"""
================================================
REAL DATA ENGINEERING EXAMPLE (API FETCH)
================================================

"""


def fetch_api(api):
    print(f"Fetching {api}")
    time.sleep(2)
    print(f"{api} done")


apis = ["users", "orders", "products"]

threads = []

for api in apis:
    t = threading.Thread(target=fetch_api, args=(api,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All APIs fetched")
