"""
02 — Arguments: Defaults, *args, **kwargs

THEORY
------
What is it?
    Python functions accept positional arguments, keyword arguments, default
    values, and variable-length collections via *args (tuple of extras) and
    **kwargs (dict of keyword extras). Callers can also unpack iterables and
    dicts with * and ** at call time.

Why it matters
    Flexible signatures let you write wrappers, decorators, and APIs that accept
    varying inputs. Understanding *args/**kwargs is essential for reading library
    code and avoiding the mutable default argument trap.

Key syntax/rules
    - def fn(a, b=2): — defaults must come after non-default parameters
    - *args collects extra positional args as a tuple; **kwargs as a dict
    - Order in signature: required, *args, keyword-only, **kwargs
    - Call with keywords in any order: fn(b=3, a=1) when names are known
    - Unpack at call site: fn(*list) spreads list; fn(**dict) spreads dict
    - NEVER use mutable defaults (list, dict) — use None and create inside

When to use
    - Default parameters for optional configuration (timeout=30, debug=False)
    - *args/**kwargs in decorators and wrapper functions
    - Keyword arguments for readability when a function has many parameters
    - Unpacking when forwarding arguments to another function

Common mistakes
    - def bad(lst=[]): — same list object reused across all calls
    - Putting required params after *args without keyword-only marker confusion
    - Forgetting that *args is a tuple — don't mutate it expecting caller changes
    - Using **kwargs without validating expected keys in public APIs

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/02_args_kwargs.py
"""


def power(base, exponent=2):  # exponent defaults to 2 if not provided
    return base ** exponent  # return base raised to exponent


def create_user(name, age, city="Unknown"):  # city has a default value
    return {"name": name, "age": age, "city": city}  # return a dict from parameters


def sum_all(*args):  # *args collects extra positional arguments as a tuple
    return sum(args)  # sum all collected positional arguments


def print_info(**kwargs):  # **kwargs collects keyword arguments as a dict
    for key, value in kwargs.items():  # iterate over each keyword argument
        print(f"  {key}: {value}")  # print each key-value pair


def flexible(required, *args, default="x", **kwargs):  # combines all argument forms
    print(f"  required={required}")  # show the required positional argument
    print(f"  args={args}")  # show extra positional arguments as tuple
    print(f"  default={default}")  # show the default parameter value
    print(f"  kwargs={kwargs}")  # show keyword arguments as dict


def bad_append(item, lst=[]):  # DON'T do this — mutable default shared across calls
    lst.append(item)  # same list object reused across all calls
    return lst  # return the shared list


def good_append(item, lst=None):  # DO this instead — None default, fresh list inside
    if lst is None:  # create a new list only when none was provided
        lst = []
    lst.append(item)  # append to the list (fresh or caller-provided)
    return lst  # return the list


def main() -> None:  # entry point that runs all args/kwargs practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Default parameters")  # section title
    print("=" * 50)  # close section header
    print(f"power(3) = {power(3)}")  # call with default exponent (2)
    print(f"power(3, 3) = {power(3, 3)}")  # call with explicit exponent

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Keyword arguments")  # section title
    print("=" * 50)  # close section header
    print(create_user(age=25, name="Bob", city="Delhi"))  # keyword args — order flexible

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — *args variable positional")  # section title
    print("=" * 50)  # close section header
    print(f"sum_all(1,2,3,4) = {sum_all(1, 2, 3, 4)}")  # pass multiple positional args

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — **kwargs variable keyword")  # section title
    print("=" * 50)  # close section header
    print("User info:")  # label the output section
    print_info(name="Alice", role="Admin", active=True)  # pass multiple keyword arguments

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Combine all forms")  # section title
    print("=" * 50)  # close section header
    print("Flexible function:")  # label combined demo
    flexible(1, 2, 3, default="y", extra="z")  # demonstrate all argument types in one call

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Unpacking at call site")  # section title
    print("=" * 50)  # close section header
    nums = [1, 2, 3]  # list of numbers to pass as separate arguments
    print(f"Unpacked: {sum_all(*nums)}")  # *nums unpacks list into positional args
    config = {"name": "App", "version": "1.0"}  # dict to pass as keyword arguments
    print_info(**config)  # **config unpacks dict into keyword arguments

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Mutable default trap")  # section title
    print("=" * 50)  # close section header
    print(f"Bad:  {bad_append('a')}, {bad_append('b')}")  # both calls share same list!
    print(f"Good: {good_append('a')}, {good_append('b')}")  # each call gets its own list

    print("=" * 50)  # print section divider
    print("PRACTICE 8 — Practical: build SQL-style query")  # section title
    print("=" * 50)  # close section header
    def build_query(table: str, *columns, **filters) -> str:  # flexible query builder
        cols = ", ".join(columns) if columns else "*"  # default to * if no columns given
        where = " AND ".join(f"{k}='{v}'" for k, v in filters.items())  # build WHERE clause
        return f"SELECT {cols} FROM {table} WHERE {where}"  # return assembled query string
    query = build_query("users", "name", "email", city="Delhi", active=True)  # build with filters
    print(query)  # show the generated query


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all args/kwargs practice sections
