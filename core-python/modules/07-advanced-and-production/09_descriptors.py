"""
09 — Descriptors

THEORY
------
What: Descriptors implement __get__, __set__, or __delete__ and control attribute access
      on host classes — the mechanism behind @property, methods, and staticmethods.
Why:  Reusable validated or typed attributes without repeating logic in every setter.
Key rules:
  - __set_name__(self, owner, name) receives the attribute name at class creation.
  - Store values on the instance as _name (private backing attribute).
  - Data descriptor (__set__ defined) takes priority over instance __dict__.
When to use: Validated fields, typed attributes, lazy computed properties, ORMs.
Common mistakes: Forgetting __set_name__; storing value on descriptor instead of instance;
                 infinite recursion by using self.name instead of self._name in __set__.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/09_descriptors.py
"""


class ValidatedAttribute:  # descriptor that validates values on assignment
    def __init__(self, min_val=None, max_val=None):  # store optional numeric bounds
        self.min_val = min_val
        self.max_val = max_val
        self.name = None  # backing attribute name set by __set_name__

    def __set_name__(self, owner, name):  # record private storage attribute name
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):  # retrieve stored value from instance
        if obj is None:  # accessed on class — return descriptor itself
            return self
        return getattr(obj, self.name, None)  # read private backing attribute

    def __set__(self, obj, value):  # validate then store new value
        if self.min_val is not None and value < self.min_val:  # enforce minimum bound
            raise ValueError(f"{self.name} must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:  # enforce maximum bound
            raise ValueError(f"{self.name} must be <= {self.max_val}")
        setattr(obj, self.name, value)  # write validated value to backing field


class Person:  # model with validated age and score descriptors
    age = ValidatedAttribute(min_val=0, max_val=150)  # age must be 0–150
    score = ValidatedAttribute(min_val=0, max_val=100)  # score must be 0–100

    def __init__(self, name, age, score):  # initialize person attributes
        self.name = name
        self.age = age  # triggers ValidatedAttribute.__set__
        self.score = score


class Typed:  # descriptor enforcing a specific Python type
    def __init__(self, expected_type):  # store required type
        self.expected_type = expected_type
        self.name = None  # backing attribute name

    def __set_name__(self, owner, name):  # set private storage attribute name
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):  # fetch stored value
        return getattr(obj, self.name) if obj else self  # return descriptor on class access

    def __set__(self, obj, value):  # enforce isinstance before assignment
        if not isinstance(value, self.expected_type):  # reject wrong types
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        setattr(obj, self.name, value)  # store type-validated value


class Config:  # configuration object with typed fields
    port = Typed(int)  # port must be int
    host = Typed(str)  # host must be str

    def __init__(self, host, port):  # initialize typed config values
        self.host = host
        self.port = port


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Validated descriptor")  # section header
    print("=" * 50)  # close header divider
    p = Person("Alice", 30, 95)  # create valid person instance
    print(f"{p.name}: age={p.age}, score={p.score}")  # read descriptor-backed fields

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Validation failure")  # section header
    print("=" * 50)  # close header divider
    try:  # demonstrate validation failure
        p.age = -5  # invalid age should raise ValueError
    except ValueError as e:  # catch expected validation error
        print(f"Validation caught: {e}")

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Typed descriptor")  # section header
    print("=" * 50)  # close header divider
    cfg = Config("localhost", 8080)  # create valid configuration
    print(f"Config: {cfg.host}:{cfg.port}")  # display host and port


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
