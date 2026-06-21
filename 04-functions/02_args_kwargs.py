"""02 — Arguments: defaults, *args, **kwargs"""

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"power(3) = {power(3)}")
print(f"power(3, 3) = {power(3, 3)}")

# Keyword arguments (order doesn't matter)
def create_user(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

print(create_user(age=25, name="Bob", city="Delhi"))

# *args — variable positional arguments (tuple)
def sum_all(*args):
    return sum(args)

print(f"sum_all(1,2,3,4) = {sum_all(1, 2, 3, 4)}")

# **kwargs — variable keyword arguments (dict)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("User info:")
print_info(name="Alice", role="Admin", active=True)

# Combine all forms
def flexible(required, *args, default="x", **kwargs):
    print(f"  required={required}")
    print(f"  args={args}")
    print(f"  default={default}")
    print(f"  kwargs={kwargs}")

print("\nFlexible function:")
flexible(1, 2, 3, default="y", extra="z")

# Unpacking when calling
nums = [1, 2, 3]
print(f"\nUnpacked: {sum_all(*nums)}")

config = {"name": "App", "version": "1.0"}
print_info(**config)

# ⚠️ Avoid mutable default arguments
def bad_append(item, lst=[]):   # DON'T do this
    lst.append(item)
    return lst

def good_append(item, lst=None):  # DO this instead
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"\nGood: {good_append('a')}, {good_append('b')}")
