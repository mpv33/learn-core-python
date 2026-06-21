"""
07 — Input and Output: Console Interaction and Formatting

THEORY
------
What is it?
    input(prompt) reads a line of text from the keyboard and always returns a str.
    print() writes to stdout. f-strings (f"...") embed expressions inside braces
    and are the modern standard for formatted output.

Why it matters
    Every CLI tool, script, and beginner program uses I/O. Misunderstanding that
    input() returns str causes int + str TypeErrors. Format specifiers (:.2f, :05d)
    appear in reports, logs, and data pipelines.

Key syntax/rules
    - name = input("Prompt: ")     → always returns str; cast with int(), float()
    - f"{value:.2f}"               → float with 2 decimal places
    - f"{num:05d}"                 → zero-padded integer, width 5
    - f"{text:>10}"                → right-align in 10-character field
    - "{}".format(x)               → older placeholder style, still valid
    - "\\n newline, \\t tab         → escape sequences inside strings

When to use
    - f-strings for all new code (readable, fast, supports expressions)
    - input() for interactive CLI scripts and simple user prompts
    - Format specifiers when aligning columns or showing currency/precision

Common mistakes
    - Forgetting int(input(...)) when doing math on user input
    - Using % formatting or .format() in new code when f-strings are clearer
    - input() with no prompt — user sees blank cursor and gets confused
    - Printing sensitive data (passwords) without masking

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/07_input_output.py
"""


def main() -> None:  # entry point that runs all input/output practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Simulated input (non-interactive)")  # section title
    print("=" * 50)  # close section header
    # name = input("Enter your name: ")  # uncomment for interactive keyboard input
    name = "Demo User"  # hard-coded name so script runs without waiting for keyboard input
    print(f"Hello, {name}!")  # greet the user using an f-string
    # age = int(input("Enter age: "))  # cast to int when doing math on user input
    age_str = "25"  # simulated string input (what input() always returns)
    age = int(age_str)  # convert string to int for arithmetic
    print(f"Next year you'll be {age + 1}")  # demonstrate math after casting input

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — f-string formatting")  # section title
    print("=" * 50)  # close section header
    item = "book"  # product name used in formatted output
    cost = 29.99  # price as a float for currency formatting
    print(f"The {item} costs ${cost:.2f}")  # embed variables; .2f shows two decimal places
    print("The {} costs ${:.2f}".format(item, cost))  # older but flexible placeholder formatting
    print("The %s costs $%.2f" % (item, cost))  # C-style formatting still supported

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Alignment and padding")  # section title
    print("=" * 50)  # close section header
    num = 42  # integer used to demo width and padding
    print(f"Number: {num:05d}")  # zero-pad to 5 digits → 00042
    print(f"Number: {num:>5}")  # right-align in a field 5 characters wide
    print(f"{'Name':<10} {'Score':>6}")  # column headers: left-align name, right-align score
    print(f"{'Alice':<10} {95:>6}")  # data row aligned under headers
    print(f"{'Bob':<10} {87:>6}")  # second data row with same alignment

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Escape characters and multiple values")  # section title
    print("=" * 50)  # close section header
    print("Line 1\nLine 2")  # \n inserts a newline between two lines
    print("Tab\tseparated")  # \t inserts a tab character between words
    print('She said "Hello"')  # single quotes let double quotes appear inside the string
    x, y = 10, 20  # two values to print together
    print("x =", x, "y =", y)  # print several arguments separated by spaces
    print(f"x = {x}, y = {y}")  # same info in one f-string (often clearer)

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: receipt formatter")  # section title
    print("=" * 50)  # close section header
    items = [("Coffee", 4.50), ("Muffin", 3.25), ("Juice", 2.99)]  # list of (name, price) tuples
    print(f"{'Item':<12} {'Price':>8}")  # receipt header with aligned columns
    print("-" * 22)  # separator line under header
    total = 0.0  # running sum of all item prices
    for item_name, price in items:  # iterate each line item on the receipt
        print(f"{item_name:<12} ${price:>7.2f}")  # print name left, price right-aligned
        total += price  # add current item price to running total
    print("-" * 22)  # separator line above total
    print(f"{'TOTAL':<12} ${total:>7.2f}")  # print bold-looking total row


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all input/output practice sections
