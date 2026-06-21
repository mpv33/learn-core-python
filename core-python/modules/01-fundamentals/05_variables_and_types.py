"""
05 — Variables and Data Types: Storing Values in Python

THEORY
------
What is it?
    Variables are names bound to objects in memory. Python has dynamic typing — the
    type is determined by the value, not a declaration. Core built-in types include
    int, float, str, bool, and NoneType.

Why it matters
    Type confusion is a top source of bugs (adding str + int). isinstance() and
    type() help debug. UPPER_CASE convention signals constants. Interviewers test
    mutability, type conversion, and the difference between = and ==.

Key syntax/rules
    - x = 42                    → bind name x to integer object 42
    - type(x)                   → returns the object's type (<class 'int'>)
    - int("42"), str(100)       → explicit type conversion (casting)
    - a, b, c = 1, 2, 3         → multiple assignment via unpacking
    - MAX_SIZE = 100            → UPPER_CASE convention for constants (not enforced)
    - isinstance(x, int)        → preferred over type(x) == int (handles subclasses)

When to use
    - Every program — variables hold state, config, and computation results
    - Type conversion when reading input (always str) or parsing API/JSON data
    - isinstance() for defensive checks before operations

Common mistakes
    - Using type(x) == int instead of isinstance(x, int)
    - int("3.14") fails — use int(float("3.14")) for decimal strings
    - Reassigning UPPER_CASE "constants" (convention only, not enforced by Python)
    - Confusing None (no value) with 0 or "" (falsy but typed values)

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/05_variables_and_types.py
"""


def main() -> None:  # entry point that runs all variable and type practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Core built-in types")  # section title
    print("=" * 50)  # close section header
    age = 25  # assign whole number 25 to variable age
    price = 19.99  # assign a decimal price value
    name = "Alice"  # assign a text name using double quotes
    is_active = True  # assign truth value True for an active flag
    result = None  # assign None to mean "no result yet" or missing value
    print(f"int:   age={age}, type={type(age)}")  # show integer value and type
    print(f"float: price={price}, type={type(price)}")  # show float value and type
    print(f"str:   name={name}, type={type(name)}")  # show string value and type
    print(f"bool:  is_active={is_active}, type={type(is_active)}")  # show bool value and type
    print(f"None:  result={result}, type={type(result)}")  # show None and confirm NoneType

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Type conversion")  # section title
    print("=" * 50)  # close section header
    num_str = "42"  # store digits as a string (text), not a number
    num_int = int(num_str)  # convert string "42" to integer 42 for math
    num_float = float("3.14")  # convert string "3.14" to float 3.14
    back_to_str = str(100)  # convert integer 100 back to string "100"
    print(f"int('42') + 8     = {num_int + 8}")  # add integers → 50
    print(f"float('3.14') * 2 = {num_float * 2}")  # multiply float by 2 → 6.28
    print(f"str(100)          = '{back_to_str}' (type {type(back_to_str).__name__})")  # show string result

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Assignment and constants")  # section title
    print("=" * 50)  # close section header
    x, y, z = 1, 2, 3  # unpack three values into three variables at once
    print(f"Unpacking: x={x}, y={y}, z={z}")  # display all three assigned values
    MAX_USERS = 100  # UPPER_CASE signals a value that should not change
    print(f"Constant convention: MAX_USERS = {MAX_USERS}")  # print the constant in a readable message

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — isinstance runtime checks")  # section title
    print("=" * 50)  # close section header
    value = 42  # sample integer used for isinstance checks
    print(f"isinstance(42, int):  {isinstance(value, int)}")  # True — value is an integer
    print(f"isinstance(42, str):  {isinstance(value, str)}")  # False — value is not a string
    print(f"isinstance(True, int): {isinstance(True, int)}")  # True — bool is subclass of int

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: shopping cart totals")  # section title
    print("=" * 50)  # close section header
    item = "book"  # product name in the cart
    unit_price = 19.99  # price per item as float
    quantity = 3  # number of items purchased
    total = unit_price * quantity  # compute line total with float multiplication
    print(f"{quantity}x {item} @ ${unit_price:.2f} = ${total:.2f}")  # formatted receipt line


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all variable and type practice sections
