"""
02 — Tuples: Ordered, Immutable Sequences

THEORY
------
What is it?
    A tuple is an ordered, immutable sequence created with parentheses () or
    by comma-separating values. Once created, you cannot add, remove, or
    reassign elements — though mutable objects inside a tuple can still change.

Why it matters
    Tuples are hashable (when all elements are hashable), so they work as dict
    keys and set members — lists cannot. They are faster and safer for fixed
    records like coordinates, database rows, and function return values.

Key syntax/rules
    - Single-element tuple requires a trailing comma: (42,) not (42)
    - Parentheses are optional: x, y = 1, 2 creates a tuple
    - Unpacking: a, b = point assigns elements to separate variables
    - Extended unpacking: first, *middle, last = sequence
    - namedtuple creates lightweight classes with named fields
    - Immutable means no reassignment — record[0] = x raises TypeError

When to use
    - Fixed-size records (coordinates, RGB colors, database rows)
    - Dict keys or set elements that must be hashable
    - Function return values that should not be accidentally modified
    - Swapping variables: a, b = b, a

Common mistakes
    - Forgetting the comma in (42,) — (42) is just an int in parentheses
    - Assuming "immutable" means contents can't change — inner lists can mutate
    - Using lists as dict keys (TypeError) when tuples would work
    - Creating namedtuple field names that aren't valid identifiers

PRACTICE
--------
Run: python3 core-python/modules/02-data-structures/02_tuples.py
"""

from collections import namedtuple  # factory for lightweight tuple subclasses with named fields


def main() -> None:  # entry point that runs all tuple practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Create and access tuples")  # section title
    print("=" * 50)  # close section header
    point = (3, 4)  # create a tuple of x and y coordinates
    single = (42,)  # single-element tuple needs a trailing comma
    rgb = 255, 128, 0  # parentheses optional when comma-separating values
    print(f"point: {point}, type: {type(point)}")  # show tuple and its type
    print(f"single: {single}, rgb: {rgb}")  # show single-element and bare tuple

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Unpacking")  # section title
    print("=" * 50)  # close section header
    x, y = point  # unpack tuple values into separate variables
    print(f"x={x}, y={y}")  # display unpacked values
    first, *middle, last = [1, 2, 3, 4, 5]  # extended unpacking with star
    print(f"first={first}, middle={middle}, last={last}")  # show unpacked parts

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Named tuples")  # section title
    print("=" * 50)  # close section header
    Point = namedtuple("Point", ["x", "y"])  # define a Point type with named fields
    p = Point(10, 20)  # create a Point instance
    print(f"Named: {p.x}, {p.y}")  # access fields by name instead of index
    print(f"As tuple: {tuple(p)}")  # convert namedtuple back to plain tuple

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Tuples as dict keys")  # section title
    print("=" * 50)  # close section header
    locations = {(0, 0): "origin", (1, 2): "point A"}  # coordinate tuples as keys
    print(f"Location at (0,0): {locations[(0, 0)]}")  # look up by tuple key
    print(f"All locations: {list(locations.items())}")  # show all key-value pairs

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Mutable objects inside tuples")  # section title
    print("=" * 50)  # close section header
    record = ("Alice", [90, 85, 88])  # tuple holds immutable name + mutable list
    record[1].append(92)  # append to inner list — tuple itself unchanged
    print(f"Mutable inside tuple: {record}")  # show that inner list was modified
    # point[0] = 5  # TypeError — cannot reassign tuple elements

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Swap and compare")  # section title
    print("=" * 50)  # close section header
    a, b = 1, 2  # assign two values
    a, b = b, a  # swap using tuple unpacking (no temp variable)
    print(f"After swap: a={a}, b={b}")  # confirm the swap worked
    print("Tuple vs List:")  # heading for comparison
    print("  Tuple: fixed size, faster, hashable if all elements hashable")  # tuple traits
    print("  List:  flexible, more methods, not hashable")  # list traits

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Practical: min/max from scores")  # section title
    print("=" * 50)  # close section header
    student = ("Bob", 88, 92, 79)  # name plus three exam scores as fixed record
    name, *scores = student  # unpack name and collect scores in a list
    print(f"{name}: min={min(scores)}, max={max(scores)}, avg={sum(scores)/len(scores):.1f}")  # stats from tuple

    print("=" * 50)  # print section divider
    print("PRACTICE 8 — Practical: function returning tuple")  # section title
    print("=" * 50)  # close section header
    def divide(a: int, b: int) -> tuple[int, int]:  # return quotient and remainder together
        return a // b, a % b  # multiple return values packaged as a tuple
    q, r = divide(17, 5)  # unpack returned tuple into two variables
    print(f"17 // 5 = {q}, remainder = {r}")  # show quotient and remainder


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all tuple practice sections
