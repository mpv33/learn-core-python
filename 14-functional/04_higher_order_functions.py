"""04 — Higher-Order Functions"""

def apply_operation(numbers, operation):
    """Takes a function as argument."""
    return [operation(n) for n in numbers]

def square(n):
    return n ** 2

def negate(n):
    return -n

nums = [1, 2, 3, 4, 5]
print(f"Square: {apply_operation(nums, square)}")
print(f"Negate: {apply_operation(nums, negate)}")

# Function that returns a function
def make_validator(min_val, max_val):
    def validate(value):
        return min_val <= value <= max_val
    return validate

age_validator = make_validator(0, 120)
score_validator = make_validator(0, 100)

print(f"Age 25 valid: {age_validator(25)}")
print(f"Score 150 valid: {score_validator(150)}")

# Compose functions
def compose(*functions):
    def composed(x):
        result = x
        for f in reversed(functions):
            result = f(result)
        return result
    return composed

def add_one(x):
    return x + 1

def double(x):
    return x * 2

add_then_double = compose(double, add_one)
print(f"compose(double, add_one)(5) = {add_then_double(5)}")

# Pipeline with reduce
from functools import reduce

def pipeline(value, *functions):
    return reduce(lambda v, f: f(v), functions, value)

result = pipeline(5, add_one, double, lambda x: x - 3)
print(f"Pipeline result: {result}")

# Decorator as HOF
def trace(func):
    def wrapper(*args, **kwargs):
        print(f"  → {func.__name__}{args}")
        return func(*args, **kwargs)
    return wrapper

@trace
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
