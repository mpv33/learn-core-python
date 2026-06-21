"""03 — Immutable Patterns"""

# Tuples and frozensets are immutable
config = ("localhost", 8080, "production")
# config[0] = "127.0.0.1"  # TypeError

# Copy-on-write for dicts
original = {"a": 1, "b": 2}
updated = {**original, "b": 99, "c": 3}
print(f"Original: {original}")
print(f"Updated:  {updated}")

# dataclass with frozen=True (see 15_advanced_oop)
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(3, 4)
print(f"Frozen point: {p}")
# p.x = 5  # FrozenInstanceError

# Avoid in-place list mutation — return new list
def add_item(items, item):
    return [*items, item]  # spread into new list

fruits = ["apple", "banana"]
fruits = add_item(fruits, "cherry")
print(f"New list: {fruits}")

# tuple unpacking for updates
record = {"name": "Alice", "scores": [90, 85]}
new_record = {**record, "scores": [*record["scores"], 92]}
print(f"Updated record: {new_record}")

# Named tuple for read-only records
from collections import namedtuple
User = namedtuple("User", ["id", "name", "email"])
user = User(1, "Alice", "alice@example.com")
print(f"User: {user.name}")

# Sort returns new list (sorted) vs mutates (list.sort)
nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)
print(f"Original: {nums}, Sorted copy: {sorted_nums}")
