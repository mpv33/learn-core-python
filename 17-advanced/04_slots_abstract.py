"""04 — __slots__ and Abstract Classes"""

# __slots__ — restrict attributes, save memory
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(f"Point: ({p.x}, {p.y})")
# p.z = 5  # AttributeError — not in __slots__

import sys
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(f"Slots size: {sys.getsizeof(Point(1,1))} vs Regular: {sys.getsizeof(RegularPoint(1,1))}")

# Abstract Base Class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self):
        return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# shape = Shape()  # TypeError — can't instantiate ABC
rect = Rectangle(4, 5)
print(f"\nRectangle: {rect.describe()}")

# Enforce interface with @abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Engine started"

car = Car()
print(f"Car: {car.start()}")
