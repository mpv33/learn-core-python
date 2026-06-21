"""
03 — break, continue, pass
===========================
Control flow inside loops.
"""

# --- break: exit the loop immediately ---
print("Search for 7:")
for num in range(1, 11):
    if num == 7:
        print(f"  Found {num}! Stopping.")
        break
    print(f"  Checking {num}...")

# --- continue: skip to next iteration ---
print("\nOdd numbers only (1-10):")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # skip even numbers
    print(num, end=" ")
print()

# --- pass: placeholder (do nothing) ---
print("\nUsing pass as placeholder:")
for i in range(3):
    pass  # TODO: implement later
print("  Loop ran without error.")

# --- break in nested loops (only breaks inner loop) ---
print("\nFind pair summing to 7:")
pairs = [(1, 6), (2, 5), (3, 4), (1, 1)]
for a, b in pairs:
    if a + b == 7:
        print(f"  Found: ({a}, {b})")
        break

# --- else on loops: runs if loop completes without break ---
print("\nSearch for 99 (not found):")
for num in range(1, 6):
    if num == 99:
        print("Found!")
        break
else:
    print("  99 not found in range 1-5.")

# --- Practical: input validation pattern ---
attempts = 0
max_attempts = 3
correct_pin = "1234"

while attempts < max_attempts:
    pin = "0000"  # Simulated wrong input
    attempts += 1
    if pin == correct_pin:
        print(f"\nPIN accepted on attempt {attempts}.")
        break
    print(f"  Wrong PIN. Attempt {attempts}/{max_attempts}.")
else:
    print("  Account locked.")
