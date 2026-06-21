"""
04 — Iterators and Iterables

THEORY
------
What: An iterable can be looped over (__iter__); an iterator produces values one at a
      time (__next__) and raises StopIteration when exhausted.
Why:  Understanding the protocol unlocks custom collections, itertools, and generators.
Key rules:
  - iter(obj) calls obj.__iter__(); next(it) calls it.__next__().
  - Iterators are single-pass — create a new iterator to iterate again.
  - for-loops call iter() then repeatedly next() until StopIteration.
When to use: Custom sequence types, lazy pipelines, wrapping external data sources.
Common mistakes: Confusing iterable with iterator; reusing an exhausted iterator;
                 implementing __iter__ without __next__ (or vice versa) correctly.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/04_iterators_iterables.py
"""


class Countdown:  # iterator that counts down to zero
    def __init__(self, start: int):  # store starting value
        self.current = start  # mutable state for iteration

    def __iter__(self):  # make instance its own iterator
        return self  # iterator protocol: __iter__ returns iterator object

    def __next__(self):  # produce next countdown value
        if self.current <= 0:  # no values left
            raise StopIteration  # signal end of iteration
        value = self.current  # capture value to return
        self.current -= 1  # decrement for next call
        return value  # emit current countdown number


class Range:  # lightweight range-like iterable using a generator
    def __init__(self, start: int, end: int):  # store half-open interval [start, end)
        self.start = start  # first value to yield
        self.end = end  # stop before this value

    def __iter__(self):  # return a new generator each time
        current = self.start  # local counter independent per iteration
        while current < self.end:  # emit until end exclusive
            yield current  # produce next integer
            current += 1  # advance counter


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Built-in iter() and next()")  # section header
    print("=" * 50)  # close header divider
    nums = iter([10, 20, 30])  # obtain iterator from list
    print(f"next: {next(nums)}, next: {next(nums)}")  # manually consume first two values

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Custom iterator class")  # section header
    print("=" * 50)  # close header divider
    print(f"Countdown: {list(Countdown(5))}")  # materialize countdown into list

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Custom iterable (reusable)")  # section header
    print("=" * 50)  # close header divider
    r = Range(2, 6)  # iterable over 2, 3, 4, 5
    print(f"Range: {list(r)}")  # first full iteration
    print(f"Reuse:  {list(r)}")  # second iteration works because __iter__ is fresh

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — itertools utilities")  # section header
    print("=" * 50)  # close header divider
    from itertools import islice, cycle, chain, zip_longest  # iterator utilities
    print(f"islice first 5 of infinite: {list(islice(cycle('AB'), 5))}")  # take 5 from cycle
    print(f"chain: {list(chain([1, 2], [3, 4]))}")  # concatenate multiple iterables
    print(f"zip_longest: {list(zip_longest([1, 2], [3, 4, 5], fillvalue=0))}")  # zip unequal

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Check iterability with ABCs")  # section header
    print("=" * 50)  # close header divider
    from collections.abc import Iterable, Iterator  # ABCs for protocol checking
    print(f"list is Iterable: {isinstance([1, 2], Iterable)}")  # lists support iteration
    print(f"list is Iterator: {isinstance([1, 2], Iterator)}")  # lists are not iterators
    print(f"iter(list) is Iterator: {isinstance(iter([1, 2]), Iterator)}")  # iter returns iterator

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Manual for-loop protocol")  # section header
    print("=" * 50)  # close header divider
    it = iter(["a", "b", "c"])  # get iterator from list
    collected = []  # accumulate values manually
    while True:  # simulate for-loop with next()
        try:  # attempt to get next value
            collected.append(next(it))  # append successful next() result
        except StopIteration:  # iterator exhausted
            break  # exit manual loop
    print(f"Manual iteration: {collected}")  # show manually collected items


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
