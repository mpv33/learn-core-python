"""
06 — Multiprocessing (CPU-bound tasks)

THEORY
------
What: multiprocessing spawns separate Python processes, each with its own GIL, enabling
      true CPU parallelism for compute-heavy tasks.
Why:  Threads cannot parallelize CPU work due to the GIL; processes bypass this limit.
Key rules:
  - Always guard with if __name__ == "__main__": on Windows/macOS (spawn start method).
  - Pool.map(func, iterable) distributes work across worker processes.
  - Inter-process communication via Queue, Pipe, or shared memory (more overhead).
When to use: Prime counting, image processing, data crunching, ML preprocessing.
Common mistakes: Missing __main__ guard; sharing mutable state without proper IPC;
                 using processes for tiny tasks (overhead exceeds benefit).

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/06_multiprocessing.py
"""

from multiprocessing import Pool, cpu_count  # process pool and core count utilities
import math  # sqrt for primality check optimization
import time  # measure elapsed runtime


def is_prime(n):  # test whether n is a prime number
    if n < 2:  # numbers below 2 are not prime
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:  # found a divisor — not prime
            return False
    return True  # no divisors found — prime


def count_primes(limit):  # count primes strictly below limit
    return sum(1 for n in range(2, limit) if is_prime(n))


def count_range(bounds):  # count primes within one sub-range
    start, end = bounds  # unpack range boundaries
    return sum(1 for n in range(max(2, start), end) if is_prime(n))


def main() -> None:  # entry point for all practice demos
    LIMIT = 50_000  # upper bound for prime counting benchmark

    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Sequential prime counting")  # section header
    print("=" * 50)  # close header divider
    start = time.perf_counter()  # high-resolution timer start
    result_seq = count_primes(LIMIT)  # run prime count in single process
    time_seq = time.perf_counter() - start  # elapsed sequential time
    print(f"Sequential: {result_seq} primes in {time_seq:.3f}s")  # report sequential result

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Parallel with Pool")  # section header
    print("=" * 50)  # close header divider
    chunks = 4  # split work into four ranges
    chunk_size = LIMIT // chunks  # size of each numeric range
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(chunks)]  # build range tuples
    start = time.perf_counter()  # timer start for parallel run
    with Pool(processes=cpu_count()) as pool:  # create pool using all CPU cores
        results = pool.map(count_range, ranges)  # distribute ranges across workers
    result_par = sum(results)  # combine partial counts from all workers
    time_par = time.perf_counter() - start  # elapsed parallel time
    print(f"Parallel:   {result_par} primes in {time_par:.3f}s")  # report parallel result
    print(f"CPU cores:  {cpu_count()}")  # show available worker processes


if __name__ == "__main__":  # required guard for spawning processes safely
    main()  # start all practice sections
