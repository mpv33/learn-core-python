"""02 — Partial Functions and Currying"""

from functools import partial

def multiply(a, b, c):
    return a * b * c

# partial — freeze some arguments
double = partial(multiply, 2)
print(f"double(5, 1) = {double(5, 1)}")

times_10 = partial(multiply, 1, 10)
print(f"times_10(5) = {times_10(5)}")

# Practical: sort with fixed key
students = [("Alice", 92), ("Bob", 85), ("Carol", 98)]
by_score = sorted(students, key=partial(lambda pair, idx: pair[idx], 1), reverse=True)
print(f"By score: {by_score}")

# Currying — transform multi-arg function to chain of single-arg functions
def curry_add(a):
    def add_b(b):
        def add_c(c):
            return a + b + c
        return add_c
    return add_b

print(f"Curried: {curry_add(1)(2)(3)}")

# Manual curry helper
def curry(func, arity):
    def curried(*args):
        if len(args) >= arity:
            return func(*args)
        return lambda *more: curried(*(args + more))
    return curried

@curry
def add_three(a, b, c):
    return a + b + c

add_three_curried = curry(add_three, 3)
print(f"Partial apply: {add_three_curried(1)(2)(3)}")
print(f"Full apply:    {add_three_curried(1, 2, 3)}")

# Built-in partial for print
debug_print = partial(print, "[DEBUG]", sep=" ")
debug_print("Server started", "port=8080")
