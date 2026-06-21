"""
01 — Basic Functions

THEORY
------
What is it?
    A function is a reusable block of code defined with def that accepts
    parameters and optionally returns a value. Functions are first-class
    objects in Python — they can be assigned, passed, and stored like any value.

Why it matters
    Functions are the building block of readable, testable code. Type hints,
    docstrings, and clear return values make code self-documenting and enable
    IDE support, linters, and static analysis tools.

Key syntax/rules
    - def name(param: type) -> return_type: defines a function with optional hints
    - return sends a value back; omitting return gives None implicitly
    - Multiple values: return a, b returns a tuple — caller unpacks with x, y = fn()
    - Docstrings (triple-quoted string as first statement) document the function
    - Parameters are passed by object reference — reassigning a param doesn't affect caller
    - UPPER_CASE constants convention applies to module-level fixed values, not functions

When to use
    - Any repeated logic that deserves a name and single responsibility
    - Encapsulating calculations, validations, or transformations
    - Breaking large scripts into testable units
    - Returning computed results instead of printing inside functions

Common mistakes
    - Using print() instead of return — makes functions hard to test and reuse
    - Forgetting that functions without return give None
    - Naming functions after what they return, not what they do (verb_noun pattern)
    - Putting side effects in functions meant to compute and return values

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/01_basic_functions.py
"""


def greet(name: str) -> str:  # define a function with type hints and a docstring
    """Return a greeting message. This is a docstring."""
    return f"Hello, {name}!"  # return a formatted greeting string


def add(a, b):  # simple function with two parameters (no type hints)
    return a + b  # return sum of a and b


def min_max(numbers):  # function returning multiple values as a tuple
    return min(numbers), max(numbers)  # return both min and max together


def absolute(n):  # function demonstrating early return
    if n < 0:  # if the number is negative
        return -n  # return the negated value immediately
    return n  # otherwise return the value as-is


def log_message(msg):  # function with side effect and no return value
    print(f"[LOG] {msg}")  # print a log message (no return statement)


def calculate_area(width: float, height: float) -> float:  # typed function for area calculation
    return width * height  # multiply width and height for area


def main() -> None:  # entry point that runs all basic function practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Define and call functions")  # section title
    print("=" * 50)  # close section header
    print(greet("Alice"))  # call greet and print the result
    print(greet.__doc__)  # access the function's docstring via __doc__

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Return values and unpacking")  # section title
    print("=" * 50)  # close section header
    print(f"add(3, 5) = {add(3, 5)}")  # call add with two arguments
    lo, hi = min_max([3, 1, 4, 1, 5])  # unpack the returned tuple into two variables
    print(f"min={lo}, max={hi}")  # display unpacked min and max

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Early return and None")  # section title
    print("=" * 50)  # close section header
    print(f"abs(-7) = {absolute(-7)}")  # test absolute with a negative number
    result = log_message("System started")  # call log_message and capture return value
    print(f"Return value: {result}")  # show that functions without return give None

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Type hints")  # section title
    print("=" * 50)  # close section header
    print(f"Area: {calculate_area(5.0, 3.0)}")  # calculate and display area of a rectangle

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: format currency")  # section title
    print("=" * 50)  # close section header
    def format_currency(amount: float, symbol: str = "₹") -> str:  # helper with default symbol
        return f"{symbol}{amount:,.2f}"  # return formatted string with thousands separator
    print(format_currency(1234567.8))  # format with default rupee symbol
    print(format_currency(99.5, "$"))  # format with custom dollar symbol

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: validate password length")  # section title
    print("=" * 50)  # close section header
    def is_valid_password(password: str, min_length: int = 8) -> bool:  # validation helper
        return len(password) >= min_length  # True when password meets minimum length
    print(f"'hello' valid: {is_valid_password('hello')}")  # too short — False
    print(f"'hello123' valid: {is_valid_password('hello123')}")  # long enough — True


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all basic function practice sections
