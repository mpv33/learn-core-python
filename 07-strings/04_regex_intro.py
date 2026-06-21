"""04 — Regular Expressions (intro)"""

import re

text = "Contact: alice@example.com or bob@test.org. Phone: 9876543210"

# findall — all matches
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
print(f"Emails: {emails}")

# search — first match
match = re.search(r"\d{10}", text)
if match:
    print(f"Phone: {match.group()}")

# sub — replace
censored = re.sub(r"\d{10}", "XXXXXXXXXX", text)
print(f"Censored: {censored}")

# compile for reuse
phone_pattern = re.compile(r"(\d{3})(\d{3})(\d{4})")
formatted = phone_pattern.sub(r"(\1) \2-\3", "9876543210")
print(f"Formatted phone: {formatted}")

# split
words = re.split(r"[\s,]+", "apple, banana  cherry   date")
print(f"Split: {words}")

# match vs fullmatch
print(f"match 'Hello': {bool(re.match(r'Hello', 'Hello World'))}")
print(f"fullmatch 'Hello': {bool(re.fullmatch(r'Hello', 'Hello World'))}")

# Groups
log = "2026-06-21 ERROR: Connection failed"
pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+): (?P<msg>.+)"
m = re.match(pattern, log)
if m:
    print(f"Parsed: date={m['date']}, level={m['level']}, msg={m['msg']}")
