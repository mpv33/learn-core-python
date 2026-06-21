"""05 — Recursion: function calls itself"""

def factorial(n: int) -> int:
    """n! = n × (n-1) × ... × 1"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

def fibonacci(n: int) -> int:
    """Return nth Fibonacci number (0-indexed)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fib(7) = {fibonacci(7)}")

# Recursion with helper
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(f"'racecar' palindrome: {is_palindrome('racecar')}")
print(f"'hello' palindrome: {is_palindrome('hello')}")

# Tail recursion note: Python doesn't optimize tail calls
# For deep recursion, use iteration or functools.lru_cache

from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(f"fib_cached(50) = {fib_cached(50)}")

# Iterative alternative (often preferred)
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"5! iterative = {factorial_iter(5)}")
