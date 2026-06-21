"""
03 — Profiling with timeit and cProfile
========================================
Measure before optimizing. Premature optimization is the root of all evil.
"""

import timeit
import cProfile
import pstats
from io import StringIO

# timeit — micro-benchmark
list_time = timeit.timeit("[x**2 for x in range(1000)]", number=10000)
gen_time = timeit.timeit("(x**2 for x in range(1000))", number=10000)
print("timeit (10000 iterations):")
print(f"  list comp: {list_time:.4f}s")
print(f"  generator: {gen_time:.4f}s")

# Compare approaches
setup = "data = list(range(10000))"
stmt_loop = "sum(x*2 for x in data)"
stmt_map = "sum(map(lambda x: x*2, data))"

t1 = timeit.timeit(stmt_loop, setup=setup, number=1000)
t2 = timeit.timeit(stmt_map, setup=setup, number=1000)
print(f"\n  gen expr: {t1:.4f}s")
print(f"  map():    {t2:.4f}s")

# cProfile — function-level profiling
def process_data(n: int) -> int:
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def main_work() -> None:
    for _ in range(100):
        process_data(5000)

profiler = cProfile.Profile()
profiler.enable()
main_work()
profiler.disable()

stream = StringIO()
stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
stats.print_stats(5)
print("\ncProfile top 5:")
print(stream.getvalue())
