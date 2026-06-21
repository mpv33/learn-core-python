"""01 — Basic Type Hints"""

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> list[int]:
    return [len(item) for item in items]

def get_user(user_id: int) -> dict[str, str | int]:
    return {"id": user_id, "name": "Alice", "active": True}

# Variable annotations
count: int = 0
names: list[str] = ["Alice", "Bob"]
config: dict[str, bool | int] = {"debug": True, "port": 8080}

print(greet("World"))
print(f"add(3, 5) = {add(3, 5)}")
print(f"process_items: {process_items(['hi', 'hello'])}")
print(f"get_user: {get_user(1)}")

# Type hints are NOT enforced at runtime
def broken(a: int) -> int:
    return "not an int"  # mypy would flag this

result = broken(5)
print(f"\nRuntime allows wrong return: {result!r} (type: {type(result).__name__})")

# Use reveal_type in mypy for debugging
# reveal_type(greet("test"))
