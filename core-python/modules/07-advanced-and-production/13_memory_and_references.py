"""
13 — Memory Model: References, id(), gc

THEORY
------
What: Python manages memory via reference counting plus a cyclic garbage collector;
      variables are names bound to objects, not boxes holding values.
Why:  Understanding references prevents bugs with mutable defaults, aliasing, and leaks.
Key rules:
  - Assignment binds a name to an object; no copying unless you copy explicitly.
  - id(obj) is the object's identity; a is b means same object (id(a) == id(b)).
  - gc.collect() reclaims unreachable cyclic objects reference counting misses.
When to use: Debugging unexpected mutations, memory leaks, understanding is vs ==.
Common mistakes: Assuming assignment copies; mutating shared list/dict unintentionally;
                 relying on del to free memory immediately (refcount drops, GC may lag).

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/13_memory_and_references.py
"""

import sys  # introspection helpers like getrefcount and getsizeof
import gc  # cyclic garbage collector interface


class Node:  # node that can point to another node
    def __init__(self):  # initialize empty reference
        self.ref = None


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Shared references")  # section header
    print("=" * 50)  # close header divider
    a = [1, 2, 3]  # create list object
    b = a  # both reference same list object
    print(f"id(a) == id(b): {id(a) == id(b)}")  # True when variables alias same object
    print(f"refcount(a): {sys.getrefcount(a) - 1}")  # -1 for getrefcount arg
    del b  # remove one reference to the list
    print(f"After del b, refcount: {sys.getrefcount(a) - 1}")  # refcount drops by one

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Cyclic garbage collection")  # section header
    print("=" * 50)  # close header divider
    n1, n2 = Node(), Node()  # create two nodes
    n1.ref = n2  # n1 points to n2
    n2.ref = n1  # n2 points back to n1 — cycle formed
    print(f"GC counts before del: {gc.get_count()}")  # show GC generation counts
    del n1, n2  # remove external references leaving cyclic pair unreachable
    gc.collect()  # force collection of cyclic garbage
    print("GC collected unreachable cycles")  # confirm GC ran

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Object sizes")  # section header
    print("=" * 50)  # close header divider
    print(f"sizeof int:     {sys.getsizeof(42)} bytes")  # size of small int object
    print(f"sizeof list(0): {sys.getsizeof([])} bytes")  # overhead of empty list
    print(f"sizeof list(1000): ~{sys.getsizeof(list(range(1000)))} bytes")  # list with 1000 ints

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — String interning")  # section header
    print("=" * 50)  # close header divider
    s1 = "hello"  # string literal
    s2 = "hello"  # identical literal may be interned
    print(f"String interning: s1 is s2 → {s1 is s2}")  # often True for small interned strings


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
