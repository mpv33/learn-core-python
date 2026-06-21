"""03 — Generators"""

# Generator function — uses yield instead of return
def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1

print("count_up_to(5):")
for num in count_up_to(5):
    print(f"  {num}", end=" ")
print()

# Generators are lazy — compute one value at a time
gen = count_up_to(3)
print(f"next: {next(gen)}, next: {next(gen)}, next: {next(gen)}")
# next(gen)  # StopIteration

# Generator expression (like list comp but lazy)
squares_gen = (x**2 for x in range(1, 6))
print(f"\nGenerator squares: {list(squares_gen)}")

# Memory benefit
import sys
list_size = sys.getsizeof([x for x in range(10000)])
gen_size = sys.getsizeof(x for x in range(10000))
print(f"List size: {list_size}, Gen size: {gen_size}")

# yield from — delegate to sub-generator
def chain_generators():
    yield from range(3)
    yield from ["a", "b"]
    yield from (x * 2 for x in range(3))

print(f"\nChained: {list(chain_generators())}")

# Practical: read large file line by line
def read_lines(lines):
    for line in lines:
        yield line.strip()

sample = ["line 1\n", "line 2\n", "line 3\n"]
for line in read_lines(sample):
    print(f"  {line}")

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(f"\nFirst 10 Fibonacci: {first_10}")
