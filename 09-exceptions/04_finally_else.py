"""04 — finally, else, and exception chaining"""

# try / except / else / finally
def read_number(text):
    try:
        value = int(text)
    except ValueError:
        print(f"  Could not parse: {text!r}")
        return None
    else:
        # Runs only if NO exception occurred
        print(f"  Successfully parsed: {value}")
        return value
    finally:
        # ALWAYS runs (cleanup)
        print(f"  [finally] Done processing {text!r}")

print("Parsing '42':")
read_number("42")

print("\nParsing 'abc':")
read_number("abc")

# finally for resource cleanup
class FakeFile:
    def __init__(self, name):
        self.name = name
        self.closed = False
        print(f"  Opened {name}")

    def read(self):
        return "data"

    def close(self):
        self.closed = True
        print(f"  Closed {self.name}")

def read_file(name):
    f = FakeFile(name)
    try:
        return f.read()
    finally:
        f.close()

read_file("demo.txt")

# Exception chaining (preserve original cause)
try:
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("Calculation failed") from e
except RuntimeError as e:
    print(f"\nRuntimeError: {e}")
    print(f"Caused by: {e.__cause__}")

# assert — debug checks (disabled with python -O)
age = 25
assert age >= 0, "Age must be non-negative"
print("\nAssert passed.")
