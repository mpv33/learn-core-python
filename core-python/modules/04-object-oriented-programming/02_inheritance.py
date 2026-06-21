"""
02 — Inheritance
================

THEORY
------
What:
  Inheritance lets a child class reuse and extend a parent class. The child gets
  parent attributes/methods and can override or add behavior. `super()` calls
  the parent implementation.

Why:
  Avoid duplicating shared logic, express "is-a" relationships (Dog is an Animal),
  and build layered APIs (Employee → Manager) with specialized behavior.

Key rules:
  - Syntax: `class Child(Parent):` — put the base class in parentheses.
  - Override methods by defining the same name in the child class.
  - Call `super().__init__(...)` in the child constructor to initialize parent state.
  - MRO (Method Resolution Order) determines which method Python calls first.

When to use:
  - Several classes share common fields or methods (Animal → Dog, Cat).
  - You need specialization layers (Employee → Manager → Director).
  - Frameworks expect subclassing (e.g., Django models, custom exceptions).

Common mistakes:
  - Forgetting `super().__init__()` so parent attributes are never set.
  - Overriding without calling `super()` when you want to extend, not replace.
  - Deep inheritance trees that are hard to follow — prefer composition when shallow reuse suffices.

PRACTICE
--------
Run: python3 core-python/modules/04-object-oriented-programming/02_inheritance.py
"""


class Animal:
    def __init__(self, name):
        self.name = name  # store animal name on the instance

    def speak(self):
        return "..."  # default speak — subclasses override this

    def info(self):
        return f"I am {self.name}"  # shared description for all animals


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"  # override parent speak for dogs


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"  # override parent speak for cats


class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)  # initialize name via Dog → Animal chain
        self.owner = owner  # add guide-dog-specific attribute

    def guide(self):
        return f"{self.name} is guiding {self.owner}"  # behavior unique to GuideDog


class Employee:
    def __init__(self, name, salary):
        self.name = name  # employee display name
        self.salary = salary  # monthly salary amount

    def annual_pay(self):
        return self.salary * 12  # base annual pay is 12 months of salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  # reuse Employee initialization
        self.bonus = bonus  # manager-specific annual bonus

    def annual_pay(self):
        return super().annual_pay() + self.bonus  # extend parent pay with bonus


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Single-level inheritance and overriding")  # label first block
    print("=" * 50)  # close header

    dog = Dog("Buddy")  # Dog inherits name from Animal
    cat = Cat("Whiskers")  # Cat inherits name from Animal
    print(dog.speak())  # Dog's overridden speak
    print(cat.speak())  # Cat's overridden speak
    print(dog.info())  # inherited info() from Animal

    print("\n" + "=" * 50)  # divider before multi-level demo
    print("PRACTICE 2 — Multi-level inheritance and super()")  # label second block
    print("=" * 50)  # close header

    guide = GuideDog("Rex", "Alice")  # GuideDog → Dog → Animal
    print(guide.guide())  # GuideDog-specific method
    print(guide.speak())  # inherited overridden speak from Dog
    print(f"GuideDog MRO: {[c.__name__ for c in GuideDog.__mro__]}")  # method lookup order

    print("\n" + "=" * 50)  # divider before isinstance demo
    print("PRACTICE 3 — isinstance and issubclass")  # label third block
    print("=" * 50)  # close header

    print(f"GuideDog is Dog: {isinstance(guide, Dog)}")  # True — subclass instance is also parent type
    print(f"GuideDog is Animal: {isinstance(guide, Animal)}")  # True — transitive inheritance
    print(f"Dog is Animal: {issubclass(Dog, Animal)}")  # True — Dog class inherits from Animal
    print(f"Cat is Dog: {issubclass(Cat, Dog)}")  # False — unrelated branches

    print("\n" + "=" * 50)  # divider before extend-vs-override demo
    print("PRACTICE 4 — Extend parent method with super()")  # label fourth block
    print("=" * 50)  # close header

    mgr = Manager("Alice", 8000, 20000)  # manager with monthly salary and bonus
    emp = Employee("Bob", 5000)  # regular employee for comparison
    print(f"{mgr.name} annual pay: ${mgr.annual_pay():,}")  # salary×12 + bonus
    print(f"{emp.name} annual pay: ${emp.annual_pay():,}")  # salary×12 only


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
