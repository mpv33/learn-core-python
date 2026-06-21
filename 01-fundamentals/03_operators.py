"""
03 — Operators
===============

Operators perform operations on values and variables.
"""

a, b = 10, 3

# --- Arithmetic ---
print("Arithmetic:")
print(f"  {a} + {b} = {a + b}")   # Addition: 13
print(f"  {a} - {b} = {a - b}")   # Subtraction: 7
print(f"  {a} * {b} = {a * b}")   # Multiplication: 30
print(f"  {a} / {b} = {a / b}")   # Division (float): 3.333...
print(f"  {a} // {b} = {a // b}") # Floor division: 3
print(f"  {a} % {b} = {a % b}")   # Modulo (remainder): 1
print(f"  {a} ** {b} = {a ** b}") # Exponent: 1000

# --- Comparison (returns True or False) ---
print("\nComparison:")
print(f"  {a} == {b}: {a == b}")  # Equal
print(f"  {a} != {b}: {a != b}")  # Not equal
print(f"  {a} > {b}: {a > b}")    # Greater than
print(f"  {a} <= {b}: {a <= b}")  # Less than or equal

# --- Logical ---
x, y = True, False
print("\nLogical:")
print(f"  x and y: {x and y}")    # Both must be True
print(f"  x or y: {x or y}")      # At least one True
print(f"  not x: {not x}")        # Negation

# --- Assignment shortcuts ---
n = 5
n += 3   # n = n + 3  → 8
n *= 2   # n = n * 2  → 16
print(f"\nAfter += and *=: n = {n}")

# --- Identity (same object in memory?) ---
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"\nlist1 == list2: {list1 == list2}")   # True (same values)
print(f"list1 is list2: {list1 is list2}")     # False (different objects)
print(f"list1 is list3: {list1 is list3}")     # True (same object)

# --- Membership ---
fruits = ["apple", "banana", "cherry"]
print(f"\n'banana' in fruits: {'banana' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# --- Chained comparisons ---
score = 85
print(f"\n60 <= {score} < 90: {60 <= score < 90}")
