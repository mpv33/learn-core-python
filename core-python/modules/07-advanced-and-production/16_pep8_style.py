"""
16 — PEP 8 Style Guide

THEORY
------
What: PEP 8 is Python's official style guide covering naming, formatting, imports, and
      idiomatic patterns for readable, consistent code.
Why:  Consistent style reduces cognitive load; tools (black, ruff) enforce it automatically.
Key rules:
  - snake_case for functions/variables; PascalCase for classes; UPPER_SNAKE for constants.
  - 4-space indent; max ~88 chars per line; two blank lines between top-level definitions.
  - Prefer enumerate over range(len()); use with for resources; catch specific exceptions.
When to use: All Python projects; configure black/ruff in CI for automatic enforcement.
Common mistakes: Inconsistent naming; bare except; mutable default arguments; tabs mixed
                 with spaces; not using a formatter/linter.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/16_pep8_style.py
"""

MAX_RETRIES = 3  # module-level constant in UPPER_SNAKE_CASE
DEFAULT_TIMEOUT = 30  # another configuration constant


def calculate_total_price(items: list[dict]) -> float:  # snake_case function with type hints
    """Calculate sum of item prices."""
    return sum(item["price"] for item in items)  # use comprehension over manual loop


class ShoppingCart:  # PascalCase class name
    """A shopping cart that holds items."""

    def __init__(self) -> None:  # initialize internal item storage
        self._items: list[dict] = []  # private list prefixed with underscore

    def add_item(self, name: str, price: float) -> None:  # public method to append item
        self._items.append({"name": name, "price": price})  # store name/price dict

    def total(self) -> float:  # compute cart total via helper
        return calculate_total_price(self._items)


def is_valid_email(email: str) -> bool:  # simple explicit email shape check
    return "@" in email and "." in email.split("@")[-1]  # require @ and domain dot


def safe_parse(value: str) -> int | None:  # parse int or return None on failure
    try:  # attempt conversion
        return int(value)
    except ValueError:  # catch specific conversion error only
        return None


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Naming conventions")  # section header
    print("=" * 50)  # close header divider
    print(f"MAX_RETRIES={MAX_RETRIES}, DEFAULT_TIMEOUT={DEFAULT_TIMEOUT}")  # show constants

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — ShoppingCart class demo")  # section header
    print("=" * 50)  # close header divider
    cart = ShoppingCart()  # create empty cart
    cart.add_item("Book", 19.99)  # add first item
    cart.add_item("Pen", 2.50)  # add second item
    print(f"Cart total: ${cart.total():.2f}")  # show formatted cart total

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — enumerate over range(len())")  # section header
    print("=" * 50)  # close header divider
    fruits = ["apple", "banana", "cherry"]  # sample iterable
    for index, fruit in enumerate(fruits):  # get index and value together
        print(f"  {index}: {fruit}")  # print indexed fruit name

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Specific exception handling")  # section header
    print("=" * 50)  # close header divider
    print(f"Valid email: {is_valid_email('user@example.com')}")  # demonstrate email validator
    print(f"Parse '42': {safe_parse('42')}")  # successful parse
    print(f"Parse 'abc': {safe_parse('abc')}")  # failed parse returns None

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Recommended tools")  # section header
    print("=" * 50)  # close header divider
    print("  black  — auto-formatter")  # formatting tool
    print("  ruff   — fast linter")  # linting tool
    print("  isort  — import sorter")  # import organization tool


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
