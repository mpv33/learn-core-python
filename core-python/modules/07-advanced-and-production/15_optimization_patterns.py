"""
15 — Optimization Patterns (Industry Standard)

THEORY
------
What: Production-proven techniques — __slots__, local variable binding, built-ins,
      str.join, set lookups, and generators for memory efficiency.
Why:  Apply optimizations in priority order: algorithm > data structure > memory > micro-opts.
Key rules:
  - Correct algorithm first (O(n) vs O(n²)); then right data structure (set vs list).
  - Use sum(), any(), str.join() — implemented in C, faster than manual loops.
  - Profile before micro-optimizing; readability matters unless hot path is proven.
When to use: Hot paths identified by profiling; high-volume objects; large file processing.
Common mistakes: Optimizing cold code; sacrificing readability for negligible gains;
                 using list for membership tests on large collections.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/15_optimization_patterns.py
"""

import sys  # object size introspection


class PointSlots:  # memory-efficient point using __slots__
    __slots__ = ("x", "y")  # fixed attribute set per instance

    def __init__(self, x: float, y: float):  # initialize coordinates
        self.x, self.y = x, y


class PointRegular:  # conventional point with dynamic __dict__
    def __init__(self, x: float, y: float):  # initialize coordinates
        self.x, self.y = x, y


GLOBAL_LIST = list(range(1000))  # module-level list used in benchmark


def sum_with_global() -> int:  # reads GLOBAL_LIST directly each iteration
    return sum(x * 2 for x in GLOBAL_LIST)


def sum_with_local() -> int:  # bind global to local name once
    data = GLOBAL_LIST  # local lookup is faster in hot loops
    return sum(x * 2 for x in data)


VALID_IDS = frozenset({"E001", "E002", "E003"})  # immutable set for fast lookup


def is_valid(emp_id: str) -> bool:  # check membership in constant time
    return emp_id in VALID_IDS


def read_large_file_lines(path: str):  # stream file lines lazily
    with open(path) as f:  # open file context manager
        for line in f:  # iterate one line at a time
            yield line.strip()  # yield cleaned line without loading whole file


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — __slots__ memory savings")  # section header
    print("=" * 50)  # close header divider
    p1, p2 = PointSlots(1, 2), PointRegular(1, 2)  # create comparable instances
    print(f"PointSlots size:   {sys.getsizeof(p1)} bytes")  # typically smaller per instance
    print(f"PointRegular size: {sys.getsizeof(p2)} bytes")  # includes __dict__ overhead

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Local vs global lookup")  # section header
    print("=" * 50)  # close header divider
    print(f"Global sum: {sum_with_global()}")  # demonstrate global access pattern
    print(f"Local sum:  {sum_with_local()}")  # demonstrate local binding pattern

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — str.join vs += in loop")  # section header
    print("=" * 50)  # close header divider
    parts = ["Hello", "World", "Python"]  # strings to concatenate
    efficient = " ".join(parts)  # O(n) join vs repeated concatenation
    print(f"join: {efficient}")  # show joined result

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Set O(1) membership")  # section header
    print("=" * 50)  # close header divider
    print(f"Valid E001: {is_valid('E001')}")  # True for known employee id
    print(f"Valid E999: {is_valid('E999')}")  # False for unknown id

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Optimization hierarchy")  # section header
    print("=" * 50)  # close header divider
    print("  1. Correct algorithm (O(n) vs O(n²))")  # priority 1
    print("  2. Right data structure (set vs list lookup)")  # priority 2
    print("  3. Generators for memory")  # priority 3
    print("  4. Built-ins and C extensions")  # priority 4
    print("  5. Micro-optimizations (last resort)")  # priority 5


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
