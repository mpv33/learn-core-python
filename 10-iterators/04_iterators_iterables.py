"""04 — Iterators and Iterables"""

# Iterable: has __iter__() — can be looped over (list, str, dict)
# Iterator: has __next__() — produces values one at a time

# Built-in iter() and next()
nums = iter([10, 20, 30])
print(f"next: {next(nums)}, next: {next(nums)}")

# Custom iterator class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("\nCountdown:", list(Countdown(5)))

# Custom iterable (not iterator) — returns fresh iterator each time
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

r = Range(2, 6)
print(f"Range: {list(r)}")
print(f"Reuse:  {list(r)}")

# itertools module
from itertools import islice, cycle, chain, zip_longest

print(f"\nislice first 5 of infinite: {list(islice(cycle('AB'), 5))}")
print(f"chain: {list(chain([1,2], [3,4]))}")
print(f"zip_longest: {list(zip_longest([1,2], [3,4,5], fillvalue=0))}")

# Check iterability
from collections.abc import Iterable, Iterator

print(f"\nlist is Iterable: {isinstance([1,2], Iterable)}")
print(f"list is Iterator: {isinstance([1,2], Iterator)}")
print(f"iter(list) is Iterator: {isinstance(iter([1,2]), Iterator)}")
