"""01 — try / except basics"""

# Without handling — program crashes
# result = 10 / 0  # ZeroDivisionError

# With handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = None

print(f"Result: {result}")

# Handle and continue
numbers = ["10", "20", "abc", "30"]
total = 0

for num in numbers:
    try:
        total += int(num)
    except ValueError:
        print(f"  Skipping invalid value: {num!r}")

print(f"Total: {total}")

# Access exception info
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    print(f"IndexError: {e}")

# Common built-in exceptions:
# ValueError, TypeError, KeyError, IndexError, FileNotFoundError, AttributeError
