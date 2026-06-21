"""
16 — map, filter, reduce

THEORY
------
What: Functional-style tools to transform (map), select (filter), and fold (reduce) iterables.
Why:  Express data pipelines declaratively; map/filter often replace simple comprehensions.
Key rules:
  - map(func, iterable) returns an iterator — wrap in list() to see all results.
  - filter(func, iterable) or filter(None, iterable) to drop falsy values.
  - reduce(func, iterable[, initial]) folds left; prefer sum()/any() when they fit.
When to use: Existing function references (str.strip), multi-iterable zip-map, fold operations.
Common mistakes: Using map/lambda when a comprehension is clearer; forgetting map returns
                 iterator; reduce without initial on empty iterable raises TypeError.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/16_map_filter_reduce.py
"""

from functools import reduce  # import fold/accumulate helper


def main() -> None:  # entry point for all practice demos
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # sample integer sequence

    print("=" * 50)  # print section divider
    print("PRACTICE 1 — map: transform each element")  # section header
    print("=" * 50)  # close header divider
    doubled = list(map(lambda x: x * 2, nums))  # apply doubling function to every element
    print(f"Doubled: {doubled}")  # show mapped results as a list

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — filter: keep matching elements")  # section header
    print("=" * 50)  # close header divider
    evens = list(filter(lambda x: x % 2 == 0, nums))  # keep only even numbers
    print(f"Evens: {evens}")  # show filtered even values

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — reduce: accumulate to single value")  # section header
    print("=" * 50)  # close header divider
    total = reduce(lambda acc, x: acc + x, nums)  # fold list into sum
    product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])  # fold list into product
    print(f"Sum: {total}, Product: {product}")  # display both reduced values

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Comprehension equivalents")  # section header
    print("=" * 50)  # close header divider
    doubled_comp = [x * 2 for x in nums]  # comprehension equivalent of map doubling
    evens_comp = [x for x in nums if x % 2 == 0]  # comprehension equivalent of filter evens
    print(f"Comp doubled: {doubled_comp[:5]}...")  # preview first five doubled values

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — map with multiple iterables")  # section header
    print("=" * 50)  # close header divider
    a = [1, 2, 3]  # first parallel iterable
    b = [10, 20, 30]  # second parallel iterable
    sums = list(map(lambda x, y: x + y, a, b))  # element-wise addition across iterables
    print(f"Zipped sum: {sums}")  # show pairwise sums

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Practical string pipeline")  # section header
    print("=" * 50)  # close header divider
    words = ["  hello ", " WORLD ", "  Python  "]  # messy strings with whitespace
    cleaned = list(map(str.strip, words))  # strip leading/trailing whitespace
    lowered = list(map(str.lower, cleaned))  # normalize to lowercase
    print(f"Pipeline: {lowered}")  # show final cleaned lowercase strings

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — filter(None) removes falsy values")  # section header
    print("=" * 50)  # close header divider
    mixed = [0, 1, "", "hello", None, [], [1]]  # list containing truthy and falsy values
    truthy = list(filter(None, mixed))  # drop values that evaluate to False
    print(f"Truthy only: {truthy}")  # show remaining truthy elements


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
