"""

================================================
MULTIPROCESSING IN PYTHON 
================================================

WHAT IS MULTIPROCESSING?
Running multiple processes using multiple CPU cores.
Best for CPU-heavy tasks (data processing, calculations).


================================================
BASIC EXAMPLE
================================================
"""

import multiprocessing
import time


def task(name):
    print(f"Process {name} started")
    time.sleep(2)
    print(f"Process {name} finished")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task, args=("A",))
    p2 = multiprocessing.Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed")

"""
================================================
REAL DATA ENGINEERING EXAMPLE (DATA PROCESSING)
================================================
"""


def square(number):
    return number * number


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)

    print("Squared numbers:", results)
