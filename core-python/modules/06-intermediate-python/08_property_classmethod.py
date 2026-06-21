"""
08 — property, classmethod, staticmethod

THEORY
------
What: Descriptors and decorators that control attribute access and define alternative
      constructors (classmethod) or utility methods (staticmethod).
Why:  Encapsulate validation, computed attributes, and factory methods cleanly.
Key rules:
  - @property: getter; add @name.setter for validated writes.
  - @classmethod: first arg is cls — use for alternative constructors.
  - @staticmethod: no implicit cls/self — pure utility on the class namespace.
When to use: Validated attributes, computed fields, from_string()/today() factories.
Common mistakes: Using staticmethod when cls is needed; heavy logic in property getters;
                 forgetting setter validation mirrors __init__ validation.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/08_property_classmethod.py
"""


class Circle:  # geometry helper demonstrating @property
    def __init__(self, radius: float):  # initialize with radius
        self._radius = radius  # private backing field for radius

    @property
    def radius(self):  # read-only accessor unless setter is defined
        return self._radius  # expose stored radius

    @radius.setter
    def radius(self, value: float):  # validate writes to radius
        if value < 0:  # reject invalid geometry
            raise ValueError("Radius cannot be negative")  # guard against negative radius
        self._radius = value  # update backing field

    @property
    def diameter(self):  # computed attribute from radius
        return self._radius * 2  # diameter is twice radius

    @property
    def area(self):  # computed read-only attribute
        return 3.14159 * self._radius ** 2  # approximate circle area


class Date:  # date value object with alternative constructors
    def __init__(self, year: int, month: int, day: int):  # primary constructor
        self.year = year  # store year component
        self.month = month  # store month component
        self.day = day  # store day component

    @classmethod
    def from_string(cls, date_str: str):  # parse ISO-like date string
        year, month, day = map(int, date_str.split("-"))  # split and convert parts to int
        return cls(year, month, day)  # construct instance via cls(...)

    @classmethod
    def today(cls):  # factory for current local date
        from datetime import date  # import inside method to defer dependency
        d = date.today()  # get today's date
        return cls(d.year, d.month, d.day)  # build Date from today's components

    def __repr__(self):  # developer-friendly string form
        return f"Date({self.year}-{self.month:02d}-{self.day:02d})"  # zero-pad month/day


class Math:  # utility namespace for math helpers
    @staticmethod
    def is_even(n: int) -> bool:  # parity check without instance or class state
        return n % 2 == 0  # True when divisible by 2

    @staticmethod
    def clamp(value: float, min_val: float, max_val: float) -> float:  # bound to range
        return max(min_val, min(value, max_val))  # lower-bound then upper-bound


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — @property with setter")  # section header
    print("=" * 50)  # close header divider
    c = Circle(5)  # create circle with radius 5
    print(f"r={c.radius}, d={c.diameter}, area={c.area:.2f}")  # access properties like attributes
    c.radius = 10  # use setter to change radius
    print(f"Updated area: {c.area:.2f}")  # derived area updates automatically

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — @classmethod factories")  # section header
    print("=" * 50)  # close header divider
    d1 = Date.from_string("2026-06-21")  # alternate constructor from string
    d2 = Date.today()  # alternate constructor for today
    print(f"{d1}, {d2}")  # show both Date instances

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — @staticmethod utilities")  # section header
    print("=" * 50)  # close header divider
    print(f"is_even(4): {Math.is_even(4)}")  # call static method on class
    print(f"clamp(15, 0, 10): {Math.clamp(15, 0, 10)}")  # clamp 15 into [0, 10]


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
