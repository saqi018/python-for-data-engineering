"""
Pandas Extract & Load (CSV and JSON) for Data Engineering

Topic Explanation (Simple):
Instead of reading messy files line-by-line, Pandas acts like a Robot Assistant. 
You give it a file path, and it instantly converts the ugly comma-separated text (CSV) 
or nested dictionaries (JSON) into a beautiful 2D DataFrame table in your computer's memory.

In Data Engineering, this is used to:
- Extract data from raw daily sales files (pd.read_csv).
- Extract data from web APIs (pd.read_json).
- Safely peek at giant 10-million-row datasets without crashing the computer (.head()).
- Load the cleaned data into a fresh file to send to the database (.to_csv).
"""

import pandas as pd

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Setup: Let's create a fake CSV file on the computer first
with open("raw_data.csv", "w") as file:
    file.write(
        "Date,Product,Price\nMon,Mouse,150\nTue,Keyboard,300\nWed,Monitor,2500")

# Example 1: The "Extract" Phase (Loading the CSV)
# The Robot Assistant reads the file and builds the DataFrame automatically.
df = pd.read_csv("raw_data.csv")

print("Example 1: Extracted DataFrame")
print(df)
print("-" * 30)

# Example 2: Safely Peeking at the Data
# If the file has millions of rows, .head() protects your screen by only showing the top 5.
print("Example 2: Peeking at the top rows")
print(df.head())
print("-" * 30)

# Example 3: The "Load" Phase (Saving the data)
# We save it back to the computer. index=False stops Pandas from saving the 0,1,2 row numbers!
df.to_csv("cleaned_data.csv", index=False)

print("Example 3: File saved successfully as cleaned_data.csv")
print("-" * 30)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# Setup: Run this to create your practice files
with open("orders.csv", "w") as f:
    f.write("OrderID,Item,Amount\n101,Laptop,1000\n102,Mouse,25\n103,Screen,200")

with open("users.json", "w") as f:
    f.write('[{"Name": "Ali", "Age": 25}, {"Name": "Sara", "Age": 30}]')

# TODO 1:
# Use pd.read_csv() to load "orders.csv" into a variable called orders_df. Print it.

# TODO 2:
# Use .head() to print only the top 5 rows of your new orders_df.

# TODO 3:
# Use pd.read_json() to load "users.json" into a variable called users_df. Print it.

# TODO 4: (Mini Data Engineer Task)
# Save your orders_df back to your computer as "final_orders.csv".
# Remember the golden rule: index=False.
# Do not print the saving action. Just print "Saved!" on the next line.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: What is the purpose of `.head()` in Pandas?
# Ans: It returns the first 5 rows of a DataFrame, allowing Data Engineers to quickly inspect the structure of massive datasets without printing millions of rows to the console.

# Q2: When saving a DataFrame to a CSV using `.to_csv()`, why do we almost always use `index=False`?
# Ans: If we don't, Pandas will write the arbitrary row numbers (0, 1, 2...) into the file as a brand new, unnamed column, which corrupts the data structure for whoever uses the file next.

# Q3: Does `pd.read_csv()` return a Series or a DataFrame?
# Ans: It returns a DataFrame automatically. You do not need to wrap it in `pd.DataFrame()`.
