# Files

```bash
python3 08-files/01_read_write_text.py
```

## Examples

- `01_read_write_text.py`
- `02_json_files.py`
- `03_csv_files.py`
- `04_path_handling.py`

→ [09-exceptions](../09-exceptions/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [09_Exceptions And Logging](../09_exceptions_and_logging/)


---

## Interview Prep

### Must-Know Concepts

- with statement
- text vs binary mode
- JSON
- CSV
- pathlib

### Theory Questions

**Q1: Why use with open()?**  
A: Ensures file closed even on exception.

**Q2: JSON serializable types?**  
A: dict, list, str, int, float, bool, None.

**Q3: pathlib vs os.path?**  
A: pathlib: OOP paths, cross-platform. Industry preferred.

### Coding Questions


### Common Pitfalls

- Not specifying encoding='utf-8'
- Not using newline='' for csv on Windows

