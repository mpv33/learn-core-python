"""
08 — Dataclasses

THEORY
------
What: @dataclass auto-generates __init__, __repr__, __eq__, and optional ordering
      from class field annotations.
Why:  Eliminate boilerplate for data-holding classes; cleaner than manual __init__.
Key rules:
  - field(default_factory=list) for mutable defaults — never use mutable default directly.
  - frozen=True makes instances immutable; order=True enables sorting.
  - __post_init__ for validation after auto-generated __init__.
When to use: DTOs, config objects, API responses, replacing simple namedtuples.
Common mistakes: Mutable default without default_factory; forgetting frozen for hashable
                 instances; duplicating validation in __init__ instead of __post_init__.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/08_dataclasses.py
"""

from dataclasses import dataclass, field, asdict  # dataclass tools and dict conversion
from typing import List  # type hint for list fields


@dataclass  # auto-generate __init__, __repr__, and comparison methods
class User:  # user record with defaults and mutable list field
    name: str  # required user name
    age: int  # required user age
    email: str = ""  # optional email defaulting to empty string
    tags: List[str] = field(default_factory=list)  # mutable default via factory

    def greet(self):  # instance method for friendly greeting
        return f"Hi, I'm {self.name}"


@dataclass(frozen=True)  # prevent attribute assignment after creation
class Point:  # immutable 2D point
    x: float  # x coordinate
    y: float  # y coordinate


@dataclass  # mutable product with validation hook
class Product:  # product with non-negative price constraint
    name: str  # product name
    price: float  # product price

    def __post_init__(self):  # run validation after __init__
        if self.price < 0:  # reject negative prices
            raise ValueError("Price cannot be negative")


@dataclass(order=True)  # generate ordering methods from fields
class Score:  # sortable score record (value first for ordering)
    value: int  # numeric score used for ordering
    name: str  # person name


@dataclass  # simple geographic coordinate record
class Coordinate:  # latitude/longitude pair
    lat: float  # latitude
    lon: float  # longitude


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Basic dataclass")  # section header
    print("=" * 50)  # close header divider
    user = User("Alice", 30, "alice@example.com", ["admin", "dev"])  # create sample user
    print(user)  # print auto-generated repr
    print(user.greet())  # call greeting method
    print(f"As dict: {asdict(user)}")  # convert dataclass instance to plain dict

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Frozen dataclass")  # section header
    print("=" * 50)  # close header divider
    p = Point(3.0, 4.0)  # instantiate frozen point
    print(f"Point: {p}")  # display point repr

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — __post_init__ validation")  # section header
    print("=" * 50)  # close header divider
    prod = Product("Laptop", 999.99)  # create valid product
    print(f"Product: {prod}")  # show product instance

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — order=True for sorting")  # section header
    print("=" * 50)  # close header divider
    scores = [Score(85, "Bob"), Score(92, "Alice"), Score(78, "Carol")]  # unsorted scores
    print(f"Sorted: {sorted(scores)}")  # sort by value field automatically

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Coordinate record")  # section header
    print("=" * 50)  # close header divider
    print(f"Coord: {Coordinate(40.7128, -74.0060)}")  # print NYC coordinates


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
