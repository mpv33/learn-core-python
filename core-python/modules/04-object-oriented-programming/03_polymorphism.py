"""
03 — Polymorphism
=================

THEORY
------
What:
  Polymorphism means "many forms" — different classes expose the same interface
  (method name/signature) but provide different implementations. Callers work with
  the interface, not the concrete type.

Why:
  Write flexible code that handles many types through one function or loop without
  long if/elif chains checking every class name.

Key rules:
  - Method overriding: subclass replaces parent behavior with its own version.
  - Duck typing: if an object has the required method, it works — no shared base needed.
  - ABC (`abc.ABC` + `@abstractmethod`) enforces that subclasses implement methods.
  - Type hints like `PaymentProcessor` document expected interfaces.

When to use:
  - Processing a list of mixed types uniformly (shapes, payments, notifications).
  - Plugin/strategy patterns where behavior varies at runtime.
  - Defining contracts that all implementations must follow (ABC).

Common mistakes:
  - Using `isinstance` checks everywhere instead of trusting the shared interface.
  - Forgetting `@abstractmethod` on ABC methods — subclasses won't be forced to implement.
  - Subclassing ABC without implementing all abstract methods — instantiation fails.

PRACTICE
--------
Run: python3 core-python/modules/04-object-oriented-programming/03_polymorphism.py
"""

from abc import ABC, abstractmethod  # tools for abstract base classes


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")  # force override in subclasses


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # store rectangle width
        self.height = height  # store rectangle height

    def area(self):
        return self.width * self.height  # rectangle area formula


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # store circle radius

    def area(self):
        return 3.14159 * self.radius ** 2  # circle area formula


class Duck:
    def quack(self):
        return "Quack!"  # duck quack behavior


class Person:
    def quack(self):
        return "I'm pretending to quack!"  # human mimicking a duck


class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass  # every payment backend must implement process()


class CreditCard(PaymentProcessor):
    def process(self, amount):
        print(f"  Charged ${amount:.2f} to credit card.")  # simulate card charge
        return True  # signal success


class PayPal(PaymentProcessor):
    def process(self, amount):
        print(f"  Paid ${amount:.2f} via PayPal.")  # simulate PayPal payment
        return True  # signal success


def make_it_quack(thing):
    print(f"  {thing.quack()}")  # duck typing — any object with quack() works


def checkout(processor: PaymentProcessor, amount):
    processor.process(amount)  # polymorphic call — works for any PaymentProcessor


def total_area(shapes):
    return sum(s.area() for s in shapes)  # sum areas without knowing concrete types


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Method overriding with mixed shapes")  # label first block
    print("=" * 50)  # close header

    shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 8)]  # list of different shape types
    print("Areas (polymorphic call):")  # label output
    for shape in shapes:  # iterate without caring about concrete class
        print(f"  {type(shape).__name__}: {shape.area():.2f}")  # each shape computes its own area
    print(f"Total area: {total_area(shapes):.2f}")  # aggregate via shared area() interface

    print("\n" + "=" * 50)  # divider before duck typing demo
    print("PRACTICE 2 — Duck typing")  # label second block
    print("=" * 50)  # close header

    make_it_quack(Duck())  # Duck has quack() — works
    make_it_quack(Person())  # Person has quack() — also works, no common base needed

    print("\n" + "=" * 50)  # divider before ABC demo
    print("PRACTICE 3 — Abstract Base Class (ABC)")  # label third block
    print("=" * 50)  # close header

    checkout(CreditCard(), 49.99)  # polymorphic checkout with credit card
    checkout(PayPal(), 29.99)  # same function, different processor implementation
    print(f"CreditCard is PaymentProcessor: {isinstance(CreditCard(), PaymentProcessor)}")  # True


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
