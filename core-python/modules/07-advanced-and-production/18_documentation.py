"""
18 — Documentation with Docstrings

THEORY
------
What: Docstrings are triple-quoted strings placed immediately after def, class, or module
      definitions — accessible via __doc__ and help().
Why:  Self-documenting code; Sphinx/pydoc generate API docs from docstrings automatically.
Key rules:
  - First line: brief summary; blank line; then Args/Returns/Raises/Examples sections.
  - Pick one style per project: Google, NumPy, or Sphinx — stay consistent.
  - Module-level docstring describes the module's purpose at the top of the file.
When to use: All public functions, classes, and modules; especially library/API code.
Common mistakes: Docstrings that restate the function name; outdated docs; no Examples;
                 mixing docstring styles within one project.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/18_documentation.py
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:  # compute body mass index
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:
        BMI value rounded to 1 decimal place.

    Raises:
        ValueError: If height is zero or negative.

    Examples:
        >>> calculate_bmi(70, 1.75)
        22.9
    """
    if height_m <= 0:  # reject invalid height input
        raise ValueError("Height must be positive")
    return round(weight_kg / (height_m ** 2), 1)  # BMI formula with one decimal place


class BankAccount:  # simple account model documented with class docstring
    """
    A simple bank account.

    Attributes:
        owner: Account holder name.
        balance: Current balance in dollars.

    Example:
        >>> acc = BankAccount("Alice", 1000)
        >>> acc.deposit(500)
        1500
    """

    def __init__(self, owner: str, balance: float = 0):  # initialize owner and starting balance
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:  # add funds and return updated balance
        """Add funds and return new balance."""
        self.balance += amount  # increase balance by deposit amount
        return self.balance  # return new balance for chaining/display


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Access function docstring")  # section header
    print("=" * 50)  # close header divider
    print(calculate_bmi.__doc__[:80] + "...")  # preview first 80 chars of function docstring
    print(f"BMI example: {calculate_bmi(70, 1.75)}")  # demonstrate BMI calculation

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Class docstring and methods")  # section header
    print("=" * 50)  # close header divider
    acc = BankAccount("Alice", 1000)  # create account with initial balance
    print(f"After deposit: ${acc.deposit(500):,.2f}")  # deposit and print formatted balance
    print("help(BankAccount) available in interactive mode.")  # note about interactive help

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Docstring styles")  # section header
    print("=" * 50)  # close header divider
    print("  Google  — Args/Returns/Raises sections (used here)")  # Google style
    print("  NumPy   — Underlined sections with Parameters/Returns")  # NumPy style
    print("  Sphinx  — :param:, :returns:, :raises: directives")  # Sphinx style


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
