"""01 — Classes and Objects"""

class Dog:
    """A simple Dog class."""

    species = "Canis familiaris"  # class attribute (shared)

    def __init__(self, name, age):
        self.name = name            # instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."

# Create objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.describe())
print(f"Species: {Dog.species}")

# Modify attributes
dog1.age = 4
print(f"Updated: {dog1.describe()}")

# Class vs instance attribute
Dog.trainer = "Alice"
print(f"dog1 trainer: {dog1.trainer}")
print(f"dog2 trainer: {dog2.trainer}")

# isinstance check
print(f"Is Dog? {isinstance(dog1, Dog)}")

# Class method and static method
class MathUtils:
    PI = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2

    @staticmethod
    def add(a, b):
        return a + b

print(f"\nCircle area: {MathUtils.circle_area(5):.2f}")
print(f"Add: {MathUtils.add(3, 4)}")
