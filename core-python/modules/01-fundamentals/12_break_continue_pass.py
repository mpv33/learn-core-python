"""
12 — break, continue, pass: Loop Control Flow

THEORY
------
What is it?
    break exits the innermost loop immediately. continue skips the rest of the
    current iteration and jumps to the next. pass is a no-op placeholder for
    syntactically required blocks. Loops can have else — runs if no break occurred.

Why it matters
    Search-and-stop patterns use break. Filtering uses continue. pass lets you
    stub functions and empty classes during development. The for/else construct
    is uncommon but appears in interviews and Pythonic search patterns.

Key syntax/rules
    - break                          → exit innermost loop entirely
    - continue                       → skip to next iteration of innermost loop
    - pass                           → do nothing; satisfies syntax requirement
    - for x in seq: ... else: ...    → else runs only if loop finished without break
    - break in nested loops          → breaks inner loop only, not outer

When to use
    - break when target found (search, first match)
    - continue to skip invalid/unwanted items in a batch
    - pass for TODO stubs in if/for/class/function bodies
    - loop else for "not found" messaging after exhaustive search

Common mistakes
    - Expecting break to exit all nested loops (use a flag or return instead)
    - Using pass when you meant continue or break
    - Empty except: pass — swallows errors silently (bad practice)
    - Forgetting else on while/for attaches to the loop, not the if inside it

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/12_break_continue_pass.py
"""


def main() -> None:  # entry point that runs all loop control practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — break: exit loop early")  # section title
    print("=" * 50)  # close section header
    print("Search for 7:")  # heading before search demo
    for num in range(1, 11):  # check numbers 1 through 10
        if num == 7:  # stop when target number is found
            print(f"  Found {num}! Stopping.")  # announce discovery
            break  # exit loop early; remaining numbers are skipped
        print(f"  Checking {num}...")  # only runs for numbers before 7

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — continue: skip iterations")  # section title
    print("=" * 50)  # close section header
    print("Odd numbers only (1-10):", end=" ")  # heading before odd-number filter
    for num in range(1, 11):  # iterate 1 through 10
        if num % 2 == 0:  # detect even numbers via remainder after division by 2
            continue  # skip even numbers and jump to next iteration
        print(num, end=" ")  # print only odd numbers on one line
    print()  # newline after odd number sequence

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — pass: syntactic placeholder")  # section title
    print("=" * 50)  # close section header
    for i in range(3):  # loop body intentionally empty for now
        pass  # valid no-op placeholder until real logic is added
    print("  Loop with pass ran without error.")  # confirms loop executed despite empty body

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — break in nested loops")  # section title
    print("=" * 50)  # close section header
    print("Find pair summing to 7:")  # heading before pair search
    pairs = [(1, 6), (2, 5), (3, 4), (1, 1)]  # list of coordinate-like pairs to test
    for a, b in pairs:  # unpack each pair into a and b
        if a + b == 7:  # check whether pair sums to target
            print(f"  Found: ({a}, {b})")  # report matching pair
            break  # stop searching after first match

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — for/else: runs when no break")  # section title
    print("=" * 50)  # close section header
    print("Search for 99 (not found):")  # heading before loop-else demo
    for num in range(1, 6):  # search small range where 99 cannot appear
        if num == 99:  # condition never true for this range
            print("Found!")  # would run only if 99 were found
            break  # would exit loop on success
    else:
        print("  99 not found in range 1-5.")  # runs because loop never hit break

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: PIN retry with lockout")  # section title
    print("=" * 50)  # close section header
    attempts = 0  # count how many tries have been made
    max_attempts = 3  # limit retries before lockout
    correct_pin = "1234"  # expected PIN for successful login
    simulated_pins = ["0000", "1111", "1234"]  # preset inputs simulating user tries
    while attempts < max_attempts:  # keep trying until attempts exhausted
        pin = simulated_pins[attempts]  # get next simulated PIN attempt
        attempts += 1  # increment attempt counter each pass
        if pin == correct_pin:  # check whether entered PIN matches
            print(f"PIN accepted on attempt {attempts}.")  # success message with attempt count
            break  # stop retry loop on correct PIN
        print(f"  Wrong PIN ({pin}). Attempt {attempts}/{max_attempts}.")  # feedback after failed try
    else:
        print("  Account locked.")  # runs only if loop exits without break


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all loop control practice sections
