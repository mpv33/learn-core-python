"""04 — Encapsulation"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # name mangling: _BankAccount__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")

# Direct access to mangled name (don't do this in practice)
# print(account.__balance)  # AttributeError
# print(account._BankAccount__balance)  # works but breaks encapsulation

# @property — Pythonic getter/setter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(f"\n{temp.celsius}°C = {temp.fahrenheit:.1f}°F")
temp.celsius = 30
print(f"Updated: {temp.celsius}°C = {temp.fahrenheit:.1f}°F")

# Read-only property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(f"\nCircle r={c.radius}, area={c.area:.2f}")
