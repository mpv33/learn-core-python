"""
03 — Generators

THEORY
------
What: Functions that yield values lazily (one at a time) instead of returning a full list.
Why:  Save memory on large/infinite sequences; enable pipeline-style data processing.
Key rules:
  - Use yield in a function (generator function) or (expr for x in iter) for gen expr.
  - Generators are iterators — exhaust after one full pass unless recreated.
  - yield from delegates iteration to a sub-generator or iterable.
When to use: Large files, infinite sequences, streaming transforms, memory-sensitive code.
Common mistakes: Trying to len() or index a generator; reusing an exhausted generator;
                 building a list when a generator would suffice.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/03_generators.py
"""


def count_up_to(n: int):  # produce integers 1..n lazily
    current = 1  # start counting at 1
    while current <= n:  # continue until limit reached
        yield current  # pause and emit current value to caller
        current += 1  # advance to next integer


def chain_generators():  # combine multiple iterable sources
    yield from range(3)  # delegate yielding of 0, 1, 2
    yield from ["a", "b"]  # delegate yielding of list items
    yield from (x * 2 for x in range(3))  # delegate to generator expression


def read_lines(lines):  # strip newline from each line lazily
    for line in lines:  # iterate provided line collection
        yield line.strip()  # emit cleaned line without storing all at once


def fibonacci():  # endless Fibonacci sequence
    a, b = 0, 1  # seed first two Fibonacci numbers
    while True:  # never stop producing values
        yield a  # emit current Fibonacci number
        a, b = b, a + b  # shift window forward one step


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Generator function with yield")  # section header
    print("=" * 50)  # close header divider
    print("count_up_to(5):", end=" ")  # label generator iteration demo
    for num in count_up_to(5):  # consume generator in a for-loop
        print(num, end=" ")  # print each yielded value on one line
    print()  # finish the line

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Lazy evaluation with next()")  # section header
    print("=" * 50)  # close header divider
    gen = count_up_to(3)  # create generator object without running body yet
    print(f"next: {next(gen)}, next: {next(gen)}, next: {next(gen)}")  # pull three values

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Generator expression")  # section header
    print("=" * 50)  # close header divider
    squares_gen = (x**2 for x in range(1, 6))  # lazy squares of 1..5
    print(f"Generator squares: {list(squares_gen)}")  # materialize generator into list

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Memory benefit vs list")  # section header
    print("=" * 50)  # close header divider
    import sys  # introspect object sizes
    list_size = sys.getsizeof([x for x in range(10000)])  # size of eager list comprehension
    gen_size = sys.getsizeof(x for x in range(10000))  # size of generator object
    print(f"List size: {list_size}, Gen size: {gen_size}")  # generator uses far less memory

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — yield from delegation")  # section header
    print("=" * 50)  # close header divider
    print(f"Chained: {list(chain_generators())}")  # flatten all delegated sequences

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Read large file line by line")  # section header
    print("=" * 50)  # close header divider
    sample = ["line 1\n", "line 2\n", "line 3\n"]  # fake file lines with trailing newlines
    for line in read_lines(sample):  # consume stripped lines one by one
        print(f"  {line}")  # print each cleaned line

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — Infinite generator (Fibonacci)")  # section header
    print("=" * 50)  # close header divider
    fib = fibonacci()  # create infinite generator instance
    first_10 = [next(fib) for _ in range(10)]  # take first ten values manually
    print(f"First 10 Fibonacci: {first_10}")  # show collected sequence

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 8 — Generator pipeline for filtering")  # section header
    print("=" * 50)  # close header divider
    numbers = range(1, 21)  # integers 1 through 20
    pipeline = (n for n in numbers if n % 3 == 0)  # lazy filter multiples of 3
    tripled = (n * 3 for n in pipeline)  # lazy transform each filtered value
    print(f"Tripled multiples of 3: {list(tripled)}")  # materialize pipeline result


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
