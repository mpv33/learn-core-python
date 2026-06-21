"""
11 — Typed Classes and Protocols

THEORY
------
What: Type-safe class design using dataclasses, Protocol (structural typing), TypedDict,
      and Generic classes with TypeVar.
Why:  Document data shapes, enable duck typing with static checks, and build reusable containers.
Key rules:
  - Protocol: define required methods; @runtime_checkable enables isinstance checks.
  - TypedDict: dict with fixed keys for static checkers (still a dict at runtime).
  - Generic[T]: parameterize classes like Stack[int] for type-safe containers.
When to use: Data records, plugin interfaces, API response schemas, reusable collections.
Common mistakes: Confusing Protocol with ABC (inheritance vs structure); TypedDict optional
                 keys require total=False; forgetting to specialize Generic types.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/11_typed_classes.py
"""

from dataclasses import dataclass  # generate boilerplate for data-holding classes
from typing import Protocol, runtime_checkable, TypedDict, TypeVar, Generic  # typing tools


@dataclass
class Product:  # immutable-style product record with generated methods
    id: int  # product identifier
    name: str  # display name
    price: float  # unit price

    def total(self, quantity: int) -> float:  # compute line total for quantity
        return self.price * quantity  # multiply unit price by count


@runtime_checkable
class Drawable(Protocol):  # anything with draw() matches this interface
    def draw(self) -> str: ...  # required method signature


class Circle:  # concrete shape without inheriting Drawable
    def draw(self) -> str:  # satisfies Drawable structurally
        return "Drawing a circle"  # circle-specific message


class Square:  # another shape implementing draw()
    def draw(self) -> str:  # same method name and return type
        return "Drawing a square"  # square-specific message


def render(shape: Drawable) -> None:  # accept any object matching Drawable
    print(f"  {shape.draw()}")  # call draw without knowing concrete class


class UserDict(TypedDict):  # required keys and value types for user records
    name: str  # user's name
    age: int  # user's age
    email: str  # user's email address


T = TypeVar("T")  # generic type variable for stack element type


class Stack(Generic[T]):  # stack holding items of type T
    def __init__(self) -> None:  # initialize empty storage
        self._items: list[T] = []  # internal list typed as list[T]

    def push(self, item: T) -> None:  # add item of type T
        self._items.append(item)  # append to end of list

    def pop(self) -> T:  # remove and return top item
        return self._items.pop()  # LIFO removal


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Typed dataclass")  # section header
    print("=" * 50)  # close header divider
    laptop = Product(1, "Laptop", 999.99)  # instantiate sample product
    print(f"{laptop.name}: ${laptop.total(2):,.2f}")  # show total for two units

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Protocol (structural typing)")  # section header
    print("=" * 50)  # close header divider
    render(Circle())  # Circle is acceptable because it has draw()
    render(Square())  # Square is also acceptable
    print(f"Circle is Drawable: {isinstance(Circle(), Drawable)}")  # runtime_checkable check

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — TypedDict")  # section header
    print("=" * 50)  # close header divider
    user: UserDict = {"name": "Alice", "age": 30, "email": "alice@example.com"}  # conforming dict
    print(f"User: {user['name']}")  # access typed key

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Generic class")  # section header
    print("=" * 50)  # close header divider
    int_stack: Stack[int] = Stack()  # stack specialized for integers
    int_stack.push(1)  # push first value
    int_stack.push(2)  # push second value
    print(f"Stack pop: {int_stack.pop()}")  # pop returns most recently pushed item (2)


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
