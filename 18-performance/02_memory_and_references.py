"""
02 — Memory Model: References, id(), gc
========================================
Python uses reference counting + cyclic garbage collector.
"""

import sys
import gc

a = [1, 2, 3]
b = a  # both reference same list object

print(f"id(a) == id(b): {id(a) == id(b)}")
print(f"refcount(a): {sys.getrefcount(a) - 1}")  # -1 for getrefcount arg

del b
print(f"After del b, refcount: {sys.getrefcount(a) - 1}")

# Circular reference — gc handles this
class Node:
    def __init__(self):
        self.ref = None

n1, n2 = Node(), Node()
n1.ref = n2
n2.ref = n1

print(f"\nGC counts before del: {gc.get_count()}")
del n1, n2
gc.collect()
print(f"GC collected unreachable cycles")

# Memory size of objects
print(f"\nsizeof int:     {sys.getsizeof(42)} bytes")
print(f"sizeof list(0): {sys.getsizeof([])} bytes")
print(f"sizeof list(1000): ~{sys.getsizeof(list(range(1000)))} bytes")

# Interning small strings
s1 = "hello"
s2 = "hello"
print(f"\nString interning: s1 is s2 → {s1 is s2}")
