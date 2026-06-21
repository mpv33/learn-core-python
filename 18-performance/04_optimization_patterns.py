"""
04 — Optimization Patterns (Industry Standard)
===============================================
Practical patterns used in production codebases.
"""

import sys

# 1. __slots__ — reduce memory for many instances
class PointSlots:
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

class PointRegular:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

p1, p2 = PointSlots(1, 2), PointRegular(1, 2)
print(f"PointSlots size:   {sys.getsizeof(p1)} bytes")
print(f"PointRegular size: {sys.getsizeof(p2)} bytes")

# 2. Local variable lookup is faster than global
GLOBAL_LIST = list(range(1000))

def sum_with_global() -> int:
    return sum(x * 2 for x in GLOBAL_LIST)

def sum_with_local() -> int:
    data = GLOBAL_LIST
    return sum(x * 2 for x in data)

# 3. Use built-in functions — implemented in C
# sum(), min(), max(), any(), all() — prefer over manual loops

# 4. Join strings with str.join — NOT += in loop
parts = ["Hello", "World", "Python"]
efficient = " ".join(parts)  # O(n)
print(f"\njoin: {efficient}")

# 5. Set for O(1) membership vs list O(n)
VALID_IDS = frozenset({"E001", "E002", "E003"})  # immutable set

def is_valid(emp_id: str) -> bool:
    return emp_id in VALID_IDS

print(f"Valid E001: {is_valid('E001')}")

# 6. Generator for large datasets — don't load all into memory
def read_large_file_lines(path: str):
    with open(path) as f:
        for line in f:
            yield line.strip()

print("\nOptimization hierarchy:")
print("  1. Correct algorithm (O(n) vs O(n²))")
print("  2. Right data structure (set vs list lookup)")
print("  3. Generators for memory")
print("  4. Built-ins and C extensions")
print("  5. Micro-optimizations (last resort)")
