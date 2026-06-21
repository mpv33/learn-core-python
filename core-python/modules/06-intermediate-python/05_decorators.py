"""
05 — Function Decorators

THEORY
------
What: A decorator wraps a function to extend or modify its behavior without changing
      its source code — syntactic sugar for func = decorator(func).
Why:  Reuse cross-cutting concerns (logging, timing, auth) across many functions.
Key rules:
  - A decorator is a callable that takes a function and returns a wrapper.
  - Use @wraps(func) from functools to preserve __name__, __doc__, etc.
  - Stacked decorators apply bottom-up: @a @b def f → f = a(b(f)).
When to use: Logging, caching, retries, access control, input validation wrappers.
Common mistakes: Forgetting @wraps (breaks introspection); wrapper not forwarding
                 *args/**kwargs; side effects that surprise callers.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/05_decorators.py
"""

from functools import wraps  # preserve wrapped function metadata
import time  # high-resolution timing for performance demo


def timer(func):  # decorator factory accepting target function
    @wraps(func)  # preserves func.__name__, __doc__
    def wrapper(*args, **kwargs):  # replacement callable with same signature
        start = time.perf_counter()  # record start time
        result = func(*args, **kwargs)  # call original function
        elapsed = time.perf_counter() - start  # compute elapsed seconds
        print(f"  {func.__name__} took {elapsed:.4f}s")  # log timing result
        return result  # forward original return value
    return wrapper  # return wrapped function to replace original


def log_calls(func):  # decorator that logs entry and exit
    @wraps(func)  # copy metadata from wrapped function
    def wrapper(*args, **kwargs):  # intercept every call
        print(f"  CALL {func.__name__}({args}, {kwargs})")  # log arguments
        result = func(*args, **kwargs)  # execute wrapped function
        print(f"  RETURN {result}")  # log return value
        return result  # propagate result to caller
    return wrapper  # expose wrapper as decorated function


def bold(func):  # outer decorator adds bold markers
    @wraps(func)  # preserve metadata through stack
    def wrapper(*args, **kwargs):  # wrap inner result
        return f"**{func(*args, **kwargs)}**"  # surround with double asterisks
    return wrapper  # return bold wrapper


def italic(func):  # inner decorator adds italic markers
    @wraps(func)  # preserve metadata
    def wrapper(*args, **kwargs):  # wrap original function output
        return f"_{func(*args, **kwargs)}_"  # surround with underscores
    return wrapper  # return italic wrapper


@timer  # equivalent to slow_add = timer(slow_add)
def slow_add(a, b):  # function whose runtime will be measured
    """Add two numbers slowly."""
    time.sleep(0.1)  # artificial delay to show timing
    return a + b  # return sum


@log_calls  # apply logging decorator
def multiply(a, b):  # simple function to trace
    return a * b  # return product


@bold  # applied second: bold(italic(greet))
@italic  # applied first: italic(greet)
def greet(name):  # returns plain greeting string
    return f"Hello, {name}"  # base message before decoration


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Timer decorator")  # section header
    print("=" * 50)  # close header divider
    result = slow_add(3, 5)  # invoke decorated function
    print(f"Result: {result}")  # show computed sum
    print(f"Function name preserved: {slow_add.__name__}")  # @wraps keeps original name
    print(f"Docstring preserved: {slow_add.__doc__}")  # @wraps keeps original docstring

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Logging decorator")  # section header
    print("=" * 50)  # close header divider
    multiply(4, 5)  # triggers call/return log lines

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Stacked decorators (bottom-up)")  # section header
    print("=" * 50)  # close header divider
    print(f"Stacked: {greet('Alice')}")  # output passes through italic then bold


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
