"""
02 — String Methods
===================

THEORY
------
What:
  Python strings provide dozens of built-in methods for transforming, searching,
  splitting, and validating text. Methods return new strings (strings are immutable).

Why:
  Avoid reinventing common text operations. Methods like `.strip()`, `.split()`,
  and `.replace()` are readable, tested, and fast.

Key rules:
  - Methods don't modify the original: `text.strip()` returns a new string.
  - Case methods: `.lower()`, `.upper()`, `.title()`, `.capitalize()`.
  - Search: `.find()` returns index or -1; `.count()`, `.startswith()`, `.endswith()`.
  - Split/join: `.split(sep)` → list; `sep.join(list)` → string.
  - Validation: `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()`.

When to use:
  - Cleaning user input (whitespace, case normalization).
  - Parsing CSV-like data, log lines, or filenames.
  - Validating form fields before processing.

Common mistakes:
  - Calling `.strip()` but not assigning the result — original string unchanged.
  - Using `.index()` when input may be missing — raises ValueError (`.find()` is safer).
  - Chaining too many methods without reading intermediate results.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/02_string_methods.py
"""


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Case and whitespace methods")  # label first block
    print("=" * 50)  # close header

    text = "  Hello, World!  "  # sample string with surrounding whitespace
    print(f"Original: '{text}'")  # show untrimmed string in quotes
    print(f"lower: '{text.lower()}'")  # convert all characters to lowercase
    print(f"upper: '{text.upper()}'")  # convert all characters to uppercase
    print(f"title: '{text.strip().title()}'")  # strip then capitalize each word
    print(f"strip: '{text.strip()}'")  # remove leading and trailing whitespace
    print(f"lstrip: '{text.lstrip()}'")  # remove whitespace from left only
    print(f"rstrip: '{text.rstrip()}'")  # remove whitespace from right only

    print("\n" + "=" * 50)  # divider before search demo
    print("PRACTICE 2 — Search and replace")  # label second block
    print("=" * 50)  # close header

    sentence = "Python is great. Python is fun."  # longer string for search demos
    print(f"find('great'): {sentence.find('great')}")  # index of substring or -1
    print(f"find('Java'): {sentence.find('Java')}")  # -1 when not found
    print(f"count('Python'): {sentence.count('Python')}")  # count non-overlapping matches
    print(f"startswith('Python'): {sentence.startswith('Python')}")  # True if begins with prefix
    print(f"endswith('fun.'): {sentence.endswith('fun.')}")  # True if ends with suffix
    print(f"replace: {sentence.replace('Python', 'Java')}")  # swap all occurrences

    print("\n" + "=" * 50)  # divider before split/join demo
    print("PRACTICE 3 — Split, join, and partition")  # label third block
    print("=" * 50)  # close header

    data = "apple,banana,cherry"  # comma-separated values
    fruits = data.split(",")  # break into list at each comma
    print(f"split: {fruits}")  # display resulting list
    print(f"join: {' | '.join(fruits)}")  # rejoin with custom separator
    print(f"partition: {sentence.partition(' is ')}")  # split into (before, sep, after)
    print(f"splitlines: {'line1\\nline2'.splitlines()}")  # split on line boundaries

    print("\n" + "=" * 50)  # divider before alignment demo
    print("PRACTICE 4 — Alignment and validation")  # label fourth block
    print("=" * 50)  # close header

    name = "Python"  # short label for padding demos
    print(f"center: '{name.center(20, '-')}'")  # center within 20 chars, pad with dashes
    print(f"left:   '{name.ljust(20)}'")  # left-align, pad right with spaces
    print(f"right:  '{name.rjust(20)}'")  # right-align, pad left with spaces
    print(f"'123'.isdigit(): {'123'.isdigit()}")  # True when all chars are digits
    print(f"'abc'.isalpha(): {'abc'.isalpha()}")  # True when all chars are letters
    print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # True for letters or digits
    filename = "report.pdf"  # filename with extension
    print(f"removesuffix('.pdf'): {filename.removesuffix('.pdf')}")  # strip suffix if present
    print(f"removeprefix('report'): {filename.removeprefix('report')}")  # strip prefix if present


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
