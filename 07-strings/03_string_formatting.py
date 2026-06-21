"""03 — String Formatting"""

name = "Alice"
score = 95.567
count = 42

# f-strings (preferred)
print(f"{name} scored {score:.1f}%")
print(f"Binary: {count:b}, Hex: {count:x}")
print(f"Padded: {count:05d}")

# Expressions inside f-strings
items = ["apple", "banana", "cherry"]
print(f"First item: {items[0].upper()}")
print(f"Total length: {sum(len(i) for i in items)}")

# Debug f-strings (Python 3.8+)
x = 10
print(f"{x=}")  # x=10

# format() method
print("Hello, {}! You have {} messages.".format(name, 5))
print("{1} before {0}".format("second", "first"))

# Named placeholders
print("{name} lives in {city}".format(name="Bob", city="Mumbai"))

# Format specifiers
pi = 3.14159265
print(f"Pi: {pi:.3f}")
print(f"Percent: {0.856:.1%}")
print(f"Thousands: {1234567:,}")

# Template strings (safe substitution)
from string import Template
t = Template("Dear $name, your balance is $$ $amount.")
print(t.substitute(name="Alice", amount="150.00"))
