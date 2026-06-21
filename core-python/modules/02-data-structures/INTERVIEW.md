# Module 02 — Interview Prep: Data Structures

> List, tuple, set, dict, copying, time complexity

---

## Theory Questions

**Q1: List vs tuple?**  
List: mutable, slower, more methods. Tuple: immutable, hashable (if elements hashable), faster, used for fixed records.

**Q2: Set vs list for membership test?**  
Set: O(1) average. List: O(n). Always use set for frequent `in` checks on large data.

**Q3: Dict insertion order?**  
Guaranteed since Python 3.7 (implementation detail in 3.6).

**Q4: What makes an object hashable?**  
Must have `__hash__()` and `__eq__()`. Immutable types are hashable. Lists are NOT hashable.

**Q5: Shallow vs deep copy?**  
Shallow: new container, shared inner objects. Deep: recursive copy of all nested objects. Use `copy.copy()` vs `copy.deepcopy()`.

**Q6: Time complexity of list operations?**  
Append: O(1). Insert at index: O(n). Search: O(n). Pop last: O(1). Pop first: O(n).

**Q7: Time complexity of dict/set operations?**  
Average O(1) for lookup, insert, delete. Worst case O(n) due to hash collisions.

**Q8: `defaultdict` vs regular dict?**  
`defaultdict` auto-creates missing keys with a factory function. Avoids KeyError checks.

**Q9: `Counter` use case?**  
Frequency counting. `most_common(n)` returns top n items.

**Q10: `deque` vs list?**  
`deque`: O(1) append/pop both ends. `list`: O(n) for pop(0). Use deque as queue.

**Q11: Can you use a list as dict key?**  
No. Lists are unhashable. Use tuple instead if immutable.

**Q12: How to remove duplicates preserving order?**  
`list(dict.fromkeys(items))`

**Q13: Difference between `append` and `extend`?**  
`append` adds one element (even a list as single item). `extend` adds each element from iterable.

**Q14: What is `namedtuple`?**  
Lightweight tuple subclass with named fields. Immutable, memory efficient.

**Q15: `frozenset` purpose?**  
Immutable set. Can be used as dict key or set element.

**Q16: Dict merge (Python 3.9+)?**  
`d1 | d2` — later keys override earlier.

**Q17: List vs tuple performance?**  
Tuple slightly faster and uses less memory due to immutability.

**Q18: What is slicing `[::-1]`?**  
Reverses sequence. Start: end with step -1.

---

## Coding Questions

**Q19: Two Sum**
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```

**Q20: Merge two sorted lists**
```python
def merge(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    return result + a[i:] + b[j:]
```

**Q21: Group anagrams**
```python
from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    return list(groups.values())
```

**Q22: Find first non-repeating character**
```python
from collections import Counter
def first_unique(s):
    counts = Counter(s)
    for i, c in enumerate(s):
        if counts[c] == 1: return c
    return None
```

**Q23: Rotate list by k**
```python
def rotate(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]
```

**Q24: Intersection of two lists**
```python
def intersection(a, b):
    return list(set(a) & set(b))
```

**Q25: Flatten nested list (one level)**
```python
def flatten(lst):
    return [item for sub in lst for item in sub]
```

---

## Common Pitfalls

- Modifying list while iterating
- Using list as dict key
- Shallow copy when deep copy needed
- `list.sort()` returns None (in-place)
- Confusing `append([1,2])` vs `extend([1,2])`

---

## Quick Checklist

- [ ] State Big-O for list, dict, set operations
- [ ] Explain shallow vs deep copy with example
- [ ] Write Two Sum from memory
- [ ] Explain when to use tuple over list
