"""
06 — Operators: Arithmetic, Comparison, and Logic

THEORY
------
What is it?
    Operators perform computations and comparisons on values. Python supports
    arithmetic (+, -, *, /, //, %, **), comparison (==, !=, <, >), logical
    (and, or, not), identity (is), membership (in), and assignment shortcuts (+=).

Why it matters
    Operator precedence bugs cause silent logic errors. // vs / is a classic interview
    question. `is` vs `==` trips up beginners. Chained comparisons (a < b < c) are
    idiomatic Python that reads naturally.

Key syntax/rules
    - / always returns float; // is floor division (truncates toward negative infinity)
    - % is modulo (remainder); ** is exponentiation
    - == compares values; is compares object identity (same memory address)
    - and / or short-circuit — right side may never evaluate
    - x in collection — membership test for sequences, sets, dict keys
    - a < b < c — chained comparison, same as a < b and b < c

When to use
    - Arithmetic for calculations; // and % for indexing and pagination
    - Chained comparisons for range checks (0 <= x <= 100)
    - in / not in for presence checks in collections
    - is only for None, True, False, and singleton checks — not general equality

Common mistakes
    - Using is to compare strings or small integers outside cached range
    - Expecting 7 / 2 to be 3 (it's 3.5) — use // for integer division
    - Writing a < b < c as (a < b) < c — chained form is correct, nested is wrong
    - Confusing & (bitwise) with and (logical) — different operators

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/06_operators.py
"""


def main() -> None:  # entry point that runs all operator practice sections
    a, b = 10, 3  # assign two integers for operator demonstrations

    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Arithmetic operators")  # section title
    print("=" * 50)  # close section header
    print(f"  {a} + {b} = {a + b}")  # addition: combine two numbers → 13
    print(f"  {a} - {b} = {a - b}")  # subtraction: difference between values → 7
    print(f"  {a} * {b} = {a * b}")  # multiplication: repeated addition → 30
    print(f"  {a} / {b} = {a / b}")  # true division: always returns float → 3.333...
    print(f"  {a} // {b} = {a // b}")  # floor division: drop decimal part → 3
    print(f"  {a} % {b} = {a % b}")  # modulo: remainder after division → 1
    print(f"  {a} ** {b} = {a ** b}")  # exponent: 10 raised to power 3 → 1000

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Comparison and logical operators")  # section title
    print("=" * 50)  # close section header
    print(f"  {a} == {b}: {a == b}")  # equal: check if values are the same
    print(f"  {a} != {b}: {a != b}")  # not equal: check if values differ
    print(f"  {a} > {b}: {a > b}")  # greater than: left value larger than right
    print(f"  {a} <= {b}: {a <= b}")  # less than or equal: left value not above right
    x, y = True, False  # two booleans for logical operator demos
    print(f"  True and False: {x and y}")  # both must be True for result to be True
    print(f"  True or False:  {x or y}")  # at least one True makes the result True
    print(f"  not True:         {not x}")  # flip True to False

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Assignment shortcuts")  # section title
    print("=" * 50)  # close section header
    n = 5  # starting value before compound assignments
    n += 3  # add 3 to n (same as n = n + 3) → 8
    n *= 2  # multiply n by 2 (same as n = n * 2) → 16
    print(f"After += 3 and *= 2: n = {n}")  # show final value after shortcuts

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Identity and membership")  # section title
    print("=" * 50)  # close section header
    list1 = [1, 2, 3]  # create first list object
    list2 = [1, 2, 3]  # create second list with same contents
    list3 = list1  # make list3 point to the same object as list1
    print(f"list1 == list2: {list1 == list2}")  # True — same values inside lists
    print(f"list1 is list2: {list1 is list2}")  # False — different objects in memory
    print(f"list1 is list3: {list1 is list3}")  # True — both names refer to same object
    fruits = ["apple", "banana", "cherry"]  # sample list for in/not in checks
    print(f"'banana' in fruits:     {'banana' in fruits}")  # True — item exists in list
    print(f"'grape' not in fruits:  {'grape' not in fruits}")  # True — item is absent

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Chained comparisons")  # section title
    print("=" * 50)  # close section header
    score = 85  # test value for readable range check
    print(f"60 <= {score} < 90: {60 <= score < 90}")  # True — score lies between 60 and 90
    temp = 22  # room temperature in Celsius for comfort check
    print(f"18 <= {temp} <= 26: {18 <= temp <= 26}")  # True — comfortable room temperature range

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: discount eligibility")  # section title
    print("=" * 50)  # close section header
    order_total = 75.00  # cart total before discount
    is_member = True  # whether customer has loyalty membership
    eligible = order_total >= 50 and is_member  # must meet minimum AND be a member
    discount = order_total * 0.10 if eligible else 0  # 10% off when eligible
    print(f"Order: ${order_total:.2f}, Member: {is_member}")  # show order context
    print(f"Discount: ${discount:.2f}, Final: ${order_total - discount:.2f}")  # show savings


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all operator practice sections
