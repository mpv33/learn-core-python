"""
04 — Input and Output
======================

input() reads from the keyboard. print() writes to the console.
"""

# --- Basic input ---
# Uncomment to try interactively:
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# --- Simulated input for demo (non-interactive run) ---
name = "Demo User"
print(f"Hello, {name}!")

# --- input() always returns a string ---
# age = int(input("Enter age: "))  # Convert to int if needed

# --- print() formatting ---

# 1. f-strings (recommended, Python 3.6+)
item = "book"
cost = 29.99
print(f"The {item} costs ${cost:.2f}")  # .2f = 2 decimal places

# 2. .format() method
print("The {} costs ${:.2f}".format(item, cost))

# 3. % formatting (older style)
print("The %s costs $%.2f" % (item, cost))

# --- Alignment and padding ---
num = 42
print(f"Number: {num:05d}")    # Zero-padded: 00042
print(f"Number: {num:>5}")     # Right-aligned in 5 chars

# --- Multiple values ---
x, y = 10, 20
print("x =", x, "y =", y)
print(f"x = {x}, y = {y}")

# --- Escape characters ---
print("Line 1\nLine 2")       # \n = newline
print("Tab\tseparated")       # \t = tab
print('She said "Hello"')     # Quotes inside strings
