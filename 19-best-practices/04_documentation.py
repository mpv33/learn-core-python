"""
04 — Documentation with Docstrings
=====================================

Python uses docstrings (triple-quoted strings) for documentation.
"""

def calculate_bmi(weight_kg: float, height_m: float) -> float:
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
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return round(weight_kg / (height_m ** 2), 1)


class BankAccount:
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

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Add funds and return new balance."""
        self.balance += amount
        return self.balance


# Access documentation
print(calculate_bmi.__doc__[:80] + "...")
print(f"\nhelp(BankAccount) available in interactive mode.")
print(f"BMI example: {calculate_bmi(70, 1.75)}")

acc = BankAccount("Alice", 1000)
print(f"After deposit: ${acc.deposit(500):,.2f}")

# Google/NumPy/Sphinx styles are all common — pick one per project
