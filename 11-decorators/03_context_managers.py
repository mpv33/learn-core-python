"""03 — Context Managers"""

from contextlib import contextmanager

# Class-based context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"  Connecting to {self.db_name}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  Closing {self.db_name}.")
        return False  # don't suppress exceptions

with DatabaseConnection("mydb") as db:
    print(f"  Running query on {db.db_name}")

# @contextmanager — generator-based (simpler)
@contextmanager
def temporary_value(obj, attr, new_value):
    old_value = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield obj
    finally:
        setattr(obj, attr, old_value)

class Config:
    debug = False

print("\nToggle debug:")
print(f"  Before: debug={Config.debug}")
with temporary_value(Config, "debug", True):
    print(f"  Inside: debug={Config.debug}")
print(f"  After:  debug={Config.debug}")

# Built-in: open, threading.Lock
from pathlib import Path

demo = Path(__file__).parent / "ctx_demo.txt"
with open(demo, "w") as f:
    f.write("context manager demo")
demo.unlink()

# contextlib helpers
from contextlib import suppress, redirect_stdout
import io

print("\nsuppress FileNotFoundError:")
with suppress(FileNotFoundError):
    open("nonexistent_file.txt")

buf = io.StringIO()
with redirect_stdout(buf):
    print("Hidden output")
print(f"Captured: {buf.getvalue()!r}")

# ExitStack — multiple context managers
from contextlib import ExitStack

with ExitStack() as stack:
    f1 = stack.enter_context(open(demo, "w"))
    f1.write("stack demo")
demo.unlink()
