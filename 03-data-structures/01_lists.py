"""01 — Lists: ordered, mutable sequences."""

# Create
fruits = ["apple", "banana", "cherry"]
numbers = list(range(1, 6))
empty = []

print(f"fruits: {fruits}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}")

# Slicing [start:stop:step]
print(f"Slice [0:2]: {fruits[0:2]}")
print(f"Reversed: {fruits[::-1]}")

# Modify
fruits.append("date")
fruits.insert(1, "apricot")
fruits.extend(["elderberry", "fig"])
print(f"After adds: {fruits}")

removed = fruits.pop()          # remove & return last
fruits.remove("banana")         # remove first match
print(f"After removes: {fruits}, popped: {removed}")

# Useful methods
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"len: {len(nums)}, count(1): {nums.count(1)}, index(4): {nums.index(4)}")
nums.sort()
print(f"sorted: {nums}")
print(f"min: {min(nums)}, max: {max(nums)}, sum: {sum(nums)}")

# List copying (shallow)
original = [[1, 2], [3, 4]]
copy = original.copy()
copy[0][0] = 99
print(f"Shallow copy shares inner lists: original[0] = {original[0]}")

# List as stack and queue
stack = []
stack.append(1); stack.append(2)
print(f"Stack pop: {stack.pop()}")

from collections import deque
queue = deque(["a", "b"])
queue.append("c")
print(f"Queue popleft: {queue.popleft()}")
