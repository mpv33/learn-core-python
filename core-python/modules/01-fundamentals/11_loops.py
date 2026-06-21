"""
11 — Loops: for and while Iteration

THEORY
------
What is it?
    Loops repeat code. for iterates over any iterable (list, str, dict, range).
    while repeats while a condition is True. range() generates number sequences.
    enumerate(), zip(), and .items() provide index pairs and parallel iteration.

Why it matters
    Loops process collections, paginate data, and drive game/retry logic. Choosing
    for vs while affects readability. enumerate avoids manual index counters.
    Nested loops appear in matrix operations and combinatorial problems.

Key syntax/rules
    - for item in iterable:         → one pass per element
    - for i in range(start, stop, step): → stop is exclusive
    - while condition:              → check condition before each iteration
    - enumerate(seq)                → yields (index, value) pairs
    - zip(a, b)                     → pairs elements from equal-length iterables
    - for k, v in d.items():        → iterate dictionary key-value pairs

When to use
    - for when you know the collection or iteration count upfront
    - while for open-ended loops (retry until success, read until EOF)
    - enumerate when you need both index and value
    - zip to walk parallel lists without manual indexing

Common mistakes
    - Off-by-one with range (range(5) is 0–4, not 1–5)
    - Infinite while loops (forgetting to update the condition variable)
    - Modifying a list while iterating over it (use a copy or comprehension)
    - Using range(len(lst)) instead of enumerate(lst) or direct iteration

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/11_loops.py
"""


def main() -> None:  # entry point that runs all loop practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — for loop over sequences")  # section title
    print("=" * 50)  # close section header
    print("Fruits:")  # heading before listing fruits
    for fruit in ["apple", "banana", "cherry"]:  # iterate each string in the list
        print(f"  - {fruit}")  # print one fruit per loop iteration

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — range() number sequences")  # section title
    print("=" * 50)  # close section header
    print("Count 0 to 4:", end=" ")  # heading for basic range demo
    for i in range(5):  # i takes values 0, 1, 2, 3, 4
        print(i, end=" ")  # print number on same line with trailing space
    print()  # finish line with default newline after countdown
    print("Count 2 to 8 step 2:", end=" ")  # heading for ranged step demo
    for i in range(2, 9, 2):  # start at 2, stop before 9, step by 2
        print(i, end=" ")  # print 2, 4, 6, 8 on one line
    print()  # move to next line after sequence

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — enumerate and while loops")  # section title
    print("=" * 50)  # close section header
    print("With index:")  # heading for enumerate demo
    for index, fruit in enumerate(["apple", "banana"]):  # get position and value together
        print(f"  {index}: {fruit}")  # show zero-based index with fruit name
    print("Countdown:", end=" ")  # heading before countdown loop
    count = 5  # starting counter value
    while count > 0:  # repeat until count reaches zero
        print(count, end=" ")  # print current count on same line
        count -= 1  # decrease count by 1 each iteration
    print("Go!")  # message after loop finishes

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Dict, string, and zip iteration")  # section title
    print("=" * 50)  # close section header
    user = {"name": "Alice", "age": 30, "city": "NYC"}  # sample mapping of user fields
    print("User info:")  # heading before key-value output
    for key, value in user.items():  # walk each dictionary entry
        print(f"  {key}: {value}")  # print field name and its value
    print("Letters in 'Python':", end=" ")  # heading before char-by-char output
    for char in "Python":  # strings are sequences of characters
        print(char, end=" ")  # print each letter separated by spaces
    print()  # newline after letters
    names = ["Alice", "Bob"]  # parallel list of names
    scores = [90, 85]  # parallel list of scores aligned by index
    print("Name → Score:")  # heading for paired output
    for name, score in zip(names, scores):  # pair items from both lists by position
        print(f"  {name}: {score}")  # show matched name and score

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Nested loops")  # section title
    print("=" * 50)  # close section header
    print("Multiplication table (2x):")  # heading for nested loop table
    for i in range(1, 4):  # outer loop: rows 1 through 3
        for j in range(1, 4):  # inner loop: columns 1 through 3
            print(f"  {i} x {j} = {i * j}")  # print product for each row/column pair

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: FizzBuzz 1–15")  # section title
    print("=" * 50)  # close section header
    for n in range(1, 16):  # classic FizzBuzz for numbers 1 through 15
        if n % 15 == 0:  # divisible by both 3 and 5
            label = "FizzBuzz"  # replace number with FizzBuzz
        elif n % 3 == 0:  # divisible by 3 only
            label = "Fizz"  # replace number with Fizz
        elif n % 5 == 0:  # divisible by 5 only
            label = "Buzz"  # replace number with Buzz
        else:
            label = str(n)  # keep the number as a string
        print(label, end=" ")  # print result on one line
    print()  # newline after FizzBuzz sequence


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all loop practice sections
