"""
11 — __slots__ and Abstract Classes

THEORY
------
What: __slots__ restricts instance attributes to save memory; ABC (Abstract Base Class)
      enforces that subclasses implement required methods via @abstractmethod.
Why:  slots reduce per-instance memory for millions of objects; ABCs define contracts.
Key rules:
  - __slots__ = ("x", "y") — no __dict__ unless " __dict__" added to slots.
  - ABC subclasses must implement all @abstractmethod methods or instantiation fails.
  - Use abc.ABC and @abstractmethod; cannot instantiate ABC directly.
When to use: slots for high-volume value objects; ABC for plugin interfaces and shapes.
Common mistakes: Adding undeclared attributes on slotted classes; forgetting to implement
                 abstract methods in subclass; using ABC when Protocol is enough.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/11_slots_abstract.py
"""

import sys  # import sys for object size inspection
from abc import ABC, abstractmethod  # abstract base class utilities


class Point:  # memory-efficient point using fixed attribute slots
    __slots__ = ("x", "y")  # only x and y may be stored on instances

    def __init__(self, x, y):  # initialize slot attributes
        self.x = x
        self.y = y


class RegularPoint:  # conventional point with dynamic __dict__
    def __init__(self, x, y):  # set arbitrary attributes on instance
        self.x = x
        self.y = y


class Shape(ABC):  # abstract shape requiring area and perimeter
    @abstractmethod
    def area(self) -> float:  # subclasses must implement area()
        pass

    @abstractmethod
    def perimeter(self) -> float:  # subclasses must implement perimeter()
        pass

    def describe(self):  # concrete helper using abstract methods
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


class Rectangle(Shape):  # concrete rectangle implementation
    def __init__(self, w, h):  # store width and height
        self.w = w
        self.h = h

    def area(self):  # compute rectangle area
        return self.w * self.h

    def perimeter(self):  # compute rectangle perimeter
        return 2 * (self.w + self.h)


class Vehicle(ABC):  # abstract vehicle requiring start behavior
    @abstractmethod
    def start(self):  # subclasses must define start()
        pass


class Car(Vehicle):  # concrete car implementation
    def start(self):  # implement required start method
        return "Engine started"


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — __slots__ memory savings")  # section header
    print("=" * 50)  # close header divider
    p = Point(3, 4)  # create slotted point
    print(f"Point: ({p.x}, {p.y})")  # access allowed slot attributes
    print(f"Slots size: {sys.getsizeof(Point(1, 1))} vs Regular: {sys.getsizeof(RegularPoint(1, 1))}")  # compare

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Abstract Base Class")  # section header
    print("=" * 50)  # close header divider
    rect = Rectangle(4, 5)  # create concrete rectangle
    print(f"Rectangle: {rect.describe()}")  # show computed area and perimeter

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Enforced interface")  # section header
    print("=" * 50)  # close header divider
    car = Car()  # instantiate concrete car
    print(f"Car: {car.start()}")  # invoke start behavior


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
