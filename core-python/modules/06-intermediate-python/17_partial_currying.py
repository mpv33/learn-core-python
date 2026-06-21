"""
17 — Partial Functions and Currying

THEORY
------
What: partial fixes some arguments of a function, producing a new callable; currying
      transforms a multi-arg function into a chain of single-arg functions.
Why:  Configure reusable callbacks (sort keys, event handlers) without lambda boilerplate.
Key rules:
  - functools.partial(func, *args, **kwargs) binds arguments at call time.
  - Currying: f(a, b, c) → f(a)(b)(c) — common in functional languages, less in Python.
  - partial preserves func metadata when used with wraps-compatible functions.
When to use: Pre-configured sort keys, logging prefixes, API clients with fixed auth.
Common mistakes: Confusing partial with functools.cache; over-currying simple Python code;
                 binding mutable default args incorrectly.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/17_partial_currying.py
"""

from functools import partial  # import tool to pre-fill function arguments


def multiply(a, b, c):  # multiply three numbers together
    return a * b * c


def curry(func, arity):  # generic curry wrapper for functions of fixed arity
    def curried(*args):  # accumulate arguments across calls
        if len(args) >= arity:  # enough args collected — call original function
            return func(*args)
        return lambda *more: curried(*(args + more))  # return function awaiting more args
    return curried


def add_three(a, b, c):  # simple three-argument addition
    return a + b + c


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — partial: freeze arguments")  # section header
    print("=" * 50)  # close header divider
    double = partial(multiply, 2)  # fix first argument to 2 (2 * b * c)
    print(f"double(5, 1) = {double(5, 1)}")  # compute 2 * 5 * 1
    times_10 = partial(multiply, 1, 10)  # fix first two arguments to 1 and 10
    print(f"times_10(5) = {times_10(5)}")  # compute 1 * 10 * 5

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — partial for sort key")  # section header
    print("=" * 50)  # close header divider
    students = [("Alice", 92), ("Bob", 85), ("Carol", 98)]  # names paired with scores
    by_score = sorted(students, key=partial(lambda pair, idx: pair[idx], 1), reverse=True)  # by score desc
    print(f"By score: {by_score}")  # show students ordered by score

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Manual currying")  # section header
    print("=" * 50)  # close header divider
    def curry_add(a):  # outer function captures first argument
        def add_b(b):  # middle function captures second argument
            def add_c(c):  # inner function captures third argument
                return a + b + c  # sum all three captured values
            return add_c  # return inner callable
        return add_b  # return middle callable
    print(f"Curried: {curry_add(1)(2)(3)}")  # apply arguments one at a time

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Generic curry helper")  # section header
    print("=" * 50)  # close header divider
    add_three_curried = curry(add_three, 3)  # explicitly curry add_three with arity 3
    print(f"Partial apply: {add_three_curried(1)(2)(3)}")  # chained single-arg application
    print(f"Full apply:    {add_three_curried(1, 2, 3)}")  # all args supplied at once

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — partial for print prefix")  # section header
    print("=" * 50)  # close header divider
    debug_print = partial(print, "[DEBUG]", sep=" ")  # prefix debug output with label
    debug_print("Server started", "port=8080")  # print debug message with custom separator


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
