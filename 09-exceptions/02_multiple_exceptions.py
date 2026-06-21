"""02 — Multiple Exceptions"""

def parse_age(value):
    try:
        age = int(value)
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        return age
    except ValueError as e:
        print(f"  Invalid age '{value}': {e}")
        return None

for test in ["25", "abc", "-5", "200"]:
    result = parse_age(test)
    if result is not None:
        print(f"  Valid age: {result}")

# Multiple except blocks
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("  Error: division by zero")
    except TypeError:
        print("  Error: must be numbers")
    return None

print(f"\nsafe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
print(f"safe_divide(10, 'a') = {safe_divide(10, 'a')}")

# Tuple of exceptions
def read_config(data):
    try:
        return data["host"], data["port"]
    except (KeyError, TypeError) as e:
        print(f"  Config error: {e}")
        return "localhost", 8080

print(f"\nConfig: {read_config({'host': 'api.com'})}")
print(f"Config: {read_config({})}")

# Catch all (use sparingly)
try:
    x = undefined_variable  # noqa: F821
except Exception as e:
    print(f"\nCaught {type(e).__name__}: {e}")
