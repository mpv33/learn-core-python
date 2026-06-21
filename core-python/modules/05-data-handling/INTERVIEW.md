# Module 05 — Interview Prep: Data Handling

> Strings, files, JSON/CSV, exceptions, logging

---

## Theory Questions

**Q1: Are strings mutable in Python?**  
No. `str` is immutable. All string methods return new strings.

**Q2: f-string vs `.format()` vs `%`?**  
f-strings (3.6+): fastest, most readable. Industry standard. Support expressions: `f"{x=}"`.

**Q3: Raw string `r"..."`?**  
Backslashes treated literally. Used for regex patterns and Windows paths.

**Q4: `re.match` vs `re.search` vs `re.fullmatch`?**  
match: start of string. search: anywhere. fullmatch: entire string must match.

**Q5: Why use `with open()`?**  
Context manager ensures file closed even on exception. Prevents resource leaks.

**Q6: Text mode vs binary mode?**  
Text: str, encoding applied. Binary: bytes, no encoding. Use `'rb'`/`'wb'` for images, etc.

**Q7: JSON serializable types?**  
dict, list, str, int, float, bool, None. NOT: datetime, set, custom objects (need `default` handler).

**Q8: Why `encoding='utf-8'`?**  
Explicit encoding prevents platform-dependent defaults. UTF-8 is universal standard.

**Q9: `pathlib` vs `os.path`?**  
pathlib: OOP, cross-platform, readable. Preferred in modern Python.

**Q10: Exception hierarchy?**  
BaseException → Exception → (ValueError, TypeError, KeyError, IOError, etc.). Catch specific, not bare `except`.

**Q11: try/except/else/finally order?**  
try → except (on error) → else (if no error) → finally (always).

**Q12: `raise from` purpose?**  
Exception chaining — preserves original cause in `__cause__`.

**Q13: Custom exception best practice?**  
Inherit from `Exception`. Create hierarchy with base app exception.

**Q14: logging levels?**  
DEBUG < INFO < WARNING < ERROR < CRITICAL. Production typically INFO or WARNING.

**Q15: logging vs print?**  
logging: levels, handlers, rotation, production-ready. print: debugging only.

**Q16: CSV `newline=''` on Windows?**  
Prevents double newlines when writing CSV files.

**Q17: What is `assert`?**  
Debug check. Disabled with `python -O`. Not for production validation.

**Q18: Bare `except:` problem?**  
Catches everything including KeyboardInterrupt, SystemExit. Always catch specific exceptions.

---

## Coding Questions

**Q19: Valid palindrome**
```python
def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

**Q20: Reverse words in sentence**
```python
def reverse_words(s):
    return " ".join(s.split()[::-1])
```

**Q21: Count word frequency**
```python
from collections import Counter
def word_freq(text):
    return Counter(text.lower().split())
```

**Q22: Read JSON safely**
```python
import json
from pathlib import Path
def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
```

**Q23: Write CSV from dicts**
```python
import csv
def write_csv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
```

**Q24: Custom exception hierarchy**
```python
class AppError(Exception): pass
class ValidationError(AppError):
    def __init__(self, field, msg):
        self.field = field
        super().__init__(f"{field}: {msg}")
```

**Q25: Retry with exception handling**
```python
def parse_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
```

**Q26: Extract emails with regex**
```python
import re
def find_emails(text):
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
```

**Q27: Setup logger**
```python
import logging
logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
logger.info("Application started")
```

---

## Common Pitfalls

- String concatenation with `+=` in loop (O(n²))
- Not closing files (use `with`)
- Bare except swallowing errors
- Using print in production
- Not handling JSON decode errors

---

## Quick Checklist

- [ ] Write palindrome check from memory
- [ ] Explain try/except/else/finally flow
- [ ] Read/write JSON and CSV
- [ ] Explain logging levels
- [ ] Difference re.match vs re.search
