"""
02 — Dict and Set Comprehensions

THEORY
------
What: Comprehension syntax for building dicts {k: v for ...} and sets {expr for ...}.
Why:  Create mappings and unique collections in one expression without temporary loops.
Key rules:
  - Dict: {key_expr: val_expr for item in iterable [if condition]}
  - Set:  {expr for item in iterable} — values must be hashable; duplicates removed.
  - Dict keys must be unique; later entries overwrite earlier ones.
When to use: Building lookup tables, inverting dicts, deduplicating transformed values.
Common mistakes: Using unhashable set members; swapping keys/values when values aren't
                 unique; overly complex one-liners that hurt readability.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/02_dict_set_comprehensions.py
"""


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Basic dict comprehension")  # section header
    print("=" * 50)  # close header divider
    word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}  # word -> length
    print(f"Word lengths: {word_lengths}")  # display resulting dictionary

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Dict comprehension with filter")  # section header
    print("=" * 50)  # close header divider
    scores = {"Alice": 92, "Bob": 55, "Carol": 88, "Dave": 45}  # name-to-score mapping
    passed = {name: score for name, score in scores.items() if score >= 60}  # passing only
    print(f"Passed: {passed}")  # show filtered dict

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Invert a dictionary")  # section header
    print("=" * 50)  # close header divider
    original = {"a": 1, "b": 2, "c": 3}  # simple bijective mapping
    inverted = {v: k for k, v in original.items()}  # swap keys and values
    print(f"Inverted: {inverted}")  # values become keys and vice versa

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Set comprehension")  # section header
    print("=" * 50)  # close header divider
    unique_lengths = {len(w) for w in ["hi", "hello", "hey", "world"]}  # unique word lengths
    print(f"Unique lengths: {unique_lengths}")  # sets deduplicate automatically

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Case-insensitive deduplication")  # section header
    print("=" * 50)  # close header divider
    words = ["Apple", "apple", "Banana", "banana", "Cherry"]  # mixed-case duplicates
    unique_lower = {w.lower() for w in words}  # normalize case then dedupe
    print(f"Unique (lower): {unique_lower}")  # one entry per distinct lowercase word

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Build dict from list of tuples")  # section header
    print("=" * 50)  # close header divider
    users = [("Alice", 30), ("Bob", 25)]  # sequence of (name, age) pairs
    user_dict = {name: age for name, age in users}  # build dict from tuples
    print(f"User dict: {user_dict}")  # show name-to-age mapping

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — Transform dict values")  # section header
    print("=" * 50)  # close header divider
    config = {"debug": True, "timeout": 30}  # settings with mixed value types
    str_config = {k: str(v) for k, v in config.items()}  # stringify every value
    print(f"String config: {str_config}")  # all values are strings

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 8 — Count vowels per word with dict comp")  # section header
    print("=" * 50)  # close header divider
    vocabulary = ["python", "comprehension", "set", "dict"]  # words to analyze
    vowel_counts = {w: sum(1 for c in w if c in "aeiou") for w in vocabulary}  # count vowels
    print(f"Vowel counts: {vowel_counts}")  # show per-word vowel totals


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
