"""
19 — Higher-Order Functions

THEORY
------
What: Functions that take other functions as arguments or return functions as results.
Why:  Enable flexible, reusable logic — validators, pipelines, decorators, callbacks.
Key rules:
  - HOF = higher-order function; closures capture variables from enclosing scope.
  - compose(f, g)(x) = f(g(x)); pipeline applies left-to-right.
  - Decorators are a special case of HOFs that wrap callables.
When to use: Strategy selection, configurable validation, data transformation pipelines.
Common mistakes: Closure late-binding bug in loops; returning wrapper without @wraps;
                 over-abstracting simple one-off logic into HOF chains.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/19_higher_order_functions.py
"""

from functools import reduce  # import left-to-right fold helper


def apply_operation(numbers, operation):  # apply a callable to each number
    return [operation(n) for n in numbers]  # list comprehension applying operation


def square(n):  # return n squared
    return n ** 2


def negate(n):  # return negated value
    return -n


def make_validator(min_val, max_val):  # factory for range-checking validators
    def validate(value):  # inner closure captures min and max bounds
        return min_val <= value <= max_val  # True when value is within range
    return validate  # return configured validator function


def compose(*functions):  # combine functions right-to-left
    def composed(x):  # apply pipeline to single input
        result = x  # start with input value
        for f in reversed(functions):  # apply each function from right to left
            result = f(result)  # feed output of prior step as next input
        return result  # return final transformed value
    return composed  # return composed callable


def add_one(x):  # increment by one
    return x + 1


def double(x):  # multiply by two
    return x * 2


def pipeline(value, *functions):  # apply functions sequentially left-to-right
    return reduce(lambda v, f: f(v), functions, value)  # fold functions over starting value


def trace(func):  # decorator that logs function calls
    def wrapper(*args, **kwargs):  # replace func with logging wrapper
        print(f"  → {func.__name__}{args}")  # log function name and positional args
        return func(*args, **kwargs)  # delegate to original function
    return wrapper  # return wrapped callable


@trace  # apply trace decorator to greet
def greet(name):  # simple greeting function
    return f"Hello, {name}!"


def main() -> None:  # entry point for all practice demos
    nums = [1, 2, 3, 4, 5]  # sample numbers to transform

    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Function as argument")  # section header
    print("=" * 50)  # close header divider
    print(f"Square: {apply_operation(nums, square)}")  # pass square as operation
    print(f"Negate: {apply_operation(nums, negate)}")  # pass negate as operation

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Function that returns a function")  # section header
    print("=" * 50)  # close header divider
    age_validator = make_validator(0, 120)  # validator for human ages
    score_validator = make_validator(0, 100)  # validator for percentage scores
    print(f"Age 25 valid: {age_validator(25)}")  # test age within valid range
    print(f"Score 150 valid: {score_validator(150)}")  # test score outside valid range

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — compose functions")  # section header
    print("=" * 50)  # close header divider
    add_then_double = compose(double, add_one)  # first add_one, then double
    print(f"compose(double, add_one)(5) = {add_then_double(5)}")  # (5+1)*2 = 12

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — pipeline with reduce")  # section header
    print("=" * 50)  # close header divider
    result = pipeline(5, add_one, double, lambda x: x - 3)  # chain add, double, subtract
    print(f"Pipeline result: {result}")  # show final pipeline output

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Decorator as HOF")  # section header
    print("=" * 50)  # close header divider
    print(greet("Alice"))  # call traced greet and print result


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
