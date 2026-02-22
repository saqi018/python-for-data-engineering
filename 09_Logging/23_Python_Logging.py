"""
================================================
PYTHON LOGGING BASICS — GITHUB READY FILE
Level: Beginner → Data Engineer
================================================

WHAT IS LOGGING?
----------------
Logging means saving messages about what your program is doing.

Real Data Engineering Example:
API → Fetch data → Save to DB → Complete

Logging helps track:
- When pipeline starts
- If error happens
- If pipeline completes

Instead of print(), companies use logging.

================================================
TOPIC 1: BASIC LOGGING SETUP
================================================

Explanation (Kid Level):
Logging is like CCTV camera for your program.
It records everything.
"""

# Solved Quiz 1:

import logging

logging.basicConfig(filename="08/Python/APIs/pipeline.log", level=logging.INFO)

logging.info("Pipeline started")


# Solved Quiz 2:

logging.warning("Memory usage high")


# Solved Quiz 3:

logging.error("Database connection failed")

"""
================================================
TOPIC 2: LOG LEVELS
================================================

Levels:
DEBUG → developer info
INFO → normal operation
WARNING → something suspicious
ERROR → something failed
CRITICAL → system crash
"""
# Solved Quiz 4:

logging.info("API fetch successful")


# Solved Quiz 5:

logging.error("API failed")


# Solved Quiz 6:

logging.warning("Slow response from API")

"""
================================================
TOPIC 3: REAL DATA PIPELINE EXAMPLE
================================================

Solved Quiz 7:
"""
try:
    logging.info("Pipeline started")

    data = [1, 2, 3]
    logging.info("Data fetched successfully")

    logging.info("Data saved to database")

    logging.info("Pipeline completed")

except Exception as e:
    logging.error(f"Pipeline failed: {e}")

"""
================================================
UNSOLVED QUIZ (YOUR PRACTICE)
================================================


 Question 1:
Log message:
"ETL started"

 Question 2:
Log warning:
"Disk almost full"

Question 3:
Log error:
"Insert failed"

Write your answers below:


# write your answers here



================================================
INTERVIEW QUESTIONS (VERY IMPORTANT)
================================================

Q1: What is logging?
Answer:
Logging records program events for monitoring and debugging.

Q2: Why use logging instead of print?
Answer:
Logging saves to files and works in production.

Q3: What is INFO level?
Answer:
Normal operation message.

Q4: What is ERROR level?
Answer:
Shows failure.

Q5: Where logging used in Data Engineering?
Answer:
ETL pipelines, Airflow, APIs, database pipelines.

================================================
END OF FILE
================================================
"""
