"""02 — Inheritance"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def info(self):
        return f"I am {self.name}"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)  # call parent __init__
        self.owner = owner

    def guide(self):
        return f"{self.name} is guiding {self.owner}"

dog = Dog("Buddy")
cat = Cat("Whiskers")
guide = GuideDog("Rex", "Alice")

print(dog.speak())
print(cat.speak())
print(guide.guide())

# Method Resolution Order (MRO)
print(f"\nGuideDog MRO: {[c.__name__ for c in GuideDog.__mro__]}")

# isinstance and issubclass
print(f"GuideDog is Dog: {isinstance(guide, Dog)}")
print(f"Dog is Animal: {issubclass(Dog, Animal)}")

# Override and extend parent method
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_pay(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_pay(self):
        return super().annual_pay() + self.bonus

mgr = Manager("Alice", 8000, 20000)
print(f"\n{mgr.name} annual pay: ${mgr.annual_pay():,}")
