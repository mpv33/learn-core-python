"""
01 — String Basics
==================

THEORY
------
What:
  Strings (`str`) are immutable sequences of Unicode characters. You can index,
  slice, iterate, and concatenate them, but never change individual characters
  in place.

Why:
  Text is everywhere — user input, file contents, API responses, logs. Mastering
  string basics is the foundation for parsing, formatting, and validation.

Key rules:
  - Indexing: `s[0]` first char, `s[-1]` last char; out-of-range raises IndexError.
  - Slicing: `s[start:stop:step]` — stop is exclusive; omit parts for defaults.
  - Immutable: `s[0] = "x"` raises TypeError; create a new string instead.
  - Raw strings `r"..."` treat backslashes literally (Windows paths, regex).
  - `encode()` / `decode()` convert between str and bytes.

When to use:
  - Reading and displaying text, building messages, checking substrings.
  - Slicing filenames, URLs, or fixed-width fields.
  - Encoding text for files, networks, or binary protocols.

Common mistakes:
  - Assuming strings are mutable and trying to modify characters in place.
  - Confusing `len(s)` (characters) with byte length after encoding.
  - Forgetting that `\n`, `\t`, `\"` are escape sequences unless using raw strings.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/01_string_basics.py
"""


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Indexing, slicing, and length")  # label first block
    print("=" * 50)  # close header

    s = "Hello, Python!"  # sample string for indexing demos
    print(f"Length: {len(s)}")  # count characters in the string
    print(f"First char: {s[0]}, Last: {s[-1]}")  # positive and negative indexing
    print(f"Slice [7:13]: {s[7:13]}")  # substring from index 7 up to (not including) 13
    print(f"Every 2nd char: {s[::2]}")  # slice with step 2 skips alternate chars
    print(f"Reversed: {s[::-1]}")  # step -1 reverses the string

    print("\n" + "=" * 50)  # divider before multi-line demo
    print("PRACTICE 2 — Multi-line and escape sequences")  # label second block
    print("=" * 50)  # close header

    poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you."""  # triple-quoted string preserves embedded newlines
    print(poem)  # print the full multi-line poem
    print("Line1\nLine2\tTabbed")  # \n newline; \t tab
    print('She said "Hi"')  # single quotes allow double quotes inside
    print("It\\'s fine")  # escape apostrophe inside double-quoted string

    print("\n" + "=" * 50)  # divider before raw strings demo
    print("PRACTICE 3 — Raw strings and concatenation")  # label third block
    print("=" * 50)  # close header

    path = r"C:\Users\name\file.txt"  # backslashes treated literally
    print(f"Raw path: {path}")  # display unescaped Windows-style path
    first = "Hello"  # first word for concatenation
    second = "World"  # second word for concatenation
    print(first + " " + second)  # join with + operator
    print(first * 3)  # repeat string three times with * operator

    print("\n" + "=" * 50)  # divider before membership demo
    print("PRACTICE 4 — Membership, iteration, and immutability")  # label fourth block
    print("=" * 50)  # close header

    print(f"'Python' in s: {'Python' in s}")  # True — substring found
    print(f"'Java' not in s: {'Java' not in s}")  # True — substring absent
    for char in "abc":  # iterate over each character
        print(char, end=" ")  # print on same line separated by spaces
    print()  # finish the line after loop
    # s[0] = "h"  # TypeError — strings are immutable

    print("\n" + "=" * 50)  # divider before encoding demo
    print("PRACTICE 5 — Encoding and decoding")  # label fifth block
    print("=" * 50)  # close header

    text = "café"  # Unicode text with non-ASCII character
    encoded = text.encode("utf-8")  # str → bytes using UTF-8
    decoded = encoded.decode("utf-8")  # bytes → str round trip
    print(f"Encoded bytes: {encoded}")  # show raw byte representation
    print(f"Decoded: {decoded}")  # confirm round-trip matches original


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
