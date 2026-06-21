"""05 — Magic (Dunder) Methods"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable (print)"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Developer-readable (debug)"""
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)               # __str__
print(repr(v1))         # __repr__
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}")

# Context manager methods
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        import time
        elapsed = time.perf_counter() - self.start
        print(f"  Elapsed: {elapsed:.4f}s")

with Timer():
    total = sum(range(1_000_000))

# Callable objects
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

times3 = Multiplier(3)
print(f"\ntimes3(7) = {times3(7)}")

# Container methods
class Playlist:
    def __init__(self):
        self._songs = []

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def add(self, song):
        self._songs.append(song)

pl = Playlist()
pl.add("Song A")
pl.add("Song B")
print(f"\nPlaylist: {len(pl)} songs, first: {pl[0]}")
