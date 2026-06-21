"""
01 — List Comprehensions

THEORY
------
What: A concise syntax to build lists by evaluating an expression for each item in an
      iterable, optionally filtering with an if clause.
Why:  Replaces verbose for-loops with readable one-liners; often faster than append loops.
Key rules:
  - Syntax: [expr for item in iterable] or [expr for item in iterable if condition]
  - If-else must come BEFORE for: [a if cond else b for x in items]
  - Keep each comprehension on one readable line; split complex logic into a loop.
When to use: Simple transforms, filters, and flat-mapping; prefer loops for side effects
             or deeply nested logic.
Common mistakes: Side effects inside comprehensions; nesting too deeply; using when a
                 generator expression would save memory.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/01_list_comprehensions.py
"""


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Basic list comprehension")  # section header
    print("=" * 50)  # close header divider
    squares = [x**2 for x in range(1, 6)]  # square each integer from 1 through 5
    print(f"Squares: {squares}")  # display resulting list

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Filter with condition")  # section header
    print("=" * 50)  # close header divider
    evens = [x for x in range(20) if x % 2 == 0]  # keep only even numbers
    print(f"Evens: {evens}")  # show filtered list

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Transform strings")  # section header
    print("=" * 50)  # close header divider
    words = ["hello", "world", "python"]  # sample word list
    upper = [w.upper() for w in words]  # uppercase each word
    print(f"Upper: {upper}")  # display transformed strings

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Nested comprehension (flatten 2D list)")  # section header
    print("=" * 50)  # close header divider
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3x3 nested list
    flat = [num for row in matrix for num in row]  # flatten by iterating rows then items
    print(f"Flat: {flat}")  # single list of all numbers

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — If-else expression (before for)")  # section header
    print("=" * 50)  # close header divider
    labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]  # ternary per item
    print(f"Labels: {labels}")  # classify each number 0..4

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Practical: filter and transform records")  # section header
    print("=" * 50)  # close header divider
    students = [  # list of student records as dicts
        {"name": "Alice", "score": 92},  # passing student
        {"name": "Bob", "score": 55},  # failing student
        {"name": "Carol", "score": 88},  # passing student
    ]
    passed = [s["name"] for s in students if s["score"] >= 60]  # names with score >= 60
    print(f"Passed: {passed}")  # show qualifying names

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — Comprehension vs loop equivalence")  # section header
    print("=" * 50)  # close header divider
    doubled_loop = []  # accumulate results manually
    for x in range(5):  # iterate 0..4
        doubled_loop.append(x * 2)  # append doubled value
    doubled_comp = [x * 2 for x in range(5)]  # equivalent one-line comprehension
    print(f"Loop:          {doubled_loop}")  # show loop result
    print(f"Comprehension: {doubled_comp}")  # show comprehension result

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 8 — Extract file extensions from paths")  # section header
    print("=" * 50)  # close header divider
    paths = ["report.pdf", "photo.jpg", "script.py", "archive"]  # sample filenames
    extensions = [p.rsplit(".", 1)[-1] if "." in p else "none" for p in paths]  # ext or none
    print(f"Extensions: {extensions}")  # show parsed extensions


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
