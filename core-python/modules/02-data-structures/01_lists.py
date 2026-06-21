"""
01 — Lists: Ordered, Mutable Sequences

THEORY
------
What is it?
    A list is an ordered, mutable collection that holds items of any type.
    Lists are created with square brackets [] and support indexing, slicing,
    and a rich set of methods for adding, removing, and transforming items.

Why it matters
    Lists are Python's most versatile container — used everywhere from storing
    user data to building pipelines. Interview questions often test slicing,
    mutability, and the difference between shallow copy and shared references.

Key syntax/rules
    - Index from 0; negative indices count from the end (-1 = last item)
    - Slicing [start:stop:step] — stop is exclusive, step defaults to 1
    - append(x) adds one item; extend(iterable) adds many; insert(i, x) at index
    - pop() removes last; remove(x) removes first match; del list[i] deletes by index
    - sort() mutates in place; sorted(list) returns a new sorted list
    - list.copy() is shallow — nested mutable objects are still shared

When to use
    - Ordered collections you need to grow, shrink, or reorder
    - Stack operations (append/pop from end)
    - Building result lists in loops or comprehensions
    - When you need duplicate values and positional access

Common mistakes
    - Using lst = other_list instead of .copy() — both names point to same object
    - Confusing append [x] with extend(x) — append nests the whole list
    - Modifying a list while iterating over it (use a copy or iterate backwards)
    - Assuming sort() returns a value — it returns None and mutates in place

PRACTICE
--------
Run: python3 core-python/modules/02-data-structures/01_lists.py
"""

from collections import deque  # fast double-ended queue for queue operations


def main() -> None:  # entry point that runs all list practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Create and access lists")  # section title
    print("=" * 50)  # close section header
    fruits = ["apple", "banana", "cherry"]  # create a list of fruit names
    numbers = list(range(1, 6))  # build [1, 2, 3, 4, 5] from range
    empty = []  # create an empty list
    print(f"fruits: {fruits}")  # display the fruits list
    print(f"numbers: {numbers}, empty: {empty}")  # show numbers and empty list
    print(f"First: {fruits[0]}, Last: {fruits[-1]}")  # index 0 and -1 access

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Slicing")  # section title
    print("=" * 50)  # close section header
    print(f"Slice [0:2]: {fruits[0:2]}")  # elements at index 0 and 1 only
    print(f"Every other: {numbers[::2]}")  # step of 2 skips alternate items
    print(f"Reversed: {fruits[::-1]}")  # reverse using step -1

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Modify lists")  # section title
    print("=" * 50)  # close section header
    fruits.append("date")  # add "date" to the end
    fruits.insert(1, "apricot")  # insert "apricot" at index 1
    fruits.extend(["elderberry", "fig"])  # add multiple items at the end
    print(f"After adds: {fruits}")  # show list after all additions
    removed = fruits.pop()  # remove and return the last item
    fruits.remove("banana")  # remove the first occurrence of "banana"
    print(f"After removes: {fruits}, popped: {removed}")  # show post-removal state

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Useful methods and builtins")  # section title
    print("=" * 50)  # close section header
    nums = [3, 1, 4, 1, 5, 9, 2, 6]  # list with duplicates for demo methods
    print(f"len: {len(nums)}, count(1): {nums.count(1)}, index(4): {nums.index(4)}")  # length, count, index
    nums.sort()  # sort in place ascending
    print(f"sorted: {nums}")  # show sorted list
    print(f"min: {min(nums)}, max: {max(nums)}, sum: {sum(nums)}")  # aggregate builtins

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Shallow copy shares inner objects")  # section title
    print("=" * 50)  # close section header
    original = [[1, 2], [3, 4]]  # nested list — inner lists are mutable
    copy = original.copy()  # shallow copy: new outer list, shared inner lists
    copy[0][0] = 99  # mutate inner list through the copy
    print(f"Shallow copy shares inner lists: original[0] = {original[0]}")  # original also changed

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Stack and queue patterns")  # section title
    print("=" * 50)  # close section header
    stack = []  # empty list used as a stack
    stack.append(1)  # push first item onto stack
    stack.append(2)  # push second item onto stack
    print(f"Stack pop: {stack.pop()}")  # pop removes and returns last item (LIFO)
    queue = deque(["a", "b"])  # deque is better for queue operations
    queue.append("c")  # add item to the right end
    print(f"Queue popleft: {queue.popleft()}")  # remove from left end (FIFO)

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — List comprehension")  # section title
    print("=" * 50)  # close section header
    squares = [x ** 2 for x in range(1, 6)]  # build [1, 4, 9, 16, 25] in one line
    print(f"Squares: {squares}")  # display comprehension result
    evens = [x for x in range(10) if x % 2 == 0]  # filter while building
    print(f"Evens 0-9: {evens}")  # show filtered comprehension

    print("=" * 50)  # print section divider
    print("PRACTICE 8 — Practical: grade curve")  # section title
    print("=" * 50)  # close section header
    scores = [72, 85, 90, 68, 95]  # sample student scores
    curved = [min(100, s + 5) for s in scores]  # add 5 points, cap at 100
    passing = [s for s in curved if s >= 70]  # keep only passing scores
    print(f"Original: {scores}")  # show raw scores
    print(f"Curved:   {curved}")  # show adjusted scores
    print(f"Passing:  {passing}")  # show filtered passing list


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all list practice sections
