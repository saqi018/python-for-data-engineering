"""
NumPy Data Types (dtype) for Data Engineering



Topic Explanation (Simple):
Normal Python lists are like a mixed bag: they can hold numbers and text together, 
but they are very slow and use a lot of RAM. 
NumPy arrays use `dtype` (Data Type). This is a strict rule: every single item 
in the array MUST be the exact same type. 

Because the computer knows exactly what type of data is inside, it can process 
millions of rows lightning fast and save massive amounts of memory.

In Data Engineering, NumPy dtypes are used to:
- Shrink giant datasets so they fit into RAM
- Speed up mathematical calculations
- Prevent "Type Errors" when saving data to databases
- Prepare clean columns for Pandas DataFrames
"""

import numpy as np

# ==================================================
# 1️⃣ SOLVED EXAMPLES (RUN & UNDERSTAND)
# ==================================================

# Example 1: Check default dtype
# NumPy automatically guesses the type based on the data.
arr_int = np.array([10, 20, 30])
arr_float = np.array([10.5, 20.5, 30.5])

print("Example 1:")
print("Int array dtype:", arr_int.dtype)      # Output: int32 or int64
print("Float array dtype:", arr_float.dtype)  # Output: float64
print("-" * 30)


# Example 2: Force a specific dtype during creation
# Useful when you want to save memory from the very beginning.
arr_force = np.array([1, 2, 3], dtype="float32")

print("Example 2:")
print("Data looks like floats now:", arr_force)
print("Forced dtype:", arr_force.dtype)
print("-" * 30)


# Example 3: Convert (Cast) an existing array
# Used when reading data from a file that guessed the wrong type.
arr_original = np.array([1.9, 2.5, 3.1])
arr_converted = arr_original.astype("int32")

print("Example 3:")
print("Original floats:", arr_original)
print("Converted to ints (decimals chopped off):", arr_converted)
print("-" * 30)


# Example 4: Type Coercion (Mixing types)
# NumPy forbids mixing. It will force everything into the most flexible type (text).
arr_mixed = np.array([1, 5.5, "Peshawar"])

print("Example 4:")
print("Mixed array coerced to strings:", arr_mixed)
print("Coerced dtype (U means string):", arr_mixed.dtype)
print("-" * 30)


# Example 5: Memory Optimization (The Data Engineer Trick)
# int8 holds small numbers (-128 to 127). int64 holds giant numbers.
arr_big_memory = np.array([1, 2, 3], dtype="int64")
arr_small_memory = np.array([1, 2, 3], dtype="int8")

print("Example 5:")
print("Memory used by int64 (bytes):", arr_big_memory.nbytes)
print("Memory used by int8 (bytes):", arr_small_memory.nbytes)
print("-" * 30)


# ==================================================
# 2️⃣ PRACTICE TASKS (UNSOLVED — DO YOURSELF)
# ==================================================

# TODO 1:
# Create a NumPy array with these decimals: [10.5, 20.2, 30.9]
# Print its dtype to see what NumPy defaults to.

# TODO 2:
# Create an array with [1, 0, 1, 0]
# Force the dtype to be "bool" when you create it.
# Print the array to see the True/False values.

# TODO 3:
# You have an array of strings: arr = np.array(["100", "200", "300"])
# Convert (cast) this array into integers using .astype()
# Print the new array multiplied by 2 to prove it is mathematical now.

# TODO 4:
# Create this mixed array: arr = np.array([True, 5, 10.6, "Build With Ai"])
# Print the array and its dtype. Notice what happened to the numbers and booleans.

# TODO 5: (Mini Data Engineer Task)
# You have a list of user ages: [25, 40, 45, 22]
# 1. Create a NumPy array from this list.
# 2. Force the data type to be the most memory-efficient integer (int8).
# 3. Print the array's memory size using .nbytes.


# ==================================================
# 3️⃣ IMPORTANT INTERVIEW QUESTIONS (ONLY ESSENTIAL)
# ==================================================

# Q1: Why does NumPy require all elements to be the exact same data type?
# Q2: What happens if you put an integer and a string in the same NumPy array?
# Q3: What is the difference between int8 and int64 in terms of memory?
# Q4: How do you change the data type of an existing NumPy array?
# Q5: Why is checking .nbytes important for Data Engineers?
#
# Interview Tip:
# "When loading large datasets, I always explicitly define the dtype
# (like using int8 for ages instead of int64) to optimize RAM usage
# and prevent out-of-memory crashes in my pipelines."
