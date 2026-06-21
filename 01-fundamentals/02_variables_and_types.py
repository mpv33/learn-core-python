"""
02 — Variables and Data Types
==============================

Variables store values. Python has several built-in types.
"""

# --- Integers (whole numbers) ---
age = 25
year = 2026
print(f"age: {age}, type: {type(age)}")

# --- Floats (decimal numbers) ---
price = 19.99
pi = 3.14159
print(f"price: {price}, type: {type(price)}")

# --- Strings (text) ---
name = "Alice"
greeting = 'Hello'
print(f"name: {name}, type: {type(name)}")

# --- Boolean (True / False) ---
is_active = True
is_admin = False
print(f"is_active: {is_active}, type: {type(is_active)}")

# --- None (represents "no value") ---
result = None
print(f"result: {result}, type: {type(result)}")

# --- Type conversion ---
num_str = "42"
num_int = int(num_str)      # string → int
num_float = float("3.14")   # string → float
back_to_str = str(100)      # int → string

print(num_int + 8)          # 50
print(num_float * 2)        # 6.28

# --- Multiple assignment ---
x, y, z = 1, 2, 3
print(x, y, z)

# --- Constants convention (UPPER_CASE) ---
MAX_USERS = 100
print(f"Max users allowed: {MAX_USERS}")

# --- Check type at runtime ---
value = 42
print(isinstance(value, int))   # True
print(isinstance(value, str))   # False
