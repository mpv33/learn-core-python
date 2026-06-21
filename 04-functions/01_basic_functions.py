"""01 — Basic Functions"""

def greet(name: str) -> str:
    """Return a greeting message. This is a docstring."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet.__doc__)

def add(a, b):
    return a + b

print(f"add(3, 5) = {add(3, 5)}")

# Multiple return values (actually returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5])
print(f"min={lo}, max={hi}")

# Early return
def absolute(n):
    if n < 0:
        return -n
    return n

print(f"abs(-7) = {absolute(-7)}")

# No return → None
def log_message(msg):
    print(f"[LOG] {msg}")

result = log_message("System started")
print(f"Return value: {result}")

# Type hints (documentation + tooling)
def calculate_area(width: float, height: float) -> float:
    return width * height

print(f"Area: {calculate_area(5.0, 3.0)}")
