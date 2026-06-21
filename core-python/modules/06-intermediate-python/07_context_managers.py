"""
07 — Context Managers

THEORY
------
What: Objects used with the with statement that guarantee setup and teardown via
      __enter__/__exit__ or the @contextmanager decorator.
Why:  Ensure resources (files, locks, connections) are released even when errors occur.
Key rules:
  - __enter__ returns the resource; __exit__ receives exception info (or None).
  - Return True from __exit__ to suppress an exception (rare — use with care).
  - @contextmanager: code before yield is setup; finally block is teardown.
When to use: File I/O, database connections, locks, temporary config changes.
Common mistakes: Swallowing exceptions in __exit__; forgetting finally in @contextmanager;
                 not using with for resources that need guaranteed cleanup.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/07_context_managers.py
"""

from contextlib import contextmanager, suppress, redirect_stdout, ExitStack  # context utilities
from pathlib import Path  # build demo file path
import io  # in-memory text buffer


class DatabaseConnection:  # manage connect/use/disconnect lifecycle
    def __init__(self, db_name: str):  # store database identifier
        self.db_name = db_name  # name exposed to with-block

    def __enter__(self):  # called when entering with-statement
        print(f"  Connecting to {self.db_name}...")  # simulate opening connection
        return self  # object bound to as-variable

    def __exit__(self, exc_type, exc_val, exc_tb):  # called when leaving with-block
        print(f"  Closing {self.db_name}.")  # simulate closing connection
        return False  # don't suppress exceptions


@contextmanager
def temporary_value(obj, attr, new_value):  # temporarily set attribute, then restore
    old_value = getattr(obj, attr)  # save current attribute value
    setattr(obj, attr, new_value)  # apply temporary override
    try:  # yield control to with-block
        yield obj  # provide object to caller
    finally:  # always restore original value
        setattr(obj, attr, old_value)  # revert attribute after block


class Config:  # simple settings holder
    debug = False  # class-level debug flag


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Class-based context manager")  # section header
    print("=" * 50)  # close header divider
    with DatabaseConnection("mydb") as db:  # acquire and release connection automatically
        print(f"  Running query on {db.db_name}")  # use connection inside block

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — @contextmanager decorator")  # section header
    print("=" * 50)  # close header divider
    print(f"  Before: debug={Config.debug}")  # show initial value
    with temporary_value(Config, "debug", True):  # temporarily enable debug
        print(f"  Inside: debug={Config.debug}")  # debug is True inside block
    print(f"  After:  debug={Config.debug}")  # original value restored

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Built-in open() context manager")  # section header
    print("=" * 50)  # close header divider
    demo = Path(__file__).parent / "ctx_demo.txt"  # temporary file beside script
    with open(demo, "w") as f:  # file closed automatically on exit
        f.write("context manager demo")  # write demo content
    print(f"  Wrote {demo.name}, exists={demo.exists()}")  # confirm file was created
    demo.unlink()  # remove temporary file

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — contextlib helpers")  # section header
    print("=" * 50)  # close header divider
    with suppress(FileNotFoundError):  # ignore specific exception inside block
        open("nonexistent_file.txt")  # would raise FileNotFoundError without suppress
    print("  suppress: no crash on missing file")  # confirm suppress worked
    buf = io.StringIO()  # capture printed output in memory
    with redirect_stdout(buf):  # temporarily redirect print output
        print("Hidden output")  # this print goes to buf, not terminal
    print(f"  Captured: {buf.getvalue()!r}")  # show captured string

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — ExitStack for multiple managers")  # section header
    print("=" * 50)  # close header divider
    with ExitStack() as stack:  # register one or more context managers
        f1 = stack.enter_context(open(demo, "w"))  # open file tracked by stack
        f1.write("stack demo")  # write through managed file handle
    print(f"  ExitStack wrote file, exists={demo.exists()}")  # confirm stack closed file
    demo.unlink()  # cleanup demo file after stack closes it


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
