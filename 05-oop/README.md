# OOP

```bash
python3 05-oop/01_classes_objects.py
```

## Examples

- `01_classes_objects.py`
- `02_inheritance.py`
- `03_polymorphism.py`
- `04_encapsulation.py`
- `05_magic_methods.py`

→ [06-modules](../06-modules/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [06_Modules And Packages](../06_modules_and_packages/)


---

## Interview Prep

### Must-Know Concepts

- class/instance
- inheritance
- polymorphism
- encapsulation
- MRO
- dunder methods

### Theory Questions

**Q1: __init__ vs __new__?**  
A: __new__ creates instance. __init__ initializes it.

**Q2: MRO?**  
A: Method Resolution Order — C3 linearization for inherited methods.

**Q3: classmethod vs staticmethod?**  
A: classmethod gets cls. staticmethod gets no implicit args.

**Q4: Composition vs Inheritance?**  
A: Prefer composition (has-a) over deep inheritance (is-a).

### Coding Questions

**Stack class**
```python
class Stack:
    def __init__(self): self._items = []
    def push(self, x): self._items.append(x)
    def pop(self): return self._items.pop()
```

### Common Pitfalls

- Deep inheritance hierarchies
- Not calling super().__init__()
- Accessing private attrs via name mangling

