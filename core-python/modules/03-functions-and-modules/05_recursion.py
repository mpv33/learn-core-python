"""
05 — Recursion: Function Calls Itself

THEORY
------
What is it?
    Recursion is when a function calls itself to solve a problem by breaking it
    into smaller subproblems. Every recursive function needs a base case (stop
    condition) and a recursive case (calls itself with a simpler input).

Why it matters
    Recursion models tree traversal, divide-and-conquer algorithms, and problems
    with self-similar structure (factorial, Fibonacci, palindromes). Interviewers
    frequently ask for recursive solutions and their iterative alternatives.

Key syntax/rules
    - Base case: if n <= 1: return 1 — stops infinite recursion
    - Recursive case: return n * factorial(n - 1) — problem shrinks each call
    - Python has a default recursion limit (~1000) — sys.setrecursionlimit() rarely needed
    - Python does NOT optimize tail recursion — deep recursion may hit RecursionError
    - @lru_cache memoizes results to turn exponential recursion into linear time
    - Prefer iteration for deep or hot-path recursion (factorial, Fibonacci)

When to use
    - Tree and graph traversal (DFS on nested structures)
    - Problems naturally defined recursively (factorial, permutations, palindrome)
    - Divide-and-conquer (merge sort, quicksort, binary search)
    - When code clarity outweighs stack depth concerns

Common mistakes
    - Missing or wrong base case — infinite recursion → RecursionError
    - Not progressing toward base case — same input recurs forever
    - Using naive Fibonacci without memoization — O(2^n) explosion
    - Assuming Python optimizes tail recursion (it does not)

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/05_recursion.py
"""

from functools import lru_cache  # cache decorator to memoize recursive results


def factorial(n: int) -> int:  # recursive factorial: n! = n × (n-1) × ... × 1
    if n <= 1:  # base case: 0! and 1! both equal 1
        return 1
    return n * factorial(n - 1)  # recursive case: n times factorial of (n-1)


def fibonacci(n: int) -> int:  # naive recursive Fibonacci (slow without cache)
    if n <= 1:  # base cases: fib(0)=0, fib(1)=1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # sum of two preceding numbers


def is_palindrome(s: str) -> bool:  # recursive palindrome checker
    s = s.lower().replace(" ", "")  # normalize: lowercase and remove spaces
    if len(s) <= 1:  # base case: empty or single char is a palindrome
        return True
    if s[0] != s[-1]:  # if first and last chars differ, not a palindrome
        return False
    return is_palindrome(s[1:-1])  # recursive case: check middle substring


@lru_cache(maxsize=None)  # cache decorator stores results to avoid redundant calls
def fib_cached(n):  # memoized Fibonacci — fast even for large n
    if n <= 1:  # base cases for cached fibonacci
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)  # recursive case with caching


def factorial_iter(n):  # iterative alternative (often preferred for factorial)
    result = 1  # start accumulator at 1
    for i in range(2, n + 1):  # multiply by each integer from 2 to n
        result *= i
    return result  # return final product


def main() -> None:  # entry point that runs all recursion practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Factorial")  # section title
    print("=" * 50)  # close section header
    print(f"5! = {factorial(5)}")  # compute 5 factorial recursively

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Fibonacci")  # section title
    print("=" * 50)  # close section header
    print(f"fib(7) = {fibonacci(7)}")  # compute 7th Fibonacci number (naive)

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Palindrome check")  # section title
    print("=" * 50)  # close section header
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")  # True — reads same both ways
    print(f"'hello' palindrome: {is_palindrome('hello')}")  # False — not a palindrome

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Memoized Fibonacci")  # section title
    print("=" * 50)  # close section header
    print(f"fib_cached(50) = {fib_cached(50)}")  # fib(50) is fast thanks to memoization

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Iterative alternative")  # section title
    print("=" * 50)  # close section header
    print(f"5! iterative = {factorial_iter(5)}")  # compute 5 factorial iteratively

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: sum nested list")  # section title
    print("=" * 50)  # close section header
    def sum_nested(items):  # recursively sum numbers in arbitrarily nested lists
        total = 0  # accumulator for the sum
        for item in items:  # iterate each element
            if isinstance(item, list):  # if element is itself a list
                total += sum_nested(item)  # recurse into nested list
            else:  # base case: item is a plain number
                total += item  # add number to total
        return total  # return accumulated sum

    nested = [1, [2, 3], [4, [5, 6]]]  # sample nested list structure
    print(f"sum_nested({nested}) = {sum_nested(nested)}")  # should sum to 21

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Practical: directory depth")  # section title
    print("=" * 50)  # close section header
    tree = {"name": "root", "children": [  # nested dict mimicking a folder tree
        {"name": "src", "children": [{"name": "main.py", "children": []}]},
        {"name": "docs", "children": []},
    ]}

    def max_depth(node: dict) -> int:  # recursively find maximum nesting depth
        if not node.get("children"):  # base case: leaf node has depth 1
            return 1
        return 1 + max(max_depth(child) for child in node["children"])  # 1 + deepest child

    print(f"Tree max depth: {max_depth(tree)}")  # show depth of sample tree


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all recursion practice sections
