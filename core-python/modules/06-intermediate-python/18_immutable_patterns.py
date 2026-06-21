"""
18 — Immutable Patterns

THEORY
------
What: Techniques to avoid in-place mutation — tuples, frozensets, frozen dataclasses,
      spread-copy dict/list updates, and sorted() vs .sort().
Why:  Safer concurrent code, predictable data flow, easier debugging and testing.
Key rules:
  - Prefer {**d, "key": val} and [*lst, item] over mutating in place.
  - @dataclass(frozen=True) and namedtuple give immutable records.
  - sorted() returns new list; list.sort() mutates in place.
When to use: Shared config, functional pipelines, hashable dict keys, thread-safe reads.
Common mistakes: Shallow copy when deep copy is needed; frozen dataclass with mutable
                 list fields; assuming tuple of lists is fully immutable.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/18_immutable_patterns.py
"""

from dataclasses import dataclass  # import dataclass decorator
from collections import namedtuple  # import lightweight immutable record type


@dataclass(frozen=True)  # instances cannot be mutated after creation
class Point:  # simple 2D coordinate record
    x: int  # x coordinate field
    y: int  # y coordinate field


def add_item(items, item):  # return new list with item appended
    return [*items, item]  # spread into new list


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Tuple immutability")  # section header
    print("=" * 50)  # close header divider
    config = ("localhost", 8080, "production")  # tuple cannot be modified in place
    print(f"Config: {config}")  # display immutable tuple
    print("  (config[0] = '127.0.0.1' would raise TypeError)")  # note immutability

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Copy-on-write dict update")  # section header
    print("=" * 50)  # close header divider
    original = {"a": 1, "b": 2}  # starting dictionary
    updated = {**original, "b": 99, "c": 3}  # spread original and override/add keys immutably
    print(f"Original: {original}")  # original dict unchanged
    print(f"Updated:  {updated}")  # new dict with updated values

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Frozen dataclass")  # section header
    print("=" * 50)  # close header divider
    p = Point(3, 4)  # create immutable point instance
    print(f"Frozen point: {p}")  # display frozen dataclass instance

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Return new list instead of mutating")  # section header
    print("=" * 50)  # close header divider
    fruits = ["apple", "banana"]  # initial fruit list
    fruits = add_item(fruits, "cherry")  # rebind to new list with cherry added
    print(f"New list: {fruits}")  # show updated list reference

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Immutable nested update")  # section header
    print("=" * 50)  # close header divider
    record = {"name": "Alice", "scores": [90, 85]}  # nested mutable structure inside dict
    new_record = {**record, "scores": [*record["scores"], 92]}  # copy dict and append score
    print(f"Original: {record}")  # original unchanged
    print(f"Updated:  {new_record}")  # show record with extended scores list

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — namedtuple read-only records")  # section header
    print("=" * 50)  # close header divider
    User = namedtuple("User", ["id", "name", "email"])  # define user record schema
    user = User(1, "Alice", "alice@example.com")  # instantiate read-only user
    print(f"User: {user.name}")  # access field by attribute name

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — sorted() vs list.sort()")  # section header
    print("=" * 50)  # close header divider
    nums = [3, 1, 4, 1, 5]  # unsorted numbers
    sorted_nums = sorted(nums)  # return new sorted list without mutating original
    print(f"Original: {nums}, Sorted copy: {sorted_nums}")  # compare original vs sorted copy


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
