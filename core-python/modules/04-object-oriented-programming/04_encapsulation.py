"""
04 — Encapsulation
==================

THEORY
------
What:
  Encapsulation hides internal state and exposes controlled access through methods
  or properties. Python uses naming conventions and `@property` rather than strict
  private keywords.

Why:
  Protect invariants (balance ≥ 0), validate input before storing, and hide
  implementation details so callers depend on a stable public API.

Key rules:
  - Public: `self.balance` — intended for external use.
  - Protected convention: `self._balance` — "internal, don't touch" signal.
  - Name mangling: `self.__balance` → `_ClassName__balance` (not true security).
  - `@property` / `@setter` provide Pythonic getters and setters with validation.

When to use:
  - Financial or validated fields (bank balance, temperature, age).
  - Computed read-only values (area from radius, full name from parts).
  - Any attribute where direct assignment could break object invariants.

Common mistakes:
  - Relying on `__` mangling for security — it's name obfuscation, not encryption.
  - Accessing `_BankAccount__balance` directly — breaks encapsulation intent.
  - Using `@property` setter without validation — defeats the purpose of encapsulation.

PRACTICE
--------
Run: python3 core-python/modules/04-object-oriented-programming/04_encapsulation.py
"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # public attribute — safe to read from outside
        self.__balance = balance  # mangled name hides balance from casual access

    def deposit(self, amount):
        if amount <= 0:  # reject invalid deposit amounts
            raise ValueError("Deposit must be positive")  # enforce business rule
        self.__balance += amount  # update private balance safely

    def withdraw(self, amount):
        if amount <= 0:  # reject zero or negative withdrawals
            raise ValueError("Withdrawal must be positive")  # enforce business rule
        if amount > self.__balance:  # prevent overdrawing the account
            raise ValueError("Insufficient funds")  # reject when balance too low
        self.__balance -= amount  # subtract after all checks pass

    def get_balance(self):
        return self.__balance  # controlled read access to private balance


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # protected convention — internal storage

    @property
    def celsius(self):
        return self._celsius  # getter — read like a plain attribute

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  # reject below absolute zero
            raise ValueError("Below absolute zero")  # validation on assignment
        self._celsius = value  # store validated value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32  # computed read-only property


class Circle:
    def __init__(self, radius):
        if radius <= 0:  # validate at construction time
            raise ValueError("Radius must be positive")  # reject invalid radius
        self._radius = radius  # protected internal storage

    @property
    def radius(self):
        return self._radius  # read-only — no setter defined

    @property
    def area(self):
        return 3.14159 * self._radius ** 2  # derived value from radius


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Private attributes and controlled methods")  # label first block
    print("=" * 50)  # close header

    account = BankAccount("Alice", 1000)  # create account with initial balance
    account.deposit(500)  # add funds through validated method
    account.withdraw(200)  # remove funds through validated method
    print(f"Balance: ${account.get_balance()}")  # read balance via getter, not direct access
    # print(account.__balance)  # AttributeError — name is mangled
    print(f"Mangled access exists but don't use it: ${account._BankAccount__balance}")  # demo only

    print("\n" + "=" * 50)  # divider before property demo
    print("PRACTICE 2 — @property getter and setter")  # label second block
    print("=" * 50)  # close header

    temp = Temperature(25)  # create temperature at 25°C
    print(f"{temp.celsius}°C = {temp.fahrenheit:.1f}°F")  # read via properties
    temp.celsius = 30  # assignment runs setter validation
    print(f"Updated: {temp.celsius}°C = {temp.fahrenheit:.1f}°F")  # fahrenheit recomputed automatically

    print("\n" + "=" * 50)  # divider before read-only property demo
    print("PRACTICE 3 — Read-only computed properties")  # label third block
    print("=" * 50)  # close header

    c = Circle(5)  # create circle with radius 5
    print(f"Circle r={c.radius}, area={c.area:.2f}")  # radius and area are read-only properties
    c2 = Circle(3)  # second circle for comparison
    print(f"Circle r={c2.radius}, area={c2.area:.2f}")  # area derived from each radius


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
