"""03 — Typed Classes and Protocols"""

from dataclasses import dataclass
from typing import Protocol, runtime_checkable

@dataclass
class Product:
    id: int
    name: str
    price: float

    def total(self, quantity: int) -> float:
        return self.price * quantity

laptop = Product(1, "Laptop", 999.99)
print(f"{laptop.name}: ${laptop.total(2):,.2f}")

# Protocol — structural typing (duck typing with types)
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Drawing a circle"

class Square:
    def draw(self) -> str:
        return "Drawing a square"

def render(shape: Drawable) -> None:
    print(f"  {shape.draw()}")

render(Circle())
render(Square())
print(f"Circle is Drawable: {isinstance(Circle(), Drawable)}")

# TypedDict — dict with fixed keys
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
    email: str

user: UserDict = {"name": "Alice", "age": 30, "email": "alice@example.com"}
print(f"\nUser: {user['name']}")

# Generic class
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"Stack pop: {int_stack.pop()}")
