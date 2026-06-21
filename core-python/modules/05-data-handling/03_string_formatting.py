"""
03 — String Formatting
======================

THEORY
------
What:
  String formatting embeds values into text. Python offers f-strings (preferred),
  `.format()`, `%` formatting, and `string.Template` for safe substitution.

Why:
  Build readable, maintainable output — reports, log messages, API payloads, and
  user-facing text — without messy concatenation.

Key rules:
  - f-strings: `f"{name} scored {score:.1f}"` — expressions allowed inside `{}`.
  - Format specs: `:.2f` (float), `:05d` (zero-padded int), `:,` (thousands sep).
  - `.format()`: positional `{}` or named `{name}` placeholders.
  - `f"{x=}"` debug syntax prints name and value (Python 3.8+).
  - `Template` uses `$name` — good for user-supplied templates (safer than f-strings).

When to use:
  - f-strings: default choice for most formatting (fast, readable).
  - `.format()`: legacy code or reusable format strings stored in variables.
  - `Template`: external templates where `{}` syntax could be ambiguous.

Common mistakes:
  - Using `%` formatting in new code — prefer f-strings.
  - Forgetting the `f` prefix: `"{name}"` prints literally, not the variable.
  - Putting complex logic inside f-strings — extract to variables for clarity.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/03_string_formatting.py
"""

from string import Template  # $-based safe substitution


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — f-strings and format specifiers")  # label first block
    print("=" * 50)  # close header

    name = "Alice"  # sample name for format demos
    score = 95.567  # floating-point score
    count = 42  # integer for numeric specifiers
    print(f"{name} scored {score:.1f}%")  # one decimal place
    print(f"Binary: {count:b}, Hex: {count:x}")  # binary and lowercase hex
    print(f"Padded: {count:05d}")  # zero-pad integer to width 5
    print(f"Thousands: {1_234_567:,}")  # comma thousands separators

    print("\n" + "=" * 50)  # divider before expressions demo
    print("PRACTICE 2 — Expressions and debug f-strings")  # label second block
    print("=" * 50)  # close header

    items = ["apple", "banana", "cherry"]  # list used inside f-string expressions
    print(f"First item: {items[0].upper()}")  # call methods inside braces
    print(f"Total length: {sum(len(i) for i in items)}")  # comprehension inside f-string
    x = 10  # variable for debug syntax demo
    print(f"{x=}")  # prints x=10 — name and value together
    print(f"{items=}")  # debug any expression

    print("\n" + "=" * 50)  # divider before format() demo
    print("PRACTICE 3 — format() method")  # label third block
    print("=" * 50)  # close header

    print("Hello, {}! You have {} messages.".format(name, 5))  # positional placeholders
    print("{1} before {0}".format("second", "first"))  # reorder by index
    print("{name} lives in {city}".format(name="Bob", city="Mumbai"))  # named placeholders
    pi = 3.14159265  # constant for fixed-point formatting
    print(f"Pi: {pi:.3f}")  # three digits after decimal
    print(f"Percent: {0.856:.1%}")  # multiply by 100 and append %

    print("\n" + "=" * 50)  # divider before Template demo
    print("PRACTICE 4 — Template strings")  # label fourth block
    print("=" * 50)  # close header

    t = Template("Dear $name, your balance is $$ $amount.")  # $$ renders literal $
    print(t.substitute(name="Alice", amount="150.00"))  # replace $placeholders
    greeting_template = Template("Welcome, $user! Today is $day.")  # reusable template
    print(greeting_template.substitute(user="Dev", day="Monday"))  # substitute different values


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
