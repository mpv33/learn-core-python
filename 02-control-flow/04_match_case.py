"""
04 — match / case (Python 3.10+)
==================================
Structural pattern matching — like switch/case but more powerful.
"""

def describe_http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case code if 400 <= code < 500:
            return f"Client Error ({code})"
        case _:
            return "Unknown Status"

for code in [200, 404, 418, 500, 999]:
    print(f"  {code}: {describe_http_status(code)}")

# --- Match with tuples ---
print("\nPoint classification:")
points = [(0, 0), (1, 0), (3, 4)]

for x, y in points:
    match (x, y):
        case (0, 0):
            print(f"  ({x},{y}) → Origin")
        case (0, _):
            print(f"  ({x},{y}) → On Y-axis")
        case (_, 0):
            print(f"  ({x},{y}) → On X-axis")
        case (a, b) if a == b:
            print(f"  ({x},{y}) → On diagonal")
        case _:
            print(f"  ({x},{y}) → General point")

# --- Match with lists ---
print("\nList patterns:")
def head_tail(lst):
    match lst:
        case []:
            return "Empty list"
        case [single]:
            return f"One item: {single}"
        case [first, *rest]:
            return f"First: {first}, Rest: {rest}"

print(head_tail([]))
print(head_tail([42]))
print(head_tail([1, 2, 3, 4]))
