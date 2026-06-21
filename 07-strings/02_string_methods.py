"""02 — String Methods"""

text = "  Hello, World!  "
print(f"Original: '{text}'")

# Case
print(f"lower: '{text.lower()}'")
print(f"upper: '{text.upper()}'")
print(f"title: '{text.strip().title()}'")

# Whitespace
print(f"strip: '{text.strip()}'")
print(f"lstrip: '{text.lstrip()}'")

# Search
sentence = "Python is great. Python is fun."
print(f"find('great'): {sentence.find('great')}")
print(f"count('Python'): {sentence.count('Python')}")
print(f"startswith('Python'): {sentence.startswith('Python')}")
print(f"endswith('fun.'): {sentence.endswith('fun.')}")

# Replace
print(f"replace: {sentence.replace('Python', 'Java')}")

# Split and join
data = "apple,banana,cherry"
fruits = data.split(",")
print(f"split: {fruits}")
print(f"join: {' | '.join(fruits)}")

# Partition
print(f"partition: {sentence.partition(' is ')}")

# Alignment
name = "Python"
print(f"center: '{name.center(20, '-')}'")
print(f"left:   '{name.ljust(20)}'")
print(f"right:  '{name.rjust(20)}'")

# is* methods
print(f"\n'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")

# Remove prefix/suffix (Python 3.9+)
filename = "report.pdf"
print(f"removesuffix('.pdf'): {filename.removesuffix('.pdf')}")
