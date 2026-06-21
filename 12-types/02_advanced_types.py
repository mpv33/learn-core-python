"""02 — Advanced Type Hints"""

from typing import Optional, Union, Callable, Any
from collections.abc import Sequence, Mapping

# Optional — value or None
def find_user(user_id: int) -> Optional[dict]:
    users = {1: {"name": "Alice"}}
    return users.get(user_id)

print(f"Found: {find_user(1)}")
print(f"Not found: {find_user(99)}")

# Union — one of several types (Python 3.10+: use int | str)
def format_id(value: Union[int, str]) -> str:
    return str(value).zfill(5)

print(f"format_id(42) = {format_id(42)}")
print(f"format_id('7') = {format_id('7')}")

# Callable
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def increment(n: int) -> int:
    return n + 1

print(f"apply_twice(increment, 5) = {apply_twice(increment, 5)}")

# Generic collections (Python 3.9+ built-in generics preferred)
def sum_sequence(nums: Sequence[int]) -> int:
    return sum(nums)

print(f"sum_sequence: {sum_sequence([1, 2, 3, 4])}")

# TypeAlias (Python 3.10+)
type UserId = int
type UserData = dict[str, str | int]

def load_user(uid: UserId) -> UserData:
    return {"id": uid, "name": "Alice"}

print(f"load_user: {load_user(1)}")

# Literal — specific values only
from typing import Literal

Mode = Literal["read", "write", "append"]

def open_file(path: str, mode: Mode) -> str:
    return f"Opened {path} in {mode} mode"

print(open_file("data.txt", "read"))

# Any — escape hatch (avoid when possible)
def legacy_func(data: Any) -> Any:
    return data
