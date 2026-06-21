"""
06 — Parameterized Decorators

THEORY
------
What: Decorators that accept arguments require an extra nesting level:
      def outer(arg): def decorator(func): def wrapper(...): ...
Why:  Configure decorator behavior (retry count, cache size) at decoration time.
Key rules:
  - Three levels: factory → decorator → wrapper (when decorator takes args).
  - Class-based decorators implement __init__(func) and __call__(...).
  - functools.wraps still applies on the innermost wrapper.
When to use: Retries, rate limiting, repeat N times, role-based access control.
Common mistakes: Missing a nesting level; not using @wraps; storing mutable state on
                 the decorator class incorrectly across instances.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/06_decorator_patterns.py
"""

from functools import wraps  # keep wrapped function identity
import random  # simulate flaky network behavior


def repeat(times):  # outer factory receives decorator parameter
    def decorator(func):  # middle layer receives function to wrap
        @wraps(func)  # preserve function metadata
        def wrapper(*args, **kwargs):  # inner callable invoked on each call
            results = []  # collect each invocation result
            for _ in range(times):  # call wrapped function repeatedly
                results.append(func(*args, **kwargs))  # store one result per iteration
            return results  # return list of all outcomes
        return wrapper  # return repeated-call wrapper
    return decorator  # return configured decorator


def retry(max_attempts=3):  # configurable retry count
    def decorator(func):  # wrap target function
        @wraps(func)  # preserve metadata
        def wrapper(*args, **kwargs):  # retry loop around original call
            for attempt in range(1, max_attempts + 1):  # attempt 1 through max_attempts
                try:  # try operation once
                    return func(*args, **kwargs)  # return immediately on success
                except Exception as e:  # catch any failure
                    print(f"  Attempt {attempt} failed: {e}")  # log failed attempt
                    if attempt == max_attempts:  # no attempts left
                        raise  # re-raise last exception
        return wrapper  # return retry-enabled wrapper
    return decorator  # return configured retry decorator


class CountCalls:  # callable class tracks invocation count
    def __init__(self, func):  # store wrapped function at decoration time
        self.func = func  # original function reference
        self.count = 0  # number of times wrapper was called
        wraps(func)(self)  # copy __name__, __doc__, etc. onto instance

    def __call__(self, *args, **kwargs):  # invoked when decorated function is called
        self.count += 1  # increment call counter
        print(f"  Call #{self.count} to {self.func.__name__}")  # log call number
        return self.func(*args, **kwargs)  # delegate to original function


@repeat(3)  # repeat say_hello three times per call
def say_hello(name):  # simple greeting function
    return f"Hello, {name}!"  # greeting string


@retry(max_attempts=3)  # retry up to three times
def flaky_operation():  # randomly fails to demo retries
    if random.random() < 0.7:  # 70% failure rate
        raise ConnectionError("Network error")  # simulate transient failure
    return "Success!"  # occasional success


@CountCalls  # replace add with CountCalls(add)
def add(a, b):  # simple addition function
    return a + b  # return sum


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Parameterized repeat decorator")  # section header
    print("=" * 50)  # close header divider
    print(say_hello("Alice"))  # prints list of three identical greetings

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Retry decorator")  # section header
    print("=" * 50)  # close header divider
    random.seed(42)  # fix randomness for reproducible demo
    try:  # attempt flaky call with retries
        print(f"Flaky result: {flaky_operation()}")  # print success if any attempt works
    except ConnectionError:  # all retries exhausted
        print("All retries exhausted.")  # report final failure

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Class-based decorator")  # section header
    print("=" * 50)  # close header divider
    print(f"add(1,2)={add(1, 2)}, add(3,4)={add(3, 4)}, total calls={add.count}")  # show count


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
