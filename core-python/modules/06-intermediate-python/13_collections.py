"""
13 — collections module

THEORY
------
What: Specialized container datatypes beyond built-in list, dict, and set — Counter,
      defaultdict, deque, namedtuple, ChainMap, and OrderedDict.
Why:  Solve common patterns (counting, grouping, queues, lightweight records) efficiently.
Key rules:
  - Counter: multiset counts; supports most_common(), arithmetic.
  - defaultdict(factory): auto-creates missing keys with factory().
  - deque: O(1) append/pop at both ends; use for queues and sliding windows.
When to use: Frequency analysis, grouping by key, BFS queues, fixed-field records.
Common mistakes: Using list as queue (O(n) pop(0)); defaultdict hiding KeyError bugs;
                 OrderedDict when regular dict suffices (3.7+ preserves order).

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/13_collections.py
"""

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap  # container types


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Counter")  # section header
    print("=" * 50)  # close header divider
    votes = ["apple", "banana", "apple", "cherry", "apple", "banana"]  # sample vote list
    counts = Counter(votes)  # tally occurrences of each item
    print(f"Counts: {counts}")  # show full frequency mapping
    print(f"Most common: {counts.most_common(2)}")  # show top two most frequent items
    print(f"apple count: {counts['apple']}")  # look up count for a specific key

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — defaultdict")  # section header
    print("=" * 50)  # close header divider
    word_map = defaultdict(list)  # dict that auto-creates empty lists for new keys
    for word in ["cat", "car", "bat", "bar"]:  # iterate sample words
        word_map[word[0]].append(word)  # group each word under its first letter
    print(f"By first letter: {dict(word_map)}")  # convert defaultdict to plain dict

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — deque")  # section header
    print("=" * 50)  # close header divider
    dq = deque([1, 2, 3])  # create deque from initial sequence
    dq.appendleft(0)  # insert element at the left end
    dq.append(4)  # insert element at the right end
    print(f"Deque: {dq}")  # show deque after both-end inserts
    print(f"popleft: {dq.popleft()}, pop: {dq.pop()}")  # remove from left then right

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — namedtuple")  # section header
    print("=" * 50)  # close header divider
    Point = namedtuple("Point", ["x", "y"])  # define a fixed-field record type
    p = Point(3, 4)  # instantiate a point with coordinates
    print(f"Point: {p}, x={p.x}, as dict: {p._asdict()}")  # access fields and convert to dict

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — OrderedDict")  # section header
    print("=" * 50)  # close header divider
    od = OrderedDict([("a", 1), ("b", 2)])  # ordered mapping from key-value pairs
    print(f"OrderedDict: {od}")  # print ordered dict contents

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — ChainMap")  # section header
    print("=" * 50)  # close header divider
    defaults = {"color": "red", "size": "M"}  # fallback configuration values
    user = {"color": "blue"}  # user overrides only some defaults
    config = ChainMap(user, defaults)  # search user first, then defaults
    print(f"ChainMap color: {config['color']}, size: {config['size']}")  # resolved values


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
