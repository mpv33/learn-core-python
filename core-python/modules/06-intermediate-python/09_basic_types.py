"""
09 — Basic Type Hints

THEORY
------
What: Annotations on parameters, return values, and variables that describe expected types.
Why:  Improve readability, enable static analysis (mypy), and document APIs for teammates.
Key rules:
  - Syntax: def fn(x: int) -> str: ...
  - Python 3.10+: use list[str], dict[str, int], str | int instead of List, Dict, Union.
  - Hints are NOT enforced at runtime — they are for tools and humans.
When to use: Public functions, class attributes, complex data shapes; pair with mypy/pyright.
Common mistakes: Treating hints as runtime validation; overusing Any; inconsistent hint style.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/09_basic_types.py
"""


def greet(name: str) -> str:  # parameter and return types annotated
    return f"Hello, {name}!"  # returns str as annotated


def add(a: int, b: int) -> int:  # both operands expected to be integers
    return a + b  # integer addition


def process_items(items: list[str]) -> list[int]:  # list of strings in, list of ints out
    return [len(item) for item in items]  # map each string to its length


def get_user(user_id: int) -> dict[str, str | int | bool]:  # dict with mixed value types
    return {"id": user_id, "name": "Alice", "active": True}  # sample user record


def broken(a: int) -> int:  # annotated to return int
    return "not an int"  # mypy would flag this — runtime allows it


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Function type annotations")  # section header
    print("=" * 50)  # close header divider
    print(greet("World"))  # call typed greeting function
    print(f"add(3, 5) = {add(3, 5)}")  # demonstrate integer addition
    print(f"process_items: {process_items(['hi', 'hello'])}")  # show length mapping
    print(f"get_user: {get_user(1)}")  # show typed dict return value

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Variable annotations")  # section header
    print("=" * 50)  # close header divider
    count: int = 0  # annotate variable as integer
    names: list[str] = ["Alice", "Bob"]  # list expected to hold strings
    config: dict[str, bool | int] = {"debug": True, "port": 8080}  # mixed value types
    print(f"count={count}, names={names}, config={config}")  # display annotated variables

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Hints are not enforced at runtime")  # section header
    print("=" * 50)  # close header divider
    result = broken(5)  # Python does not validate return type at runtime
    print(f"Runtime allows wrong return: {result!r} (type: {type(result).__name__})")  # str returned

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Annotate a simple data pipeline")  # section header
    print("=" * 50)  # close header divider
    raw: list[str] = ["  hello ", " WORLD ", "  Python  "]  # messy input strings
    cleaned: list[str] = [s.strip().lower() for s in raw]  # typed transform pipeline
    print(f"Cleaned: {cleaned}")  # show normalized output


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
