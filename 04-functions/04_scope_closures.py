"""04 — Scope and Closures"""

# Local vs global
x = "global"

def demo_scope():
    x = "local"
    print(f"  Inside function: {x}")

demo_scope()
print(f"Outside function: {x}")

# Modify global variable
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(f"Counter: {counter}")

# Enclosing scope (nonlocal)
def outer():
    message = "Hello"

    def inner():
        nonlocal message
        message = "Hello, World!"

    inner()
    return message

print(f"Outer after inner: {outer()}")

# Closure — inner function remembers outer variables
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

times3 = make_multiplier(3)
times5 = make_multiplier(5)
print(f"times3(4) = {times3(4)}, times5(4) = {times5(4)}")

# Practical closure: counter factory
def make_counter(start=0):
    count = start
    def increment(step=1):
        nonlocal count
        count += step
        return count
    return increment

counter = make_counter(10)
print(f"Counter: {counter()}, {counter()}, {counter(5)}")

# LEGB rule: Local → Enclosing → Global → Built-in
print(f"Built-in len: {len([1, 2, 3])}")
