"""
12 — finally, else, and exception chaining
==========================================

THEORY
------
What:
  `try/except/else/finally` provides complete control flow for error handling.
  `else` runs when no exception occurred; `finally` always runs for cleanup.
  Exception chaining preserves the original cause when re-raising.

Why:
  Guarantee resource cleanup (close files, release locks) even when errors occur.
  Separate success-path logic (`else`) from error handling (`except`).

Key rules:
  - `else` block runs only if the `try` block completed without exception.
  - `finally` block ALWAYS runs — success, failure, or even `return`/`break`.
  - `raise RuntimeError("msg") from original` links exceptions via `__cause__`.
  - `raise ... from None` suppresses the chain (hide low-level details).
  - `assert condition, "msg"` — debug check; disabled with `python -O`.

When to use:
  - `finally`: closing files, DB connections, releasing locks.
  - `else`: code that depends on try succeeding (avoid catching its exceptions).
  - Chaining: wrapping library errors in application-level exceptions.
  - `assert`: internal invariants during development (not user input validation).

Common mistakes:
  - Putting logic in `finally` that should only run on success — use `else`.
  - Using `assert` for user input validation — disabled in optimized (`-O`) mode.
  - Swallowing exceptions in `finally` — can mask the original error.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/12_finally_else.py
"""


class FakeFile:
    def __init__(self, name):
        self.name = name  # exposed name attribute
        self.closed = False  # track open/closed state
        print(f"  Opened {name}")  # simulate opening resource

    def read(self):
        return "data"  # fixed demo payload

    def close(self):
        self.closed = True  # mark as closed
        print(f"  Closed {self.name}")  # simulate cleanup


def read_number(text):
    try:  # attempt conversion
        value = int(text)  # may raise ValueError
    except ValueError:  # handle non-integer input
        print(f"  Could not parse: {text!r}")  # show rejected input
        return None  # early return on failure
    else:  # runs only if NO exception occurred
        print(f"  Successfully parsed: {value}")  # success path logging
        return value  # return parsed integer
    finally:  # ALWAYS runs (cleanup)
        print(f"  [finally] Done processing {text!r}")  # executes on success and failure


def read_file(name):
    f = FakeFile(name)  # acquire resource
    try:  # use resource
        return f.read()  # return file contents
    finally:  # always close, even on exception
        f.close()  # guaranteed cleanup


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — try / except / else / finally")  # label first block
    print("=" * 50)  # close header

    print("Parsing '42':")  # demo successful parse
    result_ok = read_number("42")  # triggers else and finally
    print(f"Returned: {result_ok}")  # show parsed value
    print("\nParsing 'abc':")  # demo failed parse
    result_fail = read_number("abc")  # triggers except and finally
    print(f"Returned: {result_fail}")  # show None after failure

    print("\n" + "=" * 50)  # divider before finally cleanup demo
    print("PRACTICE 2 — finally for resource cleanup")  # label second block
    print("=" * 50)  # close header

    data = read_file("demo.txt")  # demonstrate open/use/close lifecycle
    print(f"  Read: {data}")  # show file contents

    print("\n" + "=" * 50)  # divider before chaining demo
    print("PRACTICE 3 — Exception chaining")  # label third block
    print("=" * 50)  # close header

    try:  # outer handler observes wrapped error
        try:  # inner operation fails
            result = 1 / 0  # ZeroDivisionError
        except ZeroDivisionError as e:  # capture original exception
            raise RuntimeError("Calculation failed") from e  # wrap, keep cause
    except RuntimeError as e:  # handle outer exception
        print(f"RuntimeError: {e}")  # show wrapper message
        print(f"Caused by: {e.__cause__}")  # show linked original exception

    print("\n" + "=" * 50)  # divider before assert demo
    print("PRACTICE 4 — assert for debug checks")  # label fourth block
    print("=" * 50)  # close header

    age = 25  # sample value for assertion demo
    assert age >= 0, "Age must be non-negative"  # abort if condition is false (unless -O)
    print("Assert passed.")  # reached only when assertion succeeds


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
