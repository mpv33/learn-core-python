"""02 — Tuples: ordered, immutable sequences."""

# Create
point = (3, 4)
single = (42,)          # comma required for single-element tuple
rgb = 255, 128, 0       # parentheses optional

print(f"point: {point}, type: {type(point)}")

# Access (read-only)
x, y = point            # unpacking
print(f"x={x}, y={y}")

# Named tuple (readable fields)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"Named: {p.x}, {p.y}")

# Tuples as dict keys (lists cannot be keys)
locations = {(0, 0): "origin", (1, 2): "point A"}
print(f"Location at (0,0): {locations[(0, 0)]}")

# Immutable — cannot reassign elements
# point[0] = 5  # TypeError

# But mutable objects inside tuples CAN change
record = ("Alice", [90, 85, 88])
record[1].append(92)
print(f"Mutable inside tuple: {record}")

# Swap variables elegantly
a, b = 1, 2
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# Compare to list
print(f"\nTuple vs List memory (conceptually):")
print("  Tuple: fixed size, faster, hashable if all elements hashable")
print("  List:  flexible, more methods, not hashable")
