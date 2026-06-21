"""
10 — if / elif / else: Conditional Execution

THEORY
------
What is it?
    Conditional statements run code blocks only when expressions evaluate to True.
    if / elif / else chain multiple conditions top-down; the first True branch wins.
    Ternary syntax (x if condition else y) picks a value in one expression.

Why it matters
    Control flow is fundamental to every program. Nested if clarifies multi-step
    decisions. Combining conditions with and/or builds validation logic. Truthiness
    lets you write `if my_list:` instead of `if len(my_list) > 0:`.

Key syntax/rules
    - if condition: block            → indent block with 4 spaces (or consistent tab)
    - elif other: block             → checked only if prior conditions were False
    - else: block                   → runs when all conditions above were False
    - x if cond else y              → ternary expression (not a statement)
    - and / or combine conditions   → both sides must be evaluated per short-circuit rules
    - No parentheses required around condition (unlike C/Java)

When to use
    - Branching on user input, config flags, or computed results
    - elif chains for grading, status codes, menu selections
    - Ternary for simple two-way value assignment
    - Nested if when outer gate must pass before inner check matters

Common mistakes
    - Using = instead of == in conditions (SyntaxError or accidental assignment in walrus)
    - Empty blocks without pass (IndentationError)
    - elif after else (syntax error — else must be last)
    - Deep nesting (>3 levels) — refactor with early return or guard clauses

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/10_if_else.py
"""


def main() -> None:  # entry point that runs all if/else practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — if / elif / else grading")  # section title
    print("=" * 50)  # close section header
    score = 85  # example test score used to assign a letter grade
    if score >= 90:  # highest grade threshold checked first
        grade = "A"  # assign A when score is 90 or above
    elif score >= 80:  # next tier if score is below 90
        grade = "B"  # assign B when score is 80–89
    elif score >= 70:  # next tier if score is below 80
        grade = "C"  # assign C when score is 70–79
    else:  # all higher conditions failed
        grade = "F"  # assign F when score is below 70
    print(f"Score {score} → Grade {grade}")  # show final grade for the score

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Nested if statements")  # section title
    print("=" * 50)  # close section header
    age = 20  # sample age for admission example
    has_ticket = True  # whether the person has a ticket
    if age >= 18:  # outer check: must be an adult
        if has_ticket:  # inner check: adult also needs a ticket
            print("You may enter.")  # both conditions satisfied
        else:
            print("You need a ticket.")  # adult but missing ticket
    else:
        print("You must be 18+.")  # too young regardless of ticket

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Ternary and compound conditions")  # section title
    print("=" * 50)  # close section header
    status = "adult" if age >= 18 else "minor"  # pick label based on age in one expression
    print(f"Status: {status}")  # display computed adult/minor status
    username = "admin"  # login username to validate
    password = "secret123"  # password paired with username
    if username == "admin" and password == "secret123":  # both credentials must match
        print("Login successful!")  # full match grants access
    elif username == "admin":  # username correct but password wrong
        print("Wrong password.")  # tell user password failed
    else:
        print("Unknown user.")  # username not recognized

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Truthy / falsy in conditions")  # section title
    print("=" * 50)  # close section header
    values = [0, 1, "", "hello", [], [1], None]  # mix of falsy and truthy examples
    for v in values:  # inspect each value's truthiness
        print(f"  {repr(v):10} → {'Truthy' if v else 'Falsy'}")  # show whether bool(v) would be True

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: shipping rate calculator")  # section title
    print("=" * 50)  # close section header
    weight_kg = 2.5  # package weight in kilograms
    is_express = True  # whether customer chose express delivery
    if weight_kg <= 1:  # lightest tier
        rate = 5.00  # base rate for packages up to 1 kg
    elif weight_kg <= 5:  # medium tier
        rate = 8.50  # base rate for packages up to 5 kg
    else:  # heavy tier
        rate = 15.00  # base rate for packages over 5 kg
    if is_express:  # add surcharge for express delivery
        rate *= 1.5  # 50% express surcharge on base rate
    print(f"Weight: {weight_kg} kg, Express: {is_express}")  # show input parameters
    print(f"Shipping rate: ${rate:.2f}")  # display computed shipping cost


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all if/else practice sections
