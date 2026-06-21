"""
PEP 8 Style Guide — Key Conventions
====================================

Naming:
  - variables, functions: snake_case
  - Classes: PascalCase
  - Constants: UPPER_SNAKE_CASE
  - Private: _leading_underscore

Formatting:
  - 4 spaces per indent (no tabs)
  - Max line length: 79-88 chars
  - Two blank lines between top-level functions/classes
  - One blank line between methods
"""

# Good naming examples
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30


def calculate_total_price(items: list[dict]) -> float:
    """Calculate sum of item prices."""
    return sum(item["price"] for item in items)


class ShoppingCart:
    """A shopping cart that holds items."""

    def __init__(self) -> None:
        self._items: list[dict] = []

    def add_item(self, name: str, price: float) -> None:
        self._items.append({"name": name, "price": price})

    def total(self) -> float:
        return calculate_total_price(self._items)


# Prefer explicit over implicit
def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]


# Use enumerate instead of range(len())
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Use context managers for resources
# with open("file.txt") as f: ...

# Avoid bare except
def safe_parse(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None

# Demo
cart = ShoppingCart()
cart.add_item("Book", 19.99)
cart.add_item("Pen", 2.50)
print(f"\nCart total: ${cart.total():.2f}")
print(f"Valid email: {is_valid_email('user@example.com')}")

# Tools: black (formatter), ruff/flake8 (linter), isort (imports)
