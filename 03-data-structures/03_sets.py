"""03 — Sets: unordered collections of unique elements."""

# Create
colors = {"red", "green", "blue"}
numbers = set([1, 2, 2, 3, 3, 3])  # duplicates removed
empty = set()                       # not {} — that's a dict!

print(f"colors: {colors}")
print(f"numbers (deduplicated): {numbers}")

# Add / remove
colors.add("yellow")
colors.discard("green")     # no error if missing
# colors.remove("purple")   # KeyError if missing
print(f"After changes: {colors}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nUnion a | b:        {a | b}")
print(f"Intersection a & b: {a & b}")
print(f"Difference a - b:   {a - b}")
print(f"Symmetric a ^ b:      {a ^ b}")

# Membership (fast O(1) lookup)
print(f"\n2 in a: {2 in a}")

# Remove duplicates from list
items = ["apple", "banana", "apple", "cherry", "banana"]
unique = list(set(items))
print(f"Unique items: {unique}")

# frozenset — immutable set (can be dict key)
frozen = frozenset([1, 2, 3])
cache = {frozen: "cached_value"}
print(f"Frozen set as key: {cache[frozen]}")

# Practical: find common friends
alice_friends = {"Bob", "Carol", "Dave"}
bob_friends = {"Alice", "Carol", "Eve"}
mutual = alice_friends & bob_friends
print(f"\nMutual friends: {mutual}")
