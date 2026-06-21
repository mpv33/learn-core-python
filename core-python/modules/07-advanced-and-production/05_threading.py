"""
05 — Threading (I/O-bound tasks)

THEORY
------
What: threading runs multiple threads in one process, sharing memory; best for I/O-bound
      work where threads wait on network, disk, or sleep.
Why:  Overlap waiting time — download multiple URLs concurrently without extra processes.
Key rules:
  - threading.Thread(target=func, args=(...)) + start() + join().
  - ThreadPoolExecutor preferred for pools; use Lock for shared mutable state.
  - GIL limits CPU parallelism — use multiprocessing for CPU-bound work.
When to use: Concurrent downloads, socket servers, parallel file I/O, UI responsiveness.
Common mistakes: Using threads for CPU-heavy work; race conditions without locks;
                 daemon threads exiting before work completes.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/05_threading.py
"""

import threading  # low-level thread API
import time  # sleep for simulated I/O delay
from concurrent.futures import ThreadPoolExecutor, as_completed  # high-level thread pool


def download_simulation(name, duration):  # simulate blocking network download
    print(f"  [{name}] Starting...")  # log start of simulated download
    time.sleep(duration)  # block thread to mimic I/O wait
    print(f"  [{name}] Done!")  # log completion
    return f"{name} complete"  # return completion message


class SafeCounter:  # counter protected by a reentrant lock
    def __init__(self):  # initialize counter state and lock
        self._value = 0
        self._lock = threading.Lock()

    def increment(self):  # atomically increment under lock
        with self._lock:  # acquire lock for duration of block
            self._value += 1


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Manual threads")  # section header
    print("=" * 50)  # close header divider
    threads = []  # keep references to started threads
    for site, delay in [("Site-A", 0.2), ("Site-B", 0.3), ("Site-C", 0.1)]:  # three simulated sites
        t = threading.Thread(target=download_simulation, args=(site, delay))  # create thread object
        threads.append(t)  # store thread reference for joining later
        t.start()  # begin concurrent execution
    for t in threads:  # wait for all manual threads to finish
        t.join()
    print("All threads finished.")  # confirm all threads completed

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — ThreadPoolExecutor")  # section header
    print("=" * 50)  # close header divider
    with ThreadPoolExecutor(max_workers=3) as executor:  # pool reuses up to 3 worker threads
        futures = {  # map each future to its task index
            executor.submit(download_simulation, f"Task-{i}", 0.1): i
            for i in range(3)
        }
        for future in as_completed(futures):  # iterate futures as they finish
            print(f"  Result: {future.result()}")  # print each task result

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Thread-safe counter with Lock")  # section header
    print("=" * 50)  # close header divider
    counter = SafeCounter()  # shared counter across threads
    workers = [  # five threads each incrementing 1000 times
        threading.Thread(target=lambda: [counter.increment() for _ in range(1000)])
        for _ in range(5)
    ]
    for w in workers:  # start all worker threads
        w.start()
    for w in workers:  # wait for all workers to finish
        w.join()
    print(f"Safe counter: {counter._value}")  # expect 5000 with proper locking


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
