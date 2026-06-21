"""01 — String Basics"""

s = "Hello, Python!"
print(f"Length: {len(s)}")
print(f"First char: {s[0]}, Last: {s[-1]}")
print(f"Slice [7:13]: {s[7:13]}")
print(f"Every 2nd char: {s[::2]}")

# Multi-line strings
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you."""
print(poem)

# Escape sequences
print("Line1\nLine2\tTabbed")
print('She said "Hi"')
print("It\\'s fine")

# Raw strings (backslashes not escaped)
path = r"C:\Users\name\file.txt"
print(f"Raw path: {path}")

# String concatenation
first = "Hello"
second = "World"
print(first + " " + second)
print(first * 3)

# Check membership
print(f"'Python' in s: {'Python' in s}")
print(f"'Java' not in s: {'Java' not in s}")

# Iterate
for char in "abc":
    print(char, end=" ")
print()

# Strings are immutable
# s[0] = "h"  # TypeError

# Encoding
text = "café"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
print(f"\nEncoded bytes: {encoded}")
print(f"Decoded: {decoded}")
