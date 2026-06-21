"""
05 — Shallow Copy vs Deep Copy
===============================
Critical for interviews and avoiding subtle bugs.
"""

import copy

original = {
    "name": "Alice",
    "scores": [90, 85, 88],
    "meta": {"active": True},
}

# Assignment — NOT a copy (same reference)
assigned = original
assigned["name"] = "Bob"
print(f"After assignment mutate: original name = {original['name']}")

original["name"] = "Alice"  # reset

# Shallow copy — new outer container, shared inner objects
shallow = original.copy()  # or copy.copy(original)
shallow["scores"].append(100)
print(f"Shallow copy affects original scores: {original['scores']}")

# Deep copy — fully independent
original["scores"] = [90, 85, 88]  # reset
deep = copy.deepcopy(original)
deep["scores"].append(100)
deep["meta"]["active"] = False
print(f"Deep copy — original scores: {original['scores']}")
print(f"Deep copy — original meta:   {original['meta']}")

# Lists
list_a = [[1, 2], [3, 4]]
list_b = copy.copy(list_a)
list_b[0].append(99)
print(f"\nShallow list copy: list_a = {list_a}")

list_c = copy.deepcopy(list_a)
list_c[0].append(999)
print(f"Deep list copy:    list_a = {list_a}")

print("\nRule: use deepcopy when nested mutable objects must be independent.")
