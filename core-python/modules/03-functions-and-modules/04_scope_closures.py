"""
04 — Scope and Closures

THEORY
------
What is it?
    Scope determines where a name is visible. Python follows the LEGB rule:
    Local → Enclosing → Global → Built-in. A closure is an inner function that
    remembers variables from its enclosing scope even after the outer function returns.

Why it matters
    Scope bugs (accidental shadowing, unintended mutation) are common in real code.
    Closures power factories, decorators, and callbacks. Understanding global,
    nonlocal, and LEGB is essential for interviews and debugging.

Key syntax/rules
    - Local: names assigned inside a function belong to that function
    - global x declares intent to read/write module-level x inside a function
    - nonlocal x modifies a variable in the nearest enclosing (non-global) scope
    - Inner functions can read enclosing variables; nonlocal needed to reassign them
    - Closure: inner function + captured environment returned from outer function
    - LEGB lookup order: Local first, then Enclosing, Global, Built-in

When to use
    - global: sparingly, for module-level counters or config flags
    - nonlocal: when inner function must update outer function's state
    - Closures: factory functions (make_multiplier), private state (make_counter)
    - Prefer passing arguments over globals for testability

Common mistakes
    - Forgetting global/nonlocal when reassigning outer variables — creates a new local instead
    - Using global when nonlocal is needed (inside nested functions)
    - Closure late-binding in loops — all closures capture the same variable reference
    - Shadowing built-ins (list = [...]) hides the built-in list type

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/04_scope_closures.py
"""

x = "global"  # global variable x defined at module level


def demo_scope():  # function that shadows global x with a local
    x = "local"  # local x shadows the global x inside this function
    print(f"  Inside function: {x}")  # print the local x


counter = 0  # module-level counter starting at 0


def increment():  # function that modifies global counter
    global counter  # declare intent to modify the global counter
    counter += 1  # increment the global counter by 1


def outer():  # outer function demonstrating nonlocal
    message = "Hello"  # variable in outer function's scope

    def inner():  # inner function that modifies outer's message
        nonlocal message  # declare intent to modify outer's message, not create local
        message = "Hello, World!"  # update the enclosing scope's message

    inner()  # call inner to modify message
    return message  # return the updated message from outer scope


def make_multiplier(factor):  # factory function that returns a closure
    def multiply(n):  # inner function captures factor from enclosing scope
        return n * factor  # use captured factor even after make_multiplier returns
    return multiply  # return the inner function (closure)


def make_counter(start=0):  # practical closure: counter factory
    count = start  # private counter variable in enclosing scope

    def increment(step=1):  # inner increment function with optional step
        nonlocal count  # modify the enclosed count variable
        count += step  # add step to private counter
        return count  # return updated count

    return increment  # return the increment function (closure)


def main() -> None:  # entry point that runs all scope and closure practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Local vs global")  # section title
    print("=" * 50)  # close section header
    demo_scope()  # call function to show local x
    print(f"Outside function: {x}")  # outside function, global x is unchanged

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Modify global variable")  # section title
    print("=" * 50)  # close section header
    increment()  # call increment first time
    increment()  # call increment second time
    print(f"Counter: {counter}")  # show updated global counter

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — nonlocal in nested functions")  # section title
    print("=" * 50)  # close section header
    print(f"Outer after inner: {outer()}")  # show message after inner function modified it

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Closures")  # section title
    print("=" * 50)  # close section header
    times3 = make_multiplier(3)  # create closure that remembers factor 3
    times5 = make_multiplier(5)  # create closure that remembers factor 5
    print(f"times3(4) = {times3(4)}, times5(4) = {times5(4)}")  # each closure uses its own factor

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Counter factory")  # section title
    print("=" * 50)  # close section header
    counter_fn = make_counter(10)  # create a counter starting at 10
    print(f"Counter: {counter_fn()}, {counter_fn()}, {counter_fn(5)}")  # increment and show values

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — LEGB rule")  # section title
    print("=" * 50)  # close section header
    print(f"Built-in len: {len([1, 2, 3])}")  # len is a built-in from Built-in scope

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Practical: rate limiter factory")  # section title
    print("=" * 50)  # close section header
    def make_rate_limiter(max_calls: int):  # closure-based rate limiter
        calls = 0  # private call counter in enclosing scope

        def allow() -> bool:  # check if another call is allowed
            nonlocal calls  # modify enclosed calls counter
            if calls < max_calls:  # still under the limit
                calls += 1  # increment call count
                return True  # allow this call
            return False  # reject — limit reached

        return allow  # return the allow checker function

    limiter = make_rate_limiter(2)  # allow at most 2 calls
    print(f"Call 1 allowed: {limiter()}")  # first call — True
    print(f"Call 2 allowed: {limiter()}")  # second call — True
    print(f"Call 3 allowed: {limiter()}")  # third call — False (limit hit)


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all scope and closure practice sections
