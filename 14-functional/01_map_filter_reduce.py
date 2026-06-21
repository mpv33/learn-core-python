"""01 — map, filter, reduce"""

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — transform each element
doubled = list(map(lambda x: x * 2, nums))
print(f"Doubled: {doubled}")

# filter — keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Evens: {evens}")

# reduce — accumulate to single value
total = reduce(lambda acc, x: acc + x, nums)
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])
print(f"Sum: {total}, Product: {product}")

# Often list comprehensions are clearer
doubled_comp = [x * 2 for x in nums]
evens_comp = [x for x in nums if x % 2 == 0]
print(f"Comp doubled: {doubled_comp[:5]}...")

# map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(f"Zipped sum: {sums}")

# Practical pipeline
words = ["  hello ", " WORLD ", "  Python  "]
cleaned = list(map(str.strip, words))
lowered = list(map(str.lower, cleaned))
print(f"Pipeline: {lowered}")

# filter with None — removes falsy values
mixed = [0, 1, "", "hello", None, [], [1]]
truthy = list(filter(None, mixed))
print(f"Truthy only: {truthy}")
