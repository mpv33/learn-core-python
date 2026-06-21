"""02 — Dict and Set Comprehensions"""

# Dict comprehension: {key_expr: val_expr for item in iterable}
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(f"Word lengths: {word_lengths}")

# With condition
scores = {"Alice": 92, "Bob": 55, "Carol": 88, "Dave": 45}
passed = {name: score for name, score in scores.items() if score >= 60}
print(f"Passed: {passed}")

# Invert dict (values must be unique)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# Set comprehension: {expr for item in iterable}
unique_lengths = {len(w) for w in ["hi", "hello", "hey", "world"]}
print(f"Unique lengths: {unique_lengths}")

# Remove duplicates (case-insensitive)
words = ["Apple", "apple", "Banana", "banana", "Cherry"]
unique_lower = {w.lower() for w in words}
print(f"Unique (lower): {unique_lower}")

# Nested dict from list
users = [("Alice", 30), ("Bob", 25)]
user_dict = {name: age for name, age in users}
print(f"User dict: {user_dict}")

# Swap keys and values with transformation
config = {"debug": True, "timeout": 30}
str_config = {k: str(v) for k, v in config.items()}
print(f"String config: {str_config}")
