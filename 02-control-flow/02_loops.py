"""
02 — Loops
===========
Repeat code with for and while loops.
"""

# --- for loop over a sequence ---
print("Fruits:")
for fruit in ["apple", "banana", "cherry"]:
    print(f"  - {fruit}")

# --- range() generates numbers ---
print("\nCount 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

print("Count 2 to 8 step 2:")
for i in range(2, 9, 2):
    print(i, end=" ")
print()

# --- enumerate: index + value ---
print("\nWith index:")
for index, fruit in enumerate(["apple", "banana"]):
    print(f"  {index}: {fruit}")

# --- while loop ---
print("\nCountdown:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Go!")

# --- Loop over dictionary ---
user = {"name": "Alice", "age": 30, "city": "NYC"}
print("\nUser info:")
for key, value in user.items():
    print(f"  {key}: {value}")

# --- Loop over string ---
print("\nLetters in 'Python':")
for char in "Python":
    print(char, end=" ")
print()

# --- zip: iterate multiple sequences together ---
names = ["Alice", "Bob"]
scores = [90, 85]
print("\nName → Score:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# --- Nested loops ---
print("\nMultiplication table (2x):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")
