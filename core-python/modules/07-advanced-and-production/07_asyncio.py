"""
07 — Asyncio (async/await for I/O)

THEORY
------
What: asyncio provides cooperative concurrency via async/await coroutines on a single
      thread event loop — ideal for many concurrent I/O operations.
Why:  Handle thousands of connections with less overhead than one thread per connection.
Key rules:
  - async def defines coroutine; await suspends until result is ready.
  - asyncio.gather() runs coroutines concurrently; create_task() schedules on loop.
  - asyncio.run(main()) starts the event loop (Python 3.7+).
When to use: HTTP clients, websockets, async database drivers, concurrent I/O pipelines.
Common mistakes: Calling blocking code inside async (use run_in_executor); forgetting
                 await; mixing threads and asyncio without care.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/07_asyncio.py
"""

import asyncio  # coroutine-based concurrency library
import time  # measure elapsed wall-clock time


async def fetch_data(name, delay):  # simulate async I/O-bound fetch
    print(f"  [{name}] Starting fetch...")  # log fetch start
    await asyncio.sleep(delay)  # non-blocking wait simulating network latency
    print(f"  [{name}] Done!")  # log fetch completion
    return f"{name}: data"  # return fetched payload label


async def producer(queue):  # put items onto async queue
    for i in range(3):  # produce three numbered items
        await asyncio.sleep(0.1)  # simulate work between items
        await queue.put(i)  # enqueue item
        print(f"  Produced: {i}")  # log production
    await queue.put(None)  # sentinel signals consumer to stop


async def consumer(queue):  # read items from async queue until sentinel
    while True:  # process until stop signal
        item = await queue.get()  # wait for next queue item
        if item is None:  # sentinel received — exit loop
            break
        print(f"  Consumed: {item}")  # log consumption


async def run_demos() -> None:  # primary async demo routine
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Sequential async (slow)")  # section header
    print("=" * 50)  # close header divider
    start = time.perf_counter()  # start timer
    r1 = await fetch_data("API-1", 0.3)  # wait for first fetch to finish
    r2 = await fetch_data("API-2", 0.3)  # then wait for second fetch
    print(f"  Results: {r1}, {r2}")  # show sequential results
    print(f"  Time: {time.perf_counter() - start:.2f}s")  # elapsed ~0.6s

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Concurrent async with gather")  # section header
    print("=" * 50)  # close header divider
    start = time.perf_counter()  # restart timer
    results = await asyncio.gather(  # run three fetches concurrently
        fetch_data("API-1", 0.3),
        fetch_data("API-2", 0.3),
        fetch_data("API-3", 0.3),
    )
    print(f"  Results: {results}")  # show all gathered results
    print(f"  Time: {time.perf_counter() - start:.2f}s")  # elapsed ~0.3s

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — create_task")  # section header
    print("=" * 50)  # close header divider
    task1 = asyncio.create_task(fetch_data("Task-A", 0.2))  # schedule first background task
    task2 = asyncio.create_task(fetch_data("Task-B", 0.1))  # schedule second background task
    await task1  # wait for Task-A completion
    await task2  # wait for Task-B completion

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Timeout with wait_for")  # section header
    print("=" * 50)  # close header divider
    try:  # demonstrate wait_for timeout handling
        await asyncio.wait_for(fetch_data("Slow", 5), timeout=0.5)  # fail if slower than 0.5s
    except asyncio.TimeoutError:  # expected when fetch exceeds timeout
        print("  Timed out as expected.")

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Async queue producer/consumer")  # section header
    print("=" * 50)  # close header divider
    q = asyncio.Queue()  # create unbounded async queue
    await asyncio.gather(producer(q), consumer(q))  # run both coroutines together


def main() -> None:  # entry point for script execution
    asyncio.run(run_demos())  # run all async demos on event loop


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start asyncio event loop
