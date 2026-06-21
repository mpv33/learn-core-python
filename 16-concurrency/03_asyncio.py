"""03 — Asyncio (async/await for I/O)"""

import asyncio
import time

async def fetch_data(name, delay):
    print(f"  [{name}] Starting fetch...")
    await asyncio.sleep(delay)  # non-blocking wait
    print(f"  [{name}] Done!")
    return f"{name}: data"

async def main():
    print("Sequential async (slow):")
    start = time.perf_counter()
    r1 = await fetch_data("API-1", 0.3)
    r2 = await fetch_data("API-2", 0.3)
    print(f"  Results: {r1}, {r2}")
    print(f"  Time: {time.perf_counter() - start:.2f}s\n")

    print("Concurrent async (fast):")
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch_data("API-1", 0.3),
        fetch_data("API-2", 0.3),
        fetch_data("API-3", 0.3),
    )
    print(f"  Results: {results}")
    print(f"  Time: {time.perf_counter() - start:.2f}s\n")

    # asyncio.create_task for fire-and-forget
    print("Tasks:")
    task1 = asyncio.create_task(fetch_data("Task-A", 0.2))
    task2 = asyncio.create_task(fetch_data("Task-B", 0.1))
    await task1
    await task2

    # Timeout
    try:
        await asyncio.wait_for(fetch_data("Slow", 5), timeout=0.5)
    except asyncio.TimeoutError:
        print("\n  Timed out as expected.")

async def producer(queue):
    for i in range(3):
        await asyncio.sleep(0.1)
        await queue.put(i)
        print(f"  Produced: {i}")
    await queue.put(None)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"  Consumed: {item}")

async def queue_demo():
    print("\nQueue demo:")
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(queue_demo())
