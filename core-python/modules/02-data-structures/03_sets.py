"""
03 — Sets: Unordered Collections of Unique Elements

THEORY
------
What is it?
    A set is an unordered collection of unique, hashable elements created with
    {} or set(). Sets support fast membership testing and mathematical set
    operations like union, intersection, and difference.

Why it matters
    Sets give O(1) average lookup for "is x in the collection?" — much faster
    than lists for large datasets. They are the go-to tool for deduplication
    and finding overlaps between groups.

Key syntax/rules
    - {} creates an empty dict, not a set — use set() for empty set
    - Elements must be hashable (no lists or dicts inside sets)
    - add(x) inserts one item; discard(x) removes safely; remove(x) raises KeyError
    - Union: a | b or a.union(b); Intersection: a & b; Difference: a - b
    - Symmetric difference: a ^ b — elements in either set but not both
    - frozenset is an immutable set that can be used as a dict key

When to use
    - Removing duplicates from a list: list(set(items))
    - Fast membership checks on large collections
    - Finding common or unique elements between groups
    - Tracking "seen" items during algorithms (BFS, dedup pipelines)

Common mistakes
    - Using {} for an empty set — it creates an empty dictionary
    - Putting unhashable types (lists, dicts) into a set — TypeError
    - Expecting sets to preserve insertion order in older Python versions
    - Using remove() when discard() is safer (discard ignores missing items)

PRACTICE
--------
Run: python3 core-python/modules/02-data-structures/03_sets.py
"""


def main() -> None:  # entry point that runs all set practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Create sets and deduplicate")  # section title
    print("=" * 50)  # close section header
    colors = {"red", "green", "blue"}  # create a set of color names
    numbers = set([1, 2, 2, 3, 3, 3])  # convert list — duplicates removed automatically
    empty = set()  # use set() for empty set; {} creates an empty dict
    print(f"colors: {colors}")  # display the colors set
    print(f"numbers (deduplicated): {numbers}")  # show deduplicated numbers
    print(f"empty set: {empty}, type: {type(empty)}")  # confirm empty set type

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Add and remove")  # section title
    print("=" * 50)  # close section header
    colors.add("yellow")  # add a new color to the set
    colors.discard("green")  # remove "green" safely — no error if missing
    # colors.remove("purple")  # KeyError if missing — use discard instead
    print(f"After changes: {colors}")  # show set after modifications

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Set operations")  # section title
    print("=" * 50)  # close section header
    a = {1, 2, 3, 4}  # first set for demonstrating set math
    b = {3, 4, 5, 6}  # second set for demonstrating set math
    print(f"Union a | b:           {a | b}")  # all elements in either set
    print(f"Intersection a & b:    {a & b}")  # elements in both sets
    print(f"Difference a - b:      {a - b}")  # elements in a but not in b
    print(f"Symmetric a ^ b:       {a ^ b}")  # elements in either but not both

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Membership and deduplication")  # section title
    print("=" * 50)  # close section header
    print(f"2 in a: {2 in a}")  # fast O(1) membership test
    items = ["apple", "banana", "apple", "cherry", "banana"]  # list with repeats
    unique = list(set(items))  # convert to set then back to list for dedup
    print(f"Unique items: {unique}")  # show deduplicated list

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — frozenset as dict key")  # section title
    print("=" * 50)  # close section header
    frozen = frozenset([1, 2, 3])  # create an immutable set
    cache = {frozen: "cached_value"}  # use frozenset as a dictionary key
    print(f"Frozen set as key: {cache[frozen]}")  # retrieve value using frozenset key

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: mutual friends")  # section title
    print("=" * 50)  # close section header
    alice_friends = {"Bob", "Carol", "Dave"}  # Alice's friend set
    bob_friends = {"Alice", "Carol", "Eve"}  # Bob's friend set
    mutual = alice_friends & bob_friends  # intersection finds mutual friends
    print(f"Mutual friends: {mutual}")  # show friends both Alice and Bob have

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Practical: tag overlap between articles")  # section title
    print("=" * 50)  # close section header
    article_a = {"python", "tutorial", "beginner"}  # tags for first article
    article_b = {"python", "advanced", "tutorial"}  # tags for second article
    shared = article_a & article_b  # tags both articles share
    unique_to_a = article_a - article_b  # tags only in article A
    print(f"Shared tags:    {shared}")  # show overlapping tags
    print(f"Unique to A:    {unique_to_a}")  # show tags exclusive to article A

    print("=" * 50)  # print section divider
    print("PRACTICE 8 — Practical: seen-item tracking")  # section title
    print("=" * 50)  # close section header
    seen = set()  # empty set to track items already processed
    emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]  # list with duplicate email
    unique_emails = []  # build list of first-seen emails in order
    for email in emails:  # iterate through all emails
        if email not in seen:  # skip if already seen (O(1) lookup)
            seen.add(email)  # mark email as seen
            unique_emails.append(email)  # keep first occurrence in order
    print(f"Unique emails (order preserved): {unique_emails}")  # show deduped list


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all set practice sections
