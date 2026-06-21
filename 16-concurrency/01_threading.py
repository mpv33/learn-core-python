"""01 — Threading (I/O-bound tasks)"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_simulation(name, duration):
    print(f"  [{name}] Starting...")
    time.sleep(duration)
    print(f"  [{name}] Done!")
    return f"{name} complete"

# Manual threads
print("Manual threads:")
threads = []
for site, delay in [("Site-A", 0.2), ("Site-B", 0.3), ("Site-C", 0.1)]:
    t = threading.Thread(target=download_simulation, args=(site, delay))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All threads finished.\n")

# ThreadPoolExecutor (preferred)
print("ThreadPoolExecutor:")
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {
        executor.submit(download_simulation, f"Task-{i}", 0.1): i
        for i in range(3)
    }
    for future in as_completed(futures):
        print(f"  Result: {future.result()}")

# Thread-safe counter with Lock
class SafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self._value += 1

counter = SafeCounter()
workers = [
    threading.Thread(target=lambda: [counter.increment() for _ in range(1000)])
    for _ in range(5)
]
for w in workers:
    w.start()
for w in workers:
    w.join()
print(f"\nSafe counter: {counter._value}")
