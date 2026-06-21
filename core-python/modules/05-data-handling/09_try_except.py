"""
09 — try / except basics
========================

THEORY
------
What:
  Exception handling catches runtime errors so your program can recover or report
  gracefully instead of crashing. `try` runs risky code; `except` handles failures.

Why:
  Real-world input is messy — bad files, invalid numbers, network timeouts.
  Handling errors keeps programs robust and user-friendly.

Key rules:
  - `try:` block contains code that might raise an exception.
  - `except ExceptionType:` catches only that type (be specific, not bare `except:`).
  - `except Error as e:` binds the exception object for inspection.
  - Unhandled exceptions propagate up and terminate the program.
  - Common built-ins: ValueError, TypeError, KeyError, IndexError, FileNotFoundError.

When to use:
  - Parsing user input or external data that may be invalid.
  - File/network operations that can fail intermittently.
  - Loops where one bad item shouldn't stop processing the rest.

Common mistakes:
  - Bare `except:` or overly broad `except Exception:` hiding real bugs.
  - Empty `except` blocks that silently swallow errors.
  - Using exceptions for normal control flow instead of validation.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/09_try_except.py
"""


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Catch a specific exception")  # label first block
    print("=" * 50)  # close header

    try:  # attempt code that may raise an exception
        result = 10 / 0  # triggers ZeroDivisionError
    except ZeroDivisionError:  # catch only division-by-zero errors
        print("Cannot divide by zero!")  # user-friendly fallback message
        result = None  # assign safe default when operation fails
    print(f"Result: {result}")  # show None after handled error

    print("\n" + "=" * 50)  # divider before loop demo
    print("PRACTICE 2 — Handle errors in a loop")  # label second block
    print("=" * 50)  # close header

    numbers = ["10", "20", "abc", "30"]  # mix of valid and invalid numeric strings
    total = 0  # running sum accumulator
    for num in numbers:  # process each value independently
        try:  # attempt conversion for this item only
            total += int(num)  # add parsed integer to total
        except ValueError:  # catch non-numeric strings without stopping loop
            print(f"  Skipping invalid value: {num!r}")  # log and continue
    print(f"Total: {total}")  # sum of successfully parsed values only

    print("\n" + "=" * 50)  # divider before exception info demo
    print("PRACTICE 3 — Access exception info")  # label third block
    print("=" * 50)  # close header

    try:  # attempt invalid list access
        items = [1, 2, 3]  # short list for index demo
        print(items[10])  # index out of range
    except IndexError as e:  # bind exception object to e
        print(f"IndexError: {e}")  # print the exception message

    print("\n" + "=" * 50)  # divider before file error demo
    print("PRACTICE 4 — FileNotFoundError handling")  # label fourth block
    print("=" * 50)  # close header

    try:  # attempt to read a missing file
        with open("nonexistent_file.txt", "r", encoding="utf-8") as f:  # file does not exist
            content = f.read()  # never reached
    except FileNotFoundError as e:  # catch missing file specifically
        print(f"File not found: {e.filename}")  # show which file was missing
    print("Program continues after handled error.")  # prove execution did not crash


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
