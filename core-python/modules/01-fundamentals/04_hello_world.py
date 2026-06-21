"""
04 — Hello World: Your First Python Program

THEORY
------
What is it?
    print() sends text to standard output (the console). Strings are created with
    single or double quotes. Comments start with # and are ignored by the interpreter.
    Triple-quoted strings at file top are docstrings — metadata, not executed code.

Why it matters
    print() is your primary debugging tool before learning logging or debuggers.
    Understanding sep and end parameters controls formatting. Every Python developer
    starts here — interviews sometimes ask about print vs logging.

Key syntax/rules
    - print("text")              → output with trailing newline (default)
    - print("a", "b")            → items separated by space (default sep)
    - print("a", end="")         → suppress newline; control trailing text with end
    - print("a", "b", sep="-")   → join items with custom separator
    - # comment                  → single-line comment to end of line
    - 'text' and "text"          → equivalent string literals

When to use
    - Quick output during learning and prototyping
    - Script CLI feedback before building proper argparse interfaces
    - Temporary debugging (prefer logging in production)

Common mistakes
    - Forgetting print() is a function in Python 3 (not a statement like Python 2)
    - Expecting print() to return a value — it returns None
    - Using print for production logging (no levels, timestamps, or routing)

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/04_hello_world.py
"""


def main() -> None:  # entry point that runs all hello-world practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Basic print and comments")  # section title
    print("=" * 50)  # close section header
    # Single-line comment: ignored by Python
    print("Hello, World!")  # display the classic first-program greeting on screen
    print("Hello", "Python", "Learner")  # print three words with default space separator
    print('Both quote styles work')  # demonstrate that single-quoted strings print the same way

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — sep and end parameters")  # section title
    print("=" * 50)  # close section header
    print("a", "b", "c", sep="-")  # join items with "-" instead of spaces → a-b-c
    print("Line 1", end=" | ")  # keep cursor on same line and append " | " after output
    print("Line 2")  # continues on same line because previous print changed end → Line 1 | Line 2
    print("one", "two", "three", sep=" → ")  # custom arrow separator between items

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Multi-line strings and docstrings")  # section title
    print("=" * 50)  # close section header
    doc = """Multi-line string (docstring style).
Often used at the top of files to describe the module."""  # assign multi-line text to variable
    print(doc)  # print the multi-line string content
    print(f"Docstring length: {len(doc)} characters")  # show that docstrings are regular strings

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Practical: formatted greeting card")  # section title
    print("=" * 50)  # close section header
    name = "Python Learner"  # recipient name for the greeting card
    course = "Core Python Fundamentals"  # course title for the card
    print("╔" + "═" * 30 + "╗")  # top border of ASCII card
    print(f"║  Welcome, {name:<14} ║")  # left-align name in fixed-width field
    print(f"║  Course: {course:<17} ║")  # show course name in card layout
    print("╚" + "═" * 30 + "╝")  # bottom border of ASCII card


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all hello-world practice sections
