"""02 — Multiprocessing (CPU-bound tasks)"""

from multiprocessing import Pool, cpu_count
import math
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    return sum(1 for n in range(2, limit) if is_prime(n))

LIMIT = 50_000

# Sequential
start = time.perf_counter()
result_seq = count_primes(LIMIT)
time_seq = time.perf_counter() - start
print(f"Sequential: {result_seq} primes in {time_seq:.3f}s")

# Parallel with Pool
if __name__ == "__main__":
    chunks = 4
    chunk_size = LIMIT // chunks
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(chunks)]

    def count_range(bounds):
        start, end = bounds
        return sum(1 for n in range(max(2, start), end) if is_prime(n))

    start = time.perf_counter()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(count_range, ranges)
    result_par = sum(results)
    time_par = time.perf_counter() - start
    print(f"Parallel:   {result_par} primes in {time_par:.3f}s")
    print(f"CPU cores:  {cpu_count()}")

# Note: multiprocessing requires if __name__ == "__main__" guard on Windows/macOS
