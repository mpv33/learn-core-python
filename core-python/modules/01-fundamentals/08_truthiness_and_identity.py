"""
08 — Truthiness, Identity, and id(): == vs is

THEORY
------
What is it?
    Every Python object is truthy or falsy in boolean context. == compares values;
    is compares identity (same object in memory via id()). None checks must use
    `is None`. The walrus operator (:=) assigns inside an expression.

Why it matters
    Top interview topic. Using is for value comparison causes subtle bugs. Short-
    circuit evaluation (and/or) affects performance and side effects. Small integer
    caching (-5 to 256) tricks candidates in `is` vs `==` questions.

Key syntax/rules
    - Falsy: None, False, 0, 0.0, "", [], {}, set(), range(0)
    - Everything else is truthy (including "0", [0], non-empty strings)
    - a is b  → same as id(a) == id(b)
    - value is None  → correct; value == None  → works but not idiomatic
    - if (n := len(data)) > 0:  → walrus assigns n and uses it in condition
    - False and f()  → f() never called; True or f()  → f() never called

When to use
    - is / is not for None, True, False, and singleton identity checks
    - == for value equality (numbers, strings, list contents)
    - Walrus when you need a value twice (condition + body) without repeating

Common mistakes
    - if x == None instead of if x is None
    - if my_list: assumes non-empty, but forgets empty list is falsy
    - x is 257 — unreliable; use == for integer value comparison
    - Expecting and/or to return only True/False — they return the deciding operand

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/08_truthiness_and_identity.py
"""


def expensive() -> bool:  # helper that prints when actually called
    print("  (expensive called)")  # proves whether this function ran
    return True  # return True if execution reaches here


def main() -> None:  # entry point that runs all truthiness practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — == vs is (value vs identity)")  # section title
    print("=" * 50)  # close section header
    a = [1, 2, 3]  # first list object with values 1, 2, 3
    b = [1, 2, 3]  # second list with identical contents but separate object
    c = a  # c references the same list object as a
    print(f"a == b: {a == b}")  # True — same content even though different objects
    print(f"a is b: {a is b}")  # False — a and b are different list objects
    print(f"a is c: {a is c}")  # True — c points to the exact same object as a
    print(f"id(a): {id(a)}, id(b): {id(b)}, id(c): {id(c)}")  # show memory addresses

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Small integer caching")  # section title
    print("=" * 50)  # close section header
    x, y = 256, 256  # small integers may share one cached object
    p, q = 257, 257  # larger integers may not be cached the same way
    print(f"256 is 256: {x is y}")  # often True because CPython caches small ints
    print(f"257 is 257: {p is q}")  # may be False — depends on implementation details
    print(f"256 == 256: {x == y}")  # always True — value comparison is reliable

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Truthy and falsy values")  # section title
    print("=" * 50)  # close section header
    falsy = [None, False, 0, 0.0, "", [], {}, set(), range(0)]  # known falsy values
    for val in falsy:  # loop through each known falsy value
        print(f"  {repr(val):12} → bool = {bool(val)}")  # show value and its boolean conversion
    print(f"  {'[0]':12} → bool = {bool([0])}")  # truthy — non-empty list, even with falsy element

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Short-circuit evaluation")  # section title
    print("=" * 50)  # close section header
    print("Short-circuit AND (False and ...):")  # label before and demo
    result_and = False and expensive()  # left side False — expensive() never called
    print(f"  Result: {result_and}")  # show that and returned False without calling expensive
    print("Short-circuit OR (True or ...):")  # label before or demo
    result_or = True or expensive()  # left side True — expensive() never called
    print(f"  Result: {result_or}")  # show that or returned True without calling expensive

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Walrus operator and None checks")  # section title
    print("=" * 50)  # close section header
    data = ["admin", "user", "guest"]  # sample list whose length we want in the condition
    if (n := len(data)) > 2:  # assign length to n and test whether it exceeds 2
        print(f"Walrus: list has {n} items")  # use n inside the block after assignment
    value = None  # variable intentionally set to no value
    print(f"value is None: {value is None}")  # preferred identity check for None

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: config validation")  # section title
    print("=" * 50)  # close section header
    config = {"host": "localhost", "port": 8080, "debug": ""}  # sample config with empty debug flag
    for key, val in config.items():  # check each config value's truthiness
        status = "set" if val else "empty/missing"  # falsy values flagged as empty
        print(f"  {key}: {status}")  # report whether each setting has a truthy value


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all truthiness practice sections
