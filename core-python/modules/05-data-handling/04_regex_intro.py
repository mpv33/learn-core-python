"""
04 — Regular Expressions (intro)
==================================

THEORY
------
What:
  Regular expressions (regex) describe text patterns. Python's `re` module provides
  functions to search, match, split, and replace strings based on patterns.

Why:
  Validate emails, parse log lines, extract phone numbers, and clean messy text —
  tasks that plain string methods struggle with.

Key rules:
  - `re.findall(pattern, text)` — all non-overlapping matches as a list.
  - `re.search(pattern, text)` — first match anywhere (or None).
  - `re.match(pattern, text)` — match only at the start of the string.
  - `re.fullmatch(pattern, text)` — entire string must match.
  - `re.sub(pattern, repl, text)` — replace matches; use groups with `( )` and `\1`.
  - `re.compile(pattern)` — precompile for reuse (performance in loops).

When to use:
  - Extracting structured data from unstructured text (logs, forms, HTML).
  - Input validation (email, phone, date formats).
  - Bulk find-and-replace with complex rules.

Common mistakes:
  - Overusing regex when simple `.split()` or `.startswith()` would suffice.
  - Forgetting to raw-string patterns — always prefix with r (e.g. r"\\d+").
  - Greedy matching — use `*?` or `+?` for non-greedy when needed.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/04_regex_intro.py
"""

import re  # standard library module for pattern matching


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — findall and search")  # label first block
    print("=" * 50)  # close header

    text = "Contact: alice@example.com or bob@test.org. Phone: 9876543210"  # sample text
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)  # find all email-like strings
    print(f"Emails: {emails}")  # display matched addresses
    match = re.search(r"\d{10}", text)  # find first run of exactly ten digits
    if match:  # proceed only when phone pattern found
        print(f"Phone: {match.group()}")  # print matched substring

    print("\n" + "=" * 50)  # divider before sub demo
    print("PRACTICE 2 — sub and compile")  # label second block
    print("=" * 50)  # close header

    censored = re.sub(r"\d{10}", "XXXXXXXXXX", text)  # mask phone digits
    print(f"Censored: {censored}")  # show text after substitution
    phone_pattern = re.compile(r"(\d{3})(\d{3})(\d{4})")  # precompile with capture groups
    formatted = phone_pattern.sub(r"(\1) \2-\3", "9876543210")  # reformat via backreferences
    print(f"Formatted phone: {formatted}")  # display US-style formatting

    print("\n" + "=" * 50)  # divider before split demo
    print("PRACTICE 3 — split and match vs fullmatch")  # label third block
    print("=" * 50)  # close header

    words = re.split(r"[\s,]+", "apple, banana  cherry   date")  # split on whitespace/commas
    print(f"Split: {words}")  # show token list after regex split
    print(f"match 'Hello': {bool(re.match(r'Hello', 'Hello World'))}")  # True — matches at start
    print(f"fullmatch 'Hello': {bool(re.fullmatch(r'Hello', 'Hello World'))}")  # False — whole string

    print("\n" + "=" * 50)  # divider before groups demo
    print("PRACTICE 4 — Named capture groups")  # label fourth block
    print("=" * 50)  # close header

    log = "2026-06-21 ERROR: Connection failed"  # sample log line
    pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+): (?P<msg>.+)"  # named groups
    m = re.match(pattern, log)  # parse log from the beginning
    if m:  # when parsing succeeds
        print(f"Parsed: date={m['date']}, level={m['level']}, msg={m['msg']}")  # access by name
    url_match = re.search(r"(?P<protocol>https?)://(?P<host>[\w.-]+)", "Visit https://api.example.com")  # URL parse
    if url_match:  # demonstrate another named-group pattern
        print(f"URL: {url_match['protocol']} → {url_match['host']}")  # show extracted parts


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
