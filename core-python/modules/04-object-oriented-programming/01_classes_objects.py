"""
01 — Classes and Objects
========================

THEORY
------
What:
  A class is a blueprint; an object (instance) is a concrete copy with its own
  state (attributes) and behavior (methods). `self` refers to the current instance.

Why:
  Classes group related data and actions, reduce duplication, and model real-world
  entities (users, orders, sensors) in readable, reusable code.

Key rules:
  - `__init__(self, ...)` initializes instance attributes after creation.
  - Instance attributes live on `self`; class attributes are shared by all instances.
  - Methods must accept `self` as the first parameter (except @classmethod / @staticmethod).
  - `@classmethod` receives `cls`; `@staticmethod` needs neither `self` nor `cls`.

When to use:
  - Multiple values and operations belong together (e.g., BankAccount + deposit/withdraw).
  - You need many similar objects with different state (users, products, connections).
  - Shared behavior should be defined once and reused across instances.

Common mistakes:
  - Forgetting `self` in method definitions or when accessing attributes.
  - Using mutable class attributes (lists/dicts) that accidentally share state.
  - Treating class attributes as per-instance storage without assigning on `self`.

PRACTICE
--------
Run: python3 core-python/modules/04-object-oriented-programming/01_classes_objects.py
"""


class Dog:
    """A simple Dog class."""

    species = "Canis familiaris"  # class attribute shared by all Dog instances

    def __init__(self, name, age):
        self.name = name  # instance attribute unique to this dog
        self.age = age  # store age on the instance

    def bark(self):
        return f"{self.name} says Woof!"  # instance method using self.name

    def describe(self):
        return f"{self.name} is {self.age} years old."  # return a summary string


class MathUtils:
    PI = 3.14159  # class-level constant for geometry helpers

    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2  # compute area using class constant PI

    @staticmethod
    def add(a, b):
        return a + b  # plain utility; no access to class or instance state


def main() -> None:
    print("=" * 50)  # print a visual section divider
    print("PRACTICE 1 — Create objects and call methods")  # label first exercise block
    print("=" * 50)  # close the section header

    dog1 = Dog("Buddy", 3)  # instantiate first Dog with name and age
    dog2 = Dog("Max", 5)  # instantiate second Dog with different state
    print(dog1.bark())  # call bark on dog1 — uses dog1's name
    print(dog2.describe())  # call describe on dog2 — uses dog2's attributes
    print(f"Species: {Dog.species}")  # access class attribute via the class itself

    print("\n" + "=" * 50)  # blank line plus divider before next section
    print("PRACTICE 2 — Modify attributes and class vs instance")  # label second block
    print("=" * 50)  # close section header

    dog1.age = 4  # update dog1's age directly on the instance
    print(f"Updated: {dog1.describe()}")  # show description reflects new age
    Dog.trainer = "Alice"  # add class attribute after instances were created
    print(f"dog1 trainer: {dog1.trainer}")  # instance finds trainer via class lookup
    print(f"dog2 trainer: {dog2.trainer}")  # dog2 sees the same class attribute
    print(f"Is Dog? {isinstance(dog1, Dog)}")  # True — dog1 is a Dog instance

    print("\n" + "=" * 50)  # divider before classmethod/staticmethod demo
    print("PRACTICE 3 — @classmethod and @staticmethod")  # label third block
    print("=" * 50)  # close section header

    print(f"Circle area: {MathUtils.circle_area(5):.2f}")  # call class method on MathUtils
    print(f"Add: {MathUtils.add(3, 4)}")  # call static method without an instance

    print("\n" + "=" * 50)  # divider before __dict__ demo
    print("PRACTICE 4 — Inspect instance state with __dict__")  # label fourth block
    print("=" * 50)  # close section header

    print(f"dog1 attributes: {dog1.__dict__}")  # show per-instance attribute dictionary
    print(f"Dog class attrs: {[k for k in Dog.__dict__ if not k.startswith('_')]}")  # list public class names


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
