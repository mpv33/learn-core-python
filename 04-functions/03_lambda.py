"""03 — Lambda: small anonymous functions"""

# Basic lambda
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# Often used with sorted, map, filter
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 85},
    {"name": "Carol", "score": 98},
]

by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("Top student:", by_score[0]["name"])

# map — apply function to every item
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(f"Doubled: {doubled}")

# filter — keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Evens: {evens}")

# Lambda with multiple args
add = lambda a, b: a + b
print(f"lambda add: {add(3, 7)}")

# When NOT to use lambda — use def for complex logic
def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

print(f"Valid email: {is_valid_email('user@example.com')}")
