"""04 — property, classmethod, staticmethod"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(f"r={c.radius}, d={c.diameter}, area={c.area:.2f}")
c.radius = 10
print(f"Updated area: {c.area:.2f}")

# classmethod — receives class as first arg
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        from datetime import date
        d = date.today()
        return cls(d.year, d.month, d.day)

    def __repr__(self):
        return f"Date({self.year}-{self.month:02d}-{self.day:02d})"

d1 = Date.from_string("2026-06-21")
d2 = Date.today()
print(f"\n{d1}, {d2}")

# staticmethod — no implicit first argument
class Math:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def clamp(value, min_val, max_val):
        return max(min_val, min(value, max_val))

print(f"is_even(4): {Math.is_even(4)}")
print(f"clamp(15, 0, 10): {Math.clamp(15, 0, 10)}")
