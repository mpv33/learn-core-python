"""01 — List Comprehensions"""

# Basic: [expression for item in iterable]
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# Transform strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(f"Upper: {upper}")

# Nested comprehension (flatten 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flat: {flat}")

# With if-else (expression before for)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Labels: {labels}")

# Practical: filter and transform
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 55},
    {"name": "Carol", "score": 88},
]
passed = [s["name"] for s in students if s["score"] >= 60]
print(f"Passed: {passed}")

# Compare to loop (comprehension is faster and more Pythonic for simple cases)
# Loop version:
doubled_loop = []
for x in range(5):
    doubled_loop.append(x * 2)

doubled_comp = [x * 2 for x in range(5)]
print(f"Doubled: {doubled_comp}")
