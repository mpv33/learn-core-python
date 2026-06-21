# Strings

```bash
python3 07-strings/01_string_basics.py
```

## Examples

- `01_string_basics.py`
- `02_string_methods.py`
- `03_string_formatting.py`
- `04_regex_intro.py`

→ [08-files](../08-files/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [08_File Io And Serialization](../08_file_io_and_serialization/)


---

## Interview Prep

### Must-Know Concepts

- immutability
- slicing
- f-strings
- re module
- encoding

### Theory Questions

**Q1: Are strings mutable?**  
A: No. str is immutable.

**Q2: f-string vs .format()?**  
A: f-strings: faster, more readable. Industry standard.

**Q3: Raw string r''?**  
A: Backslashes treated literally. Used for regex patterns.

### Coding Questions

**Valid palindrome**
```python
s = ''.join(c.lower() for c in s if c.isalnum())
return s == s[::-1]
```

### Common Pitfalls

- O(n²) string concatenation with +=
- Confusing re.match vs re.search vs re.fullmatch

