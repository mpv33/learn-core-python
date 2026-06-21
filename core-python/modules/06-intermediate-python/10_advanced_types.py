"""
10 — Advanced Type Hints

THEORY
------
What: Richer typing constructs — Optional, Union, Callable, Literal, TypeAlias, Protocols.
Why:  Express nullable returns, function signatures, fixed string sets, and reusable aliases.
Key rules:
  - Optional[T] means T | None; prefer X | None in Python 3.10+.
  - Callable[[ArgTypes], ReturnType] for function parameters.
  - Literal["a", "b"] restricts to specific values; TypeAlias (type X = ...) names complex types.
When to use: APIs with nullable returns, callbacks, config modes, shared type definitions.
Common mistakes: Using Any instead of a precise type; Optional when value is never None;
                 mixing old typing module imports with modern built-in generics.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/10_advanced_types.py
"""

from typing import Optional, Union, Callable, Any, Literal  # legacy/advanced typing helpers
from collections.abc import Sequence  # abstract collection protocol


def find_user(user_id: int) -> Optional[dict]:  # returns dict when found, else None
    users = {1: {"name": "Alice"}}  # tiny in-memory user table
    return users.get(user_id)  # None if key missing


def format_id(value: Union[int, str]) -> str:  # accept int or str input
    return str(value).zfill(5)  # zero-pad string form to width 5


def apply_twice(func: Callable[[int], int], value: int) -> int:  # func takes int, returns int
    return func(func(value))  # apply function twice


def increment(n: int) -> int:  # simple int -> int function
    return n + 1  # add one


def sum_sequence(nums: Sequence[int]) -> int:  # accept any integer sequence
    return sum(nums)  # add all elements


type UserId = int  # alias for user identifier type (Python 3.12+)
type UserData = dict[str, str | int]  # alias for user record shape


def load_user(uid: UserId) -> UserData:  # use aliases in signatures
    return {"id": uid, "name": "Alice"}  # sample user payload


Mode = Literal["read", "write", "append"]  # allowed file open modes


def open_file(path: str, mode: Mode) -> str:  # mode must be one of three literals
    return f"Opened {path} in {mode} mode"  # pretend open operation


def legacy_func(data: Any) -> Any:  # opts out of static checking
    return data  # pass through unchanged


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Optional (nullable return)")  # section header
    print("=" * 50)  # close header divider
    print(f"Found: {find_user(1)}")  # existing user id
    print(f"Not found: {find_user(99)}")  # missing user returns None

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Union types")  # section header
    print("=" * 50)  # close header divider
    print(f"format_id(42) = {format_id(42)}")  # pad integer converted to string
    print(f"format_id('7') = {format_id('7')}")  # pad string directly

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Callable")  # section header
    print("=" * 50)  # close header divider
    print(f"apply_twice(increment, 5) = {apply_twice(increment, 5)}")  # 5 -> 6 -> 7

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Sequence and TypeAlias")  # section header
    print("=" * 50)  # close header divider
    print(f"sum_sequence: {sum_sequence([1, 2, 3, 4])}")  # sum list elements
    print(f"load_user: {load_user(1)}")  # demonstrate alias usage

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Literal restricted values")  # section header
    print("=" * 50)  # close header divider
    print(open_file("data.txt", "read"))  # valid literal mode

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Any escape hatch")  # section header
    print("=" * 50)  # close header divider
    print(f"legacy_func(42) = {legacy_func(42)}")  # Any accepts anything


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
