"""
14 — itertools and functools

THEORY
------
What: itertools provides iterator building blocks; functools offers higher-order function
      utilities like reduce, partial, lru_cache, and total_ordering.
Why:  Compose efficient lazy pipelines and add memoization/comparison without boilerplate.
Key rules:
  - itertools returns iterators — wrap in list() to materialize for display.
  - groupby requires sorted input for all-group grouping (consecutive keys only).
  - lru_cache: cache by arguments; use maxsize and cache_info() for tuning.
When to use: Combinatorics, running totals, partial application, expensive pure functions.
Common mistakes: Forgetting groupby needs sorted data; unbounded lru_cache on large arg
                 spaces; using reduce when sum()/any() is clearer.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/14_itertools_functools.py
"""

from itertools import permutations, combinations, product, groupby, accumulate  # combinator tools
from functools import reduce, partial, lru_cache, total_ordering  # functional helpers


def power(base, exp):  # compute base raised to exponent
    return base ** exp  # return power result


@lru_cache(maxsize=128)  # cache up to 128 distinct fib(n) results
def fib(n):  # recursive Fibonacci with memoization
    if n < 2:  # base cases for 0 and 1
        return n
    return fib(n - 1) + fib(n - 2)  # sum of two prior Fibonacci values


@total_ordering  # derive __le__, __gt__, etc. from __eq__ and __lt__
class Score:  # comparable score wrapper
    def __init__(self, value):  # store numeric score
        self.value = value

    def __eq__(self, other):  # equality based on score value
        return self.value == other.value

    def __lt__(self, other):  # less-than based on score value
        return self.value < other.value

    def __repr__(self):  # readable debug representation
        return f"Score({self.value})"


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — itertools combinatorics")  # section header
    print("=" * 50)  # close header divider
    print(f"Permutations of ABC (2): {list(permutations('ABC', 2))}")  # ordered 2-item arrangements
    print(f"Combinations of ABC (2): {list(combinations('ABC', 2))}")  # unordered 2-item selections
    print(f"Product: {list(product([1, 2], ['a', 'b']))}")  # cartesian product
    print(f"Accumulate: {list(accumulate([1, 2, 3, 4, 5]))}")  # running totals

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — groupby")  # section header
    print("=" * 50)  # close header divider
    data = [  # sample categorized records as (category, item) tuples
        ("Fruit", "apple"), ("Fruit", "banana"),
        ("Veg", "carrot"), ("Veg", "broccoli"),
    ]
    for key, group in groupby(data, key=lambda x: x[0]):  # group consecutive rows by category
        items = [item for _, item in group]  # collect item names within each group
        print(f"  {key}: {items}")  # print grouped items per category

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — functools.reduce")  # section header
    print("=" * 50)  # close header divider
    total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])  # fold list into a single sum
    print(f"Reduce sum: {total}")  # show reduced total

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — partial application")  # section header
    print("=" * 50)  # close header divider
    square = partial(power, exp=2)  # bind exponent to 2 for squaring
    cube = partial(power, exp=3)  # bind exponent to 3 for cubing
    print(f"square(5)={square(5)}, cube(3)={cube(3)}")  # demonstrate partial application

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — lru_cache memoization")  # section header
    print("=" * 50)  # close header divider
    print(f"fib(20)={fib(20)}, cache info: {fib.cache_info()}")  # fast result plus cache stats

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — total_ordering")  # section header
    print("=" * 50)  # close header divider
    print(f"Score(90) > Score(85): {Score(90) > Score(85)}")  # test auto-generated comparison


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
