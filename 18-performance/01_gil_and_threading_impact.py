"""
01 — Global Interpreter Lock (GIL)
===================================
The GIL allows only ONE thread to execute Python bytecode at a time.
Impact: threads help I/O-bound work, NOT CPU-bound parallelism.
Use multiprocessing for CPU-bound tasks.
"""

import threading
import time

counter = 0
lock = threading.Lock()

def increment_unsafe(n: int) -> None:
    global counter
    for _ in range(n):
        counter += 1  # NOT atomic — race condition without lock

def increment_safe(n: int) -> None:
    global counter
    for _ in range(n):
        with lock:
            counter += 1

def demo_race_condition() -> None:
    global counter
    counter = 0
    threads = [threading.Thread(target=increment_unsafe, args=(100_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Unsafe counter (expected 400000): {counter}")

def demo_with_lock() -> None:
    global counter
    counter = 0
    threads = [threading.Thread(target=increment_safe, args=(100_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Safe counter (expected 400000):   {counter}")

print("GIL + Race Condition Demo")
print("-" * 40)
demo_race_condition()
demo_with_lock()

print("\nKey takeaway:")
print("  I/O-bound  → threading or asyncio")
print("  CPU-bound  → multiprocessing")
print("  GIL        → limits CPU parallelism in threads")
