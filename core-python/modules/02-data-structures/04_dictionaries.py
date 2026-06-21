"""
04 — Dictionaries: Key-Value Mappings

THEORY
------
What is it?
    A dictionary maps unique, hashable keys to values using curly braces {} or
    dict(). Keys are looked up in O(1) average time, making dicts Python's
    primary structure for labeled data, caches, and configuration.

Why it matters
    Dicts appear in nearly every Python program — JSON APIs, config files,
    counting frequencies, grouping data. Interview questions often cover
    get() vs [], dict comprehensions, merging, and nested access.

Key syntax/rules
    - Keys must be hashable (str, int, tuple — not list or dict)
    - d[key] raises KeyError if missing; d.get(key, default) returns default safely
    - d[key] = value adds or updates; pop(key) removes and returns value
    - Iterate keys with for k in d, values with d.values(), pairs with d.items()
    - Dict merge (3.9+): defaults | overrides — later values win on duplicate keys
    - defaultdict(factory) auto-creates missing keys with factory()

When to use
    - Labelled records (user profiles, product specs, API responses)
    - Counting and grouping (word counts, inventory tallies)
    - Caches and lookup tables (id → object, name → score)
    - Configuration with named settings

Common mistakes
    - Using mutable objects (lists) as keys — TypeError
    - Using d[key] when key might not exist — prefer get() for safe access
    - Iterating and mutating dict keys simultaneously — copy keys first
    - Assuming dict order before Python 3.7 (insertion order is guaranteed in 3.7+)

PRACTICE
--------
Run: python3 core-python/modules/02-data-structures/04_dictionaries.py
"""

from collections import Counter, defaultdict  # specialized dict subclasses for counting


def main() -> None:  # entry point that runs all dictionary practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Create and access")  # section title
    print("=" * 50)  # close section header
    person = {"name": "Alice", "age": 30, "city": "NYC"}  # dict with string keys
    print(f"person: {person}")  # display the whole dictionary
    print(f"name: {person['name']}")  # access value by key with square brackets
    print(f"email (get): {person.get('email', 'N/A')}")  # safe access with default

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Modify and remove")  # section title
    print("=" * 50)  # close section header
    person["age"] = 31  # update an existing key's value
    person["email"] = "alice@example.com"  # add a new key-value pair
    print(f"Updated: {person}")  # show updated dictionary
    removed_age = person.pop("age")  # pop removes key and returns its value
    del person["city"]  # del removes a key without returning it
    print(f"After pop/del: {person}, removed age: {removed_age}")  # show post-removal state

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Iterate keys, values, items")  # section title
    print("=" * 50)  # close section header
    print("Keys, values, items:")  # label iteration section
    for key in person:  # loop over keys (default when iterating a dict)
        print(f"  key={key}, value={person[key]}")  # access each value by key
    for key, value in person.items():  # loop over key-value pairs together
        print(f"  {key}: {value}")  # print formatted pair

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Dict comprehension and merge")  # section title
    print("=" * 50)  # close section header
    squares = {x: x ** 2 for x in range(1, 6)}  # build dict mapping number to square
    print(f"Squares: {squares}")  # show the squares dictionary
    defaults = {"theme": "dark", "lang": "en"}  # default settings dictionary
    user_prefs = {"lang": "hi", "font_size": 14}  # user overrides some defaults
    merged = defaults | user_prefs  # merge dicts; later values win on duplicate keys
    print(f"Merged: {merged}")  # show merged result

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Nested dictionaries")  # section title
    print("=" * 50)  # close section header
    company = {  # dictionary containing another dictionary for employees
        "name": "TechCorp",
        "employees": {
            "E001": {"name": "Alice", "role": "Engineer"},
            "E002": {"name": "Bob", "role": "Designer"},
        },
    }
    print(f"Employee E001: {company['employees']['E001']}")  # chained key lookups

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — defaultdict and Counter")  # section title
    print("=" * 50)  # close section header
    word_count = defaultdict(int)  # int factory means missing keys default to 0
    for word in ["apple", "banana", "apple"]:  # count occurrences of each word
        word_count[word] += 1  # increment count (no KeyError on first sight)
    print(f"Word counts: {dict(word_count)}")  # convert to regular dict for display
    letters = Counter("mississippi")  # count frequency of each character
    print(f"Letter freq: {letters.most_common(3)}")  # show the 3 most common letters

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Practical: invert a mapping")  # section title
    print("=" * 50)  # close section header
    country_to_capital = {"India": "New Delhi", "France": "Paris", "Japan": "Tokyo"}  # country → capital
    capital_to_country = {v: k for k, v in country_to_capital.items()}  # swap keys and values
    print(f"Capital of France: {country_to_capital['France']}")  # forward lookup
    print(f"Paris is in: {capital_to_country['Paris']}")  # inverted lookup

    print("=" * 50)  # print section divider
    print("PRACTICE 8 — Practical: group records by category")  # section title
    print("=" * 50)  # close section header
    products = [  # sample product records as list of dicts
        {"name": "Pen", "category": "Stationery"},
        {"name": "Notebook", "category": "Stationery"},
        {"name": "Laptop", "category": "Electronics"},
    ]
    by_category: dict[str, list[str]] = defaultdict(list)  # group names by category
    for product in products:  # iterate each product record
        by_category[product["category"]].append(product["name"])  # append name to category list
    print(f"Grouped: {dict(by_category)}")  # show grouped result as plain dict


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all dictionary practice sections
