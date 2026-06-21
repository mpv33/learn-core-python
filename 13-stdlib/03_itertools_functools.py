"""03 — itertools and functools"""

from itertools import permutations, combinations, product, groupby, accumulate
from functools import reduce, partial, lru_cache

# itertools
print(f"Permutations of ABC (2): {list(permutations('ABC', 2))}")
print(f"Combinations of ABC (2): {list(combinations('ABC', 2))}")
print(f"Product: {list(product([1,2], ['a','b']))}")
print(f"Accumulate: {list(accumulate([1,2,3,4,5]))}")

data = [
    ("Fruit", "apple"), ("Fruit", "banana"),
    ("Veg", "carrot"), ("Veg", "broccoli"),
]
for key, group in groupby(data, key=lambda x: x[0]):
    items = [item for _, item in group]
    print(f"  {key}: {items}")

# functools.reduce
total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])
print(f"\nReduce sum: {total}")

# partial — fix some arguments
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(f"square(5)={square(5)}, cube(3)={cube(3)}")

# lru_cache — memoization
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"\nfib(20)={fib(20)}, cache info: {fib.cache_info()}")

# total_ordering — auto-generate comparison methods
from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"Score({self.value})"

print(f"\nScore(90) > Score(85): {Score(90) > Score(85)}")
