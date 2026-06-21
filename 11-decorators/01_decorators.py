"""01 — Function Decorators"""

from functools import wraps
import time

# A decorator is a function that takes a function and returns a wrapper
def timer(func):
    @wraps(func)  # preserves func.__name__, __doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    """Add two numbers slowly."""
    time.sleep(0.1)
    return a + b

result = slow_add(3, 5)
print(f"Result: {result}")
print(f"Function name preserved: {slow_add.__name__}")
print(f"Docstring preserved: {slow_add.__doc__}")

# Logging decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  CALL {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"  RETURN {result}")
        return result
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

multiply(4, 5)

# Stacking decorators (applied bottom-up)
def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"_{func(*args, **kwargs)}_"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

print(f"\nStacked: {greet('Alice')}")
