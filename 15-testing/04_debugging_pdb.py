"""
04 — Debugging with pdb
========================
Python Debugger — set breakpoints, inspect variables, step through code.
"""

def calculate_discount(price: float, discount_pct: float) -> float:
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("Discount must be 0-100")
    return price * (1 - discount_pct / 100)

def checkout(items: list[dict]) -> float:
    total = 0.0
    for item in items:
        price = item["price"]
        discount = item.get("discount", 0)
        final = calculate_discount(price, discount)
        total += final
    return round(total, 2)

# Method 1: breakpoint() — Python 3.7+ (calls pdb.set_trace())
def debug_checkout():
    cart = [
        {"name": "Book", "price": 29.99, "discount": 10},
        {"name": "Pen", "price": 2.50, "discount": 0},
    ]
    # breakpoint()  # Uncomment to debug interactively
    total = checkout(cart)
    print(f"Total: ${total:.2f}")

# pdb commands (when breakpoint hits):
#   n (next)     — next line
#   s (step)     — step into function
#   c (continue) — run until next breakpoint
#   p var        — print variable
#   l (list)     — show source code
#   q (quit)     — exit debugger

# Method 2: python -m pdb script.py
# Method 3: pytest --pdb  (drop into debugger on test failure)

if __name__ == "__main__":
    debug_checkout()
    print("\nRun with: python -m pdb 15-testing/04_debugging_pdb.py")
