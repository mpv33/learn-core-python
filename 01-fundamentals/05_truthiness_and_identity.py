"""
05 — Truthiness, Identity, and id()
====================================
Critical interview topics: == vs is, truthy/falsy values.
"""

# == compares VALUES | is compares IDENTITY (same object in memory)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")   # True  — same content
print(f"a is b: {a is b}")   # False — different list objects
print(f"a is c: {a is c}")   # True  — c references same object

# Small integer caching (-5 to 256) — interview favorite
x, y = 256, 256
p, q = 257, 257
print(f"\n256 is 256: {x is y}")   # Often True (cached)
print(f"257 is 257: {p is q}")     # May be False (implementation-dependent)

# Truthy / Falsy
FALSY = [None, False, 0, 0.0, "", [], {}, set(), range(0)]
print("\nFalsy values:")
for val in FALSY:
    print(f"  {repr(val):12} → bool = {bool(val)}")

# Short-circuit evaluation
def expensive():
    print("  (expensive called)")
    return True

print("\nShort-circuit AND:")
False and expensive()   # expensive() NOT called
print("Short-circuit OR:")
True or expensive()     # expensive() NOT called

# Walrus operator (Python 3.8+) — assign inside expression
data = ["admin", "user", "guest"]
if (n := len(data)) > 2:
    print(f"\nWalrus: list has {n} items")

# None checks — use `is None`, not `== None`
value = None
print(f"value is None: {value is None}")
