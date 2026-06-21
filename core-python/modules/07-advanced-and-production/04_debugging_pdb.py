"""
04 — Debugging with pdb

THEORY
------
What: pdb is Python's built-in debugger — pause execution, inspect variables, step
      through code line by line.
Why:  Find bugs faster than print-debugging; inspect live state at the point of failure.
Key rules:
  - breakpoint() (Python 3.7+) calls pdb.set_trace() — pauses at that line.
  - Key commands: n (next), s (step into), c (continue), p var, l (list), q (quit).
  - Run: python -m pdb script.py or pytest --pdb on test failure.
When to use: Unexpected values, logic errors, understanding unfamiliar code paths.
Common mistakes: Leaving breakpoint() in committed code; stepping without reading locals;
                 not using conditional breakpoints for loops.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/04_debugging_pdb.py
"""


def calculate_discount(price: float, discount_pct: float) -> float:  # compute discounted price
    if discount_pct < 0 or discount_pct > 100:  # validate discount percentage range
        raise ValueError("Discount must be 0-100")
    return price * (1 - discount_pct / 100)  # apply percentage discount to price


def checkout(items: list[dict]) -> float:  # sum discounted prices for cart items
    total = 0.0  # running checkout total
    for item in items:  # process each cart item
        price = item["price"]  # read item base price
        discount = item.get("discount", 0)  # read optional discount percent
        final = calculate_discount(price, discount)  # compute discounted line price
        total += final  # add line total to cart sum
    return round(total, 2)  # return total rounded to cents


def main() -> None:  # entry point for debugging demo
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Checkout with discount calculation")  # section header
    print("=" * 50)  # close header divider
    cart = [  # sample shopping cart items
        {"name": "Book", "price": 29.99, "discount": 10},
        {"name": "Pen", "price": 2.50, "discount": 0},
    ]
    # breakpoint()  # uncomment to debug interactively at this point
    total = checkout(cart)  # compute cart total
    print(f"Total: ${total:.2f}")  # display formatted total

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — pdb commands reference")  # section header
    print("=" * 50)  # close header divider
    print("  n (next)     — execute next line")  # pdb command reference
    print("  s (step)     — step into function")  # pdb command reference
    print("  c (continue) — run until next breakpoint")  # pdb command reference
    print("  p var        — print variable value")  # pdb command reference
    print("  l (list)     — show source code context")  # pdb command reference
    print("  q (quit)     — exit debugger")  # pdb command reference

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Alternative debug entry points")  # section header
    print("=" * 50)  # close header divider
    print("  python -m pdb core-python/modules/07-advanced-and-production/04_debugging_pdb.py")  # CLI pdb
    print("  pytest --pdb  (drop into debugger on test failure)")  # pytest integration


if __name__ == "__main__":  # run demo when executed directly
    main()  # start debugging demo
