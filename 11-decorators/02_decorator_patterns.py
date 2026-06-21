"""02 — Parameterized Decorators"""

from functools import wraps

# Decorator with arguments: needs an extra wrapper level
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))

# Retry decorator
import random

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def flaky_operation():
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success!"

random.seed(42)
try:
    print(f"\nFlaky result: {flaky_operation()}")
except ConnectionError:
    print("All retries exhausted.")

# Class-based decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"  Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def add(a, b):
    return a + b

print(f"\nadd(1,2)={add(1,2)}, add(3,4)={add(3,4)}, total calls={add.count}")
