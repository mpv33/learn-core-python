"""01 — Dataclasses"""

from dataclasses import dataclass, field, asdict
from typing import List

@dataclass
class User:
    name: str
    age: int
    email: str = ""
    tags: List[str] = field(default_factory=list)

    def greet(self):
        return f"Hi, I'm {self.name}"

user = User("Alice", 30, "alice@example.com", ["admin", "dev"])
print(user)
print(user.greet())
print(f"As dict: {asdict(user)}")

# frozen dataclass (immutable)
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
print(f"\nPoint: {p}")

# post_init for validation
@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

prod = Product("Laptop", 999.99)
print(f"Product: {prod}")

# order=True enables comparison
@dataclass(order=True)
class Score:
    value: int
    name: str

scores = [Score(85, "Bob"), Score(92, "Alice"), Score(78, "Carol")]
print(f"\nSorted: {sorted(scores)}")

# Replace namedtuple in most cases
@dataclass
class Coordinate:
    lat: float
    lon: float

print(f"Coord: {Coordinate(40.7128, -74.0060)}")
