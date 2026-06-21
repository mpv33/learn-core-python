"""02 — pytest-style Tests (also runnable concepts)"""

# pytest uses plain assert statements — simpler syntax
# Install: pip install pytest
# Run: pytest 02_pytest_style.py -v

def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# --- Tests (pytest discovers test_* functions) ---

def test_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_not_palindrome():
    assert is_palindrome("hello") is False

def test_flatten():
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty():
    assert flatten([]) == []

# Parametrize example (pytest feature):
# @pytest.mark.parametrize("input,expected", [
#     ("racecar", True),
#     ("hello", False),
# ])
# def test_palindrome_param(input, expected):
#     assert is_palindrome(input) == expected

if __name__ == "__main__":
    test_palindrome_simple()
    test_palindrome_with_spaces()
    test_not_palindrome()
    test_flatten()
    test_flatten_empty()
    print("All tests passed!")
