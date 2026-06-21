"""02 — collections module"""

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter
votes = ["apple", "banana", "apple", "cherry", "apple", "banana"]
counts = Counter(votes)
print(f"Counts: {counts}")
print(f"Most common: {counts.most_common(2)}")
print(f"apple count: {counts['apple']}")

# defaultdict — auto-create missing keys
word_map = defaultdict(list)
for word in ["cat", "car", "bat", "bar"]:
    word_map[word[0]].append(word)
print(f"\nBy first letter: {dict(word_map)}")

# deque — double-ended queue (O(1) append/pop both ends)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"Deque: {dq}")
print(f"popleft: {dq.popleft()}, pop: {dq.pop()}")

# namedtuple — lightweight immutable objects
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\nPoint: {p}, x={p.x}, as dict: {p._asdict()}")

# OrderedDict (less needed since 3.7 — regular dict preserves order)
od = OrderedDict([("a", 1), ("b", 2)])
print(f"OrderedDict: {od}")

# ChainMap — layered dicts
from collections import ChainMap
defaults = {"color": "red", "size": "M"}
user = {"color": "blue"}
config = ChainMap(user, defaults)
print(f"\nChainMap color: {config['color']}, size: {config['size']}")
