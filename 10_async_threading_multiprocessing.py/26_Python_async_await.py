"""
================================================
ASYNC PYTHON (async/await)
================================================

WHAT IS ASYNC?
Asynchronous programming allows tasks to run without blocking.
Best for high-performance API calls and network operations.

================================================
BASIC EXAMPLE
================================================
"""
import asyncio


async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")


async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )

asyncio.run(main())

"""
================================================
REAL DATA ENGINEERING EXAMPLE (ASYNC API FETCH)
================================================
"""


async def fetch_api(api):
    print(f"Fetching {api}")
    await asyncio.sleep(2)
    print(f"{api} done")


async def main_pipeline():
    apis = ["users", "orders", "products"]
    await asyncio.gather(*(fetch_api(api) for api in apis))

asyncio.run(main_pipeline())
