"""02 — Descriptors"""

class ValidatedAttribute:
    """Descriptor that validates on set."""

    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val
        self.name = None

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}")
        setattr(obj, self.name, value)

class Person:
    age = ValidatedAttribute(min_val=0, max_val=150)
    score = ValidatedAttribute(min_val=0, max_val=100)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

p = Person("Alice", 30, 95)
print(f"{p.name}: age={p.age}, score={p.score}")

try:
    p.age = -5
except ValueError as e:
    print(f"Validation caught: {e}")

# Typed descriptor
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name) if obj else self

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        setattr(obj, self.name, value)

class Config:
    port = Typed(int)
    host = Typed(str)

    def __init__(self, host, port):
        self.host = host
        self.port = port

cfg = Config("localhost", 8080)
print(f"\nConfig: {cfg.host}:{cfg.port}")
