"""04 — Dictionaries: key-value mappings."""

# Create
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

print(f"person: {person}")
print(f"name: {person['name']}")

# Safe access
print(f"email (get): {person.get('email', 'N/A')}")

# Modify
person["age"] = 31
person["email"] = "alice@example.com"
print(f"Updated: {person}")

# Remove
removed_age = person.pop("age")
del person["city"]
print(f"After pop/del: {person}, removed age: {removed_age}")

# Iterate
print("\nKeys, values, items:")
for key in person:
    print(f"  key={key}, value={person[key]}")

for key, value in person.items():
    print(f"  {key}: {value}")

# dict comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares: {squares}")

# Merge dicts (Python 3.9+)
defaults = {"theme": "dark", "lang": "en"}
user_prefs = {"lang": "hi", "font_size": 14}
merged = defaults | user_prefs
print(f"Merged: {merged}")

# Nested dict
company = {
    "name": "TechCorp",
    "employees": {
        "E001": {"name": "Alice", "role": "Engineer"},
        "E002": {"name": "Bob", "role": "Designer"},
    }
}
print(f"\nEmployee E001: {company['employees']['E001']}")

# defaultdict — auto-create missing keys
from collections import defaultdict
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1
print(f"Word counts: {dict(word_count)}")

# Counter
from collections import Counter
letters = Counter("mississippi")
print(f"Letter freq: {letters.most_common(3)}")
