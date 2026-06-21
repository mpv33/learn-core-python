# Advanced

```bash
python3 17-advanced/01_dataclasses.py
```

## Examples

- `01_dataclasses.py`
- `02_descriptors.py`
- `03_metaclasses_intro.py`
- `04_slots_abstract.py`

→ [18-performance](../18-performance/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [18_Performance And Memory](../18_performance_and_memory/)


---

## Interview Prep

### Must-Know Concepts

- dataclass
- descriptor
- metaclass
- slots
- ABC

### Theory Questions

**Q1: Descriptor?**  
A: Object with get/set controlling attribute access.

**Q2: Metaclass?**  
A: Class of a class. type is default.

**Q3: __slots__?**  
A: Restricts attributes, saves memory, no __dict__.

### Coding Questions


### Common Pitfalls

- Overusing metaclasses
- dataclass mutable default without default_factory

