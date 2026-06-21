"""
02 — pytest-style Tests

THEORY
------
What: pytest is a third-party test framework using plain assert statements, fixtures,
      and parametrize decorators for concise, readable tests.
Why:  Less boilerplate than unittest; rich plugin ecosystem; better failure output.
Key rules:
  - Test functions named test_* are auto-discovered; use plain assert (not self.assertEqual).
  - Install: pip install pytest; run: pytest path/to/file.py -v
  - Fixtures (@pytest.fixture) replace setUp for shared test resources.
When to use: New projects, data-driven tests, fixtures, plugins (cov, asyncio).
Common mistakes: Using assert without pytest installed; test functions with wrong naming;
                 relying on test order (pytest runs in arbitrary order).

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/02_pytest_style.py
"""


def is_palindrome(s: str) -> bool:  # check whether string reads same forwards and backwards
    cleaned = s.lower().replace(" ", "")  # normalize case and remove spaces
    return cleaned == cleaned[::-1]  # compare string to its reverse


def flatten(nested):  # recursively flatten nested lists into one list
    result = []  # accumulator for flattened values
    for item in nested:  # walk each element in nested structure
        if isinstance(item, list):  # recurse into nested lists
            result.extend(flatten(item))
        else:  # append scalar values directly
            result.append(item)
    return result  # return fully flattened list


def test_palindrome_simple():  # test plain palindrome word
    assert is_palindrome("racecar") is True


def test_palindrome_with_spaces():  # test palindrome phrase with spaces
    assert is_palindrome("A man a plan a canal Panama") is True


def test_not_palindrome():  # test non-palindrome string
    assert is_palindrome("hello") is False


def test_flatten():  # test flattening deeply nested list
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_empty():  # test flattening empty list
    assert flatten([]) == []


def main() -> None:  # entry point for manual test runner without pytest
    print("=" * 50)  # print section divider
    print("PRACTICE — Manual test runner (pytest-style)")  # section header
    print("=" * 50)  # close header divider
    test_palindrome_simple()  # run palindrome simple test
    test_palindrome_with_spaces()  # run palindrome with spaces test
    test_not_palindrome()  # run not-palindrome test
    test_flatten()  # run flatten test
    test_flatten_empty()  # run flatten empty test
    print("All tests passed!")  # confirm all manual tests succeeded


if __name__ == "__main__":  # run manual tests when executed directly
    main()  # start manual test execution
