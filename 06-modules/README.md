# Modules

```bash
python3 06-modules/01_imports.py
```

## Examples

- `01_imports.py`
- `02_use_local_module.py`
- `03_name_main.py`

→ [07-strings](../07-strings/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [07_Strings And Regex](../07_strings_and_regex/)


---

## Interview Prep

### Must-Know Concepts

- import system
- __name__
- __init__.py
- relative imports
- sys.path

### Theory Questions

**Q1: if __name__ == '__main__'?**  
A: Block runs only when file executed directly, not when imported.

**Q2: Package vs Module?**  
A: Module: single .py file. Package: directory with __init__.py.

**Q3: Relative import?**  
A: from .utils import helper — requires package context.

### Coding Questions


### Common Pitfalls

- Circular imports
- Wildcard import (from x import *)
- Running module with relative imports directly

