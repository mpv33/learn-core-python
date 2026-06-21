"""
05 — Shallow Copy vs Deep Copy

THEORY
------
What is it?
    Copying in Python has three levels: assignment (same object), shallow copy
    (new outer container, shared inner objects), and deep copy (fully independent
    recursive duplicate). Use copy.copy() for shallow and copy.deepcopy() for deep.

Why it matters
    This is a classic interview topic and a source of subtle bugs. Mutating a
    "copy" that shares inner lists or dicts silently corrupts the original.
    Knowing when to use shallow vs deep copy prevents hard-to-debug data issues.

Key syntax/rules
    - Assignment (b = a) creates a second name for the same object — not a copy
    - Shallow: list.copy(), dict.copy(), copy.copy(obj) — outer container is new
    - Deep: copy.deepcopy(obj) — recursively copies all nested mutable objects
    - Immutable inner objects (int, str, tuple) are safe in shallow copies
    - Nested lists, dicts, and custom objects inside containers are shared in shallow copies

When to use
    - Shallow copy: flat structures or when inner objects should stay shared
    - Deep copy: nested mutable data that must be fully independent (configs, trees)
    - Assignment: intentional aliasing when both names should refer to same object

Common mistakes
    - Thinking .copy() or list[:] creates a fully independent clone of nested data
    - Using deepcopy everywhere — it's slower and can fail on objects with cycles
    - Mutating a shallow copy's inner list and wondering why the original changed
    - Confusing copy with assignment when passing mutable defaults to functions

PRACTICE
--------
Run: python3 core-python/modules/02-data-structures/05_copy_shallow_deep.py
"""

import copy  # provides copy.copy() and copy.deepcopy()


def main() -> None:  # entry point that runs all copy practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Assignment is NOT a copy")  # section title
    print("=" * 50)  # close section header
    original = {"name": "Alice", "scores": [90, 85, 88], "meta": {"active": True}}  # nested mutable dict
    assigned = original  # assigned points to the same object as original
    assigned["name"] = "Bob"  # mutating through assigned also changes original
    print(f"After assignment mutate: original name = {original['name']}")  # both names share data
    original["name"] = "Alice"  # reset name for next demonstration

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Shallow copy shares inner objects")  # section title
    print("=" * 50)  # close section header
    shallow = original.copy()  # new outer dict but inner lists/dicts are shared
    shallow["scores"].append(100)  # appending to inner list affects both copies
    print(f"Shallow copy affects original scores: {original['scores']}")  # demonstrate shared inner list
    shallow["name"] = "Carol"  # replacing top-level key does NOT affect original
    print(f"Shallow name change safe: original={original['name']}, shallow={shallow['name']}")  # top-level is independent

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Deep copy is fully independent")  # section title
    print("=" * 50)  # close section header
    original["scores"] = [90, 85, 88]  # reset scores list before deep copy demo
    deep = copy.deepcopy(original)  # recursively copies all nested objects
    deep["scores"].append(100)  # modify deep copy's inner list
    deep["meta"]["active"] = False  # modify deep copy's inner dict
    print(f"Deep copy — original scores: {original['scores']}")  # original scores unchanged
    print(f"Deep copy — original meta:   {original['meta']}")  # original meta unchanged

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Shallow vs deep on nested lists")  # section title
    print("=" * 50)  # close section header
    list_a = [[1, 2], [3, 4]]  # nested list for list copy demonstration
    list_b = copy.copy(list_a)  # shallow copy of the nested list
    list_b[0].append(99)  # mutating inner list through copy affects original
    print(f"Shallow list copy: list_a = {list_a}")  # show that list_a was affected
    list_c = copy.deepcopy(list_a)  # deep copy creates fully independent structure
    list_c[0].append(999)  # mutating deep copy's inner list does not affect list_a
    print(f"Deep list copy:    list_a = {list_a}")  # list_a unchanged after deep copy mutation

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: safe config override")  # section title
    print("=" * 50)  # close section header
    default_config = {"debug": False, "limits": {"max_retries": 3, "timeout": 30}}  # shared default config
    user_config = copy.deepcopy(default_config)  # deep copy so overrides don't leak back
    user_config["limits"]["max_retries"] = 5  # user raises retry limit
    user_config["debug"] = True  # user enables debug mode
    print(f"Default limits: {default_config['limits']}")  # original config untouched
    print(f"User limits:    {user_config['limits']}")  # user config independently modified

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Rule of thumb")  # section title
    print("=" * 50)  # close section header
    print("Rule: use deepcopy when nested mutable objects must be independent.")  # summary guidance


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all copy practice sections
