# Module 04 — Interview Prep: Object-Oriented Programming

> Classes, inheritance, polymorphism, encapsulation, magic methods

---

## Theory Questions

**Q1: Four pillars of OOP?**  
Encapsulation, Abstraction, Inheritance, Polymorphism.

**Q2: `__init__` vs `__new__`?**  
`__new__` creates instance (classmethod). `__init__` initializes it. `__new__` used for singletons, immutable types.

**Q3: What is MRO?**  
Method Resolution Order — C3 linearization determining search order for inherited methods. View: `ClassName.__mro__`.

**Q4: `@classmethod` vs `@staticmethod` vs `@property`?**  
classmethod: gets `cls`, factory methods. staticmethod: no implicit args. property: computed attribute with getter/setter.

**Q5: Composition vs inheritance?**  
Prefer composition ("has-a") over deep inheritance ("is-a") for flexibility and loose coupling.

**Q6: What is polymorphism?**  
Same interface, different behavior. Method overriding in subclasses or duck typing.

**Q7: Duck typing?**  
"If it walks like a duck and quacks like a duck, it's a duck." Type determined by behavior, not explicit inheritance.

**Q8: What is encapsulation?**  
Hide internal state, expose via methods/properties. `_prefix` convention for "private". `__name` mangling for stronger hiding.

**Q9: Abstract Base Class (ABC)?**  
Class with `@abstractmethod` that cannot be instantiated. Enforces interface on subclasses.

**Q10: `self` in Python?**  
Explicit reference to instance. Must be first parameter of instance methods (by convention named `self`).

**Q11: Multiple inheritance in Python?**  
Supported. MRO resolves diamond problem via C3 linearization.

**Q12: What are magic/dunder methods?**  
`__str__`, `__repr__`, `__add__`, `__len__`, etc. Define behavior for built-in operations.

**Q13: `__str__` vs `__repr__`?**  
`__str__`: human-readable (for users). `__repr__`: unambiguous (for developers/debugging). Goal: `eval(repr(obj)) == obj`.

**Q14: Class attribute vs instance attribute?**  
Class attribute shared by all instances. Instance attribute unique per object. Instance shadows class attribute.

**Q15: What is `@dataclass`?**  
Decorator auto-generating `__init__`, `__repr__`, `__eq__` for data-holding classes.

**Q16: SOLID principles?**  
Single responsibility, Open/closed, Liskov substitution, Interface segregation, Dependency inversion.

**Q17: What is method overriding?**  
Subclass provides its own implementation of parent method. Use `super()` to call parent version.

**Q18: Can you override `__init__` without calling super?**  
Yes, but you may skip parent initialization. Usually call `super().__init__()`.

---

## Coding Questions

**Q19: Implement Stack class**
```python
class Stack:
    def __init__(self):
        self._items = []
    def push(self, item):
        self._items.append(item)
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
```

**Q20: Implement Queue using deque**
```python
from collections import deque
class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, item):
        self._items.append(item)
    def dequeue(self):
        return self._items.popleft()
```

**Q21: Singleton pattern**
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Q22: Property with validation**
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value
```

**Q23: Bank account with encapsulation**
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("Invalid amount")
        self._balance += amount
    def withdraw(self, amount):
        if amount > self._balance: raise ValueError("Insufficient funds")
        self._balance -= amount
    @property
    def balance(self):
        return self._balance
```

**Q24: Vector with operator overloading**
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

---

## Common Pitfalls

- Not calling `super().__init__()`
- Deep inheritance hierarchies
- Accessing `__mangled` names directly
- Confusing class vs instance attributes
- God classes with too many responsibilities

---

## Quick Checklist

- [ ] Explain MRO with diamond inheritance example
- [ ] Difference classmethod/staticmethod/property
- [ ] Implement Stack class from memory
- [ ] Explain composition vs inheritance
- [ ] List 5 common dunder methods and purpose
