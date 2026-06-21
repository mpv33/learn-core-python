"""
14 — Profiling with timeit and cProfile

THEORY
------
What: timeit micro-benchmarks small code snippets; cProfile records function-level call
      counts and cumulative time for an entire program run.
Why:  Measure before optimizing — data-driven decisions beat guessing bottlenecks.
Key rules:
  - timeit.timeit(stmt, setup, number=N) runs stmt N times; divide for per-run time.
  - cProfile: python -m cProfile script.py or Profile().enable()/disable() in code.
  - Sort by cumulative time to find the real bottlenecks, not just leaf functions.
When to use: Before optimization sprints, comparing algorithm implementations, CI perf regression.
Common mistakes: Optimizing without profiling; micro-benchmarking unrepresentative snippets;
                 ignoring I/O in benchmarks; premature optimization.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/14_profiling_timeit.py
"""

import timeit  # micro-benchmark timing utility
import cProfile  # function-level profiler
import pstats  # format and sort profiling statistics
from io import StringIO  # capture profiler output in memory


def process_data(n: int) -> int:  # CPU work to profile
    total = 0  # accumulator
    for i in range(n):  # loop over range
        total += i ** 2  # add squared value
    return total  # return sum of squares


def main_work() -> None:  # repeatedly call process_data
    for _ in range(100):  # invoke workload 100 times
        process_data(5000)  # process 5000 integers each call


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — timeit micro-benchmark")  # section header
    print("=" * 50)  # close header divider
    list_time = timeit.timeit("[x**2 for x in range(1000)]", number=10000)  # benchmark list comp
    gen_time = timeit.timeit("(x**2 for x in range(1000))", number=10000)  # benchmark generator
    print(f"  list comp: {list_time:.4f}s")  # total seconds for list comp runs
    print(f"  generator: {gen_time:.4f}s")  # total seconds for generator runs

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Compare approaches with timeit")  # section header
    print("=" * 50)  # close header divider
    setup = "data = list(range(10000))"  # shared setup code for both benchmarks
    stmt_loop = "sum(x*2 for x in data)"  # generator expression summation
    stmt_map = "sum(map(lambda x: x*2, data))"  # map-based summation
    t1 = timeit.timeit(stmt_loop, setup=setup, number=1000)  # time generator approach
    t2 = timeit.timeit(stmt_map, setup=setup, number=1000)  # time map approach
    print(f"  gen expr: {t1:.4f}s")  # report generator timing
    print(f"  map():    {t2:.4f}s")  # report map timing

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — cProfile function-level profiling")  # section header
    print("=" * 50)  # close header divider
    profiler = cProfile.Profile()  # create profiler instance
    profiler.enable()  # start collecting profile data
    main_work()  # run workload under profiling
    profiler.disable()  # stop collecting profile data
    stream = StringIO()  # in-memory text buffer for stats output
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")  # sort by cumulative time
    stats.print_stats(5)  # print top 5 functions by cumulative time
    print("cProfile top 5:")  # section header
    print(stream.getvalue())  # display captured profiler report


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
