"""
10 — Multiple Exceptions
========================

THEORY
------
What:
  Python lets you handle several exception types with separate `except` blocks,
  a tuple of types in one block, or a broad catch as a last resort.

Why:
  Different errors need different responses — division by zero vs type mismatch
  vs missing config key each deserve specific handling.

Key rules:
  - Multiple blocks: `except A:` then `except B:` — first match wins.
  - Tuple catch: `except (KeyError, TypeError) as e:` handles either type.
  - Order matters — put specific exceptions before general ones.
  - `except Exception as e:` catches nearly everything — use sparingly at boundaries.
  - Re-raise with `raise` to propagate after logging or cleanup.

When to use:
  - Functions that can fail in several predictable ways (parsing, I/O, math).
  - API boundaries where you log and return defaults for known error types.
  - Config loaders that fall back when keys are missing or types wrong.

Common mistakes:
  - Catching `Exception` first — specific handlers below it never run.
  - Using broad catch to hide programming bugs instead of fixing them.
  - Returning None for every error without distinguishing failure reasons.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/10_multiple_exceptions.py
"""


def parse_age(value):
    try:  # attempt parsing and business-rule checks
        age = int(value)  # convert string to integer
        if age < 0:  # reject negative ages
            raise ValueError("Age cannot be negative")  # explicit validation error
        if age > 150:  # reject unrealistic ages
            raise ValueError("Age seems unrealistic")  # explicit validation error
        return age  # return valid parsed age
    except ValueError as e:  # catch int() failures and raised ValueErrors
        print(f"  Invalid age '{value}': {e}")  # report invalid input
        return None  # signal failure with None


def safe_divide(a, b):
    try:  # attempt division
        return a / b  # return quotient on success
    except ZeroDivisionError:  # handle divisor zero
        print("  Error: division by zero")  # explain zero-division failure
    except TypeError:  # handle non-numeric operands
        print("  Error: must be numbers")  # explain type mismatch
    return None  # fallback when an exception was caught


def read_config(data):
    try:  # attempt keyed access on config mapping
        return data["host"], data["port"]  # return tuple of settings
    except (KeyError, TypeError) as e:  # catch missing keys or non-mapping data
        print(f"  Config error: {e}")  # log configuration problem
        return "localhost", 8080  # safe default host and port


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Validation with explicit raise")  # label first block
    print("=" * 50)  # close header

    for test in ["25", "abc", "-5", "200"]:  # exercise valid and invalid inputs
        result = parse_age(test)  # attempt to parse each test value
        if result is not None:  # print only successful parses
            print(f"  Valid age: {result}")  # show accepted age

    print("\n" + "=" * 50)  # divider before multiple except demo
    print("PRACTICE 2 — Multiple except blocks")  # label second block
    print("=" * 50)  # close header

    print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")  # normal division succeeds
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")  # triggers ZeroDivisionError
    print(f"safe_divide(10, 'a') = {safe_divide(10, 'a')}")  # triggers TypeError

    print("\n" + "=" * 50)  # divider before tuple except demo
    print("PRACTICE 3 — Tuple of exceptions")  # label third block
    print("=" * 50)  # close header

    print(f"Config: {read_config({'host': 'api.com'})}")  # missing port → KeyError → defaults
    print(f"Config: {read_config({})}")  # empty dict falls back to defaults
    print(f"Config: {read_config({'host': 'prod.com', 'port': 443})}")  # valid config succeeds

    print("\n" + "=" * 50)  # divider before broad catch demo
    print("PRACTICE 4 — Catch-all (use sparingly)")  # label fourth block
    print("=" * 50)  # close header

    try:  # reference an undefined name intentionally
        x = undefined_variable  # noqa: F821 — intentionally undefined for demo
    except Exception as e:  # broad catch; avoid in production except at boundaries
        print(f"Caught {type(e).__name__}: {e}")  # show exception class and message


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
