"""
05 — Magic (Dunder) Methods
============================

THEORY
------
What:
  Dunder (double-underscore) methods like `__str__`, `__add__`, and `__len__` hook
  your class into Python's built-in operators and functions. They make custom
  objects feel like built-in types.

Why:
  Enable intuitive syntax (`v1 + v2`, `print(obj)`, `len(obj)`) and integrate with
  Python protocols (context managers, callables, containers).

Key rules:
  - `__str__` → human-readable (used by `print()`); `__repr__` → developer/debug form.
  - `__add__`, `__eq__`, `__lt__` enable operators (+, ==, <).
  - `__enter__` / `__exit__` make objects work with `with` statements.
  - `__call__` makes an instance callable like a function.
  - `__len__` / `__getitem__` make objects behave like sequences.

When to use:
  - Value objects (Vector, Money, DateRange) that support arithmetic or comparison.
  - Resource wrappers (Timer, FileLock) for context manager cleanup.
  - Callable config objects or functors that store state between calls.

Common mistakes:
  - Implementing `__eq__` without `__hash__` — instances become unhashable (can't use in sets).
  - Returning wrong types from operators (e.g., `__add__` should return a new instance).
  - Putting heavy logic in `__str__`/`__repr__` — keep them fast and side-effect free.

PRACTICE
--------
Run: python3 core-python/modules/04-object-oriented-programming/05_magic_methods.py
"""

import math  # sqrt for Vector magnitude
import time  # perf_counter for Timer context manager


class Vector:
    def __init__(self, x, y):
        self.x = x  # x component
        self.y = y  # y component

    def __str__(self):
        return f"Vector({self.x}, {self.y})"  # human-readable for print()

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"  # unambiguous for debugging

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)  # enable v1 + v2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  # enable v1 == v2

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))  # magnitude as integer

    def __getitem__(self, index):
        return (self.x, self.y)[index]  # enable v1[0] and v1[1] indexing


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()  # record start time on context entry
        return self  # returned object is bound to `as` target (optional)

    def __exit__(self, *args):
        elapsed = time.perf_counter() - self.start  # compute elapsed seconds
        print(f"  Elapsed: {elapsed:.4f}s")  # report timing when block exits


class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # store multiplication factor

    def __call__(self, x):
        return x * self.factor  # enable times3(7) callable syntax


class Playlist:
    def __init__(self):
        self._songs = []  # internal list backing the playlist

    def __len__(self):
        return len(self._songs)  # enable len(pl) on the playlist

    def __getitem__(self, index):
        return self._songs[index]  # enable pl[0] indexing

    def __contains__(self, song):
        return song in self._songs  # enable "Song A" in pl membership test

    def add(self, song):
        self._songs.append(song)  # append a track to the internal list


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — __str__, __repr__, and operators")  # label first block
    print("=" * 50)  # close header

    v1 = Vector(3, 4)  # first vector instance
    v2 = Vector(1, 2)  # second vector instance
    print(v1)  # uses __str__
    print(repr(v1))  # uses __repr__
    print(f"v1 + v2 = {v1 + v2}")  # uses __add__
    print(f"v1 == v2: {v1 == v2}")  # uses __eq__
    print(f"len(v1): {len(v1)}")  # uses __len__ — magnitude 5
    print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")  # uses __getitem__

    print("\n" + "=" * 50)  # divider before context manager demo
    print("PRACTICE 2 — Context manager (__enter__ / __exit__)")  # label second block
    print("=" * 50)  # close header

    with Timer():  # __enter__ starts timer; __exit__ prints elapsed
        total = sum(range(1_000_000))  # timed computation inside with block
    print(f"  Sum result: {total}")  # show computation completed

    print("\n" + "=" * 50)  # divider before callable demo
    print("PRACTICE 3 — Callable objects (__call__)")  # label third block
    print("=" * 50)  # close header

    times3 = Multiplier(3)  # create callable multiplier object
    double = Multiplier(2)  # second callable with different factor
    print(f"times3(7) = {times3(7)}")  # call instance like a function
    print(f"double(10) = {double(10)}")  # another callable demo

    print("\n" + "=" * 50)  # divider before container demo
    print("PRACTICE 4 — Container methods (__len__, __getitem__, __contains__)")  # label fourth block
    print("=" * 50)  # close header

    pl = Playlist()  # empty playlist
    pl.add("Song A")  # add first track
    pl.add("Song B")  # add second track
    print(f"Playlist: {len(pl)} songs, first: {pl[0]}")  # len and indexing via dunders
    print(f"'Song A' in playlist: {'Song A' in pl}")  # membership via __contains__


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
