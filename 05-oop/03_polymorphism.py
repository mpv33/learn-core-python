"""03 — Polymorphism"""

# Method overriding — subclasses provide their own implementation
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 8)]

print("Areas (polymorphic call):")
for shape in shapes:
    print(f"  {type(shape).__name__}: {shape.area():.2f}")

# Duck typing — "If it walks like a duck and quacks like a duck..."
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm pretending to quack!"

def make_it_quack(thing):
    print(f"  {thing.quack()}")

make_it_quack(Duck())
make_it_quack(Person())

# Abstract Base Class — enforce interface
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass

class CreditCard(PaymentProcessor):
    def process(self, amount):
        print(f"  Charged ${amount:.2f} to credit card.")
        return True

class PayPal(PaymentProcessor):
    def process(self, amount):
        print(f"  Paid ${amount:.2f} via PayPal.")
        return True

def checkout(processor: PaymentProcessor, amount):
    processor.process(amount)

checkout(CreditCard(), 49.99)
checkout(PayPal(), 29.99)
