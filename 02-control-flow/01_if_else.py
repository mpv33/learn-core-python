"""
01 — if / elif / else
======================
Execute code only when conditions are True.
"""

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")

# --- Nested if ---
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You may enter.")
    else:
        print("You need a ticket.")
else:
    print("You must be 18+.")

# --- Ternary (one-line conditional) ---
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# --- Multiple conditions ---
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Login successful!")
elif username == "admin":
    print("Wrong password.")
else:
    print("Unknown user.")

# --- Truthy / Falsy ---
values = [0, 1, "", "hello", [], [1], None]
for v in values:
    print(f"  {repr(v):10} → {'Truthy' if v else 'Falsy'}")
