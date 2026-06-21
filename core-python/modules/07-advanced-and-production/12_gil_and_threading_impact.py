"""
12 — Global Interpreter Lock (GIL)

THEORY
------
What: The GIL is a mutex that allows only one thread to execute Python bytecode at a time
      within a single process.
Why:  Protects CPython's internal structures but limits CPU parallelism in threads.
Key rules:
  - I/O-bound work releases the GIL (threads help); CPU-bound work holds it (threads don't help).
  - Use multiprocessing for CPU parallelism; asyncio or threading for I/O concurrency.
  - Locks protect shared mutable state from race conditions (separate from GIL).
When to use: Choose concurrency model based on I/O vs CPU bound nature of the task.
Common mistakes: Expecting threads to speed up CPU-heavy loops; ignoring race conditions
                 because "Python has a GIL"; not using locks for in-place mutations.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/12_gil_and_threading_impact.py
"""

import threading  # thread-based concurrency primitives


counter = 0  # shared mutable counter accessed by multiple threads
lock = threading.Lock()  # mutex protecting counter in safe demo


def increment_unsafe(n: int) -> None:  # increment shared counter without synchronization
    global counter  # refer to module-level counter
    for _ in range(n):  # repeat n times
        counter += 1  # NOT atomic — race condition without lock


def increment_safe(n: int) -> None:  # increment shared counter under lock
    global counter  # refer to module-level counter
    for _ in range(n):  # repeat n times
        with lock:  # acquire lock around non-atomic read-modify-write
            counter += 1


def demo_race_condition() -> None:  # show lost updates from concurrent increments
    global counter
    counter = 0  # reset counter before demo
    threads = [threading.Thread(target=increment_unsafe, args=(100_000,)) for _ in range(4)]  # four racing threads
    for t in threads:  # start all threads
        t.start()
    for t in threads:  # wait for completion
        t.join()
    print(f"Unsafe counter (expected 400000): {counter}")  # often less than expected


def demo_with_lock() -> None:  # show correct total with synchronization
    global counter
    counter = 0  # reset counter before demo
    threads = [threading.Thread(target=increment_safe, args=(100_000,)) for _ in range(4)]  # four synchronized threads
    for t in threads:  # start all threads
        t.start()
    for t in threads:  # wait for completion
        t.join()
    print(f"Safe counter (expected 400000):   {counter}")  # should reach exact expected total


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Race condition without lock")  # section header
    print("=" * 50)  # close header divider
    demo_race_condition()  # run unsafe increment demo

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Safe increment with Lock")  # section header
    print("=" * 50)  # close header divider
    demo_with_lock()  # run lock-protected increment demo

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Key takeaway")  # section header
    print("=" * 50)  # close header divider
    print("  I/O-bound  → threading or asyncio")  # guidance for I/O work
    print("  CPU-bound  → multiprocessing")  # guidance for CPU work
    print("  GIL        → limits CPU parallelism in threads")  # GIL limitation note


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
