"""
13 — match / case: Structural Pattern Matching (Python 3.10+)

THEORY
------
What is it?
    match/case performs structural pattern matching — like switch/case but matches
    shapes, not just values. Patterns can destructure tuples, lists, and objects.
    case _: is the wildcard default. Guards (case x if condition) add extra checks.

Why it matters
    Cleaner than long if/elif chains for dispatching on types or shapes. Parses
    HTTP status codes, AST nodes, and API payloads idiomatically. Requires Python
    3.10+ — verify with 01_verify_installation.py.

Key syntax/rules
    - match subject:                 → compare subject against case patterns
    - case 200:                     → literal value match
    - case 500 | 502 | 503:         → combine patterns with | (OR)
    - case x if x > 0:               → capture value x and apply guard condition
    - case (0, 0):                   → tuple destructuring
    - case [first, *rest]:           → list pattern with star capture
    - case _:                       → wildcard — matches anything (must be last)

When to use
    - Dispatching on enums, status codes, or command types
    - Destructuring tuples and lists in one step
    - Parsing structured data (JSON-like dicts with match enhancements in 3.10+)
    - Replacing isinstance() + if/elif chains for type-based routing

Common mistakes
    - Using match on Python < 3.10 (SyntaxError)
    - Forgetting case _ default — MatchError if nothing matches
    - Expecting fall-through like C switch — only first match runs
    - Confusing | in patterns (OR) with | in type hints (union)

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/13_match_case.py
"""


def describe_http_status(code: int) -> str:  # map numeric HTTP codes to readable labels
    match code:  # compare code against multiple patterns
        case 200:  # exact match for success status
            return "OK"  # standard success response
        case 404:  # exact match for missing resource
            return "Not Found"  # client requested unknown URL
        case 500 | 502 | 503:  # combine several server-error codes with OR
            return "Server Error"  # any listed code counts as server failure
        case code if 400 <= code < 500:  # guard clause for other 4xx client errors
            return f"Client Error ({code})"  # include actual code in message
        case _:  # wildcard catches anything not matched above
            return "Unknown Status"  # fallback for unexpected codes


def head_tail(lst: list) -> str:  # describe list shape using pattern matching
    match lst:  # inspect list length and contents
        case []:  # empty list pattern
            return "Empty list"  # no elements to report
        case [single]:  # exactly one element captured as single
            return f"One item: {single}"  # describe lone element
        case [first, *rest]:  # first item plus remaining tail as rest
            return f"First: {first}, Rest: {rest}"  # split head from tail


def main() -> None:  # entry point that runs all match/case practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — HTTP status code dispatch")  # section title
    print("=" * 50)  # close section header
    for code in [200, 404, 418, 500, 999]:  # sample codes including edge cases
        print(f"  {code}: {describe_http_status(code)}")  # print label for each test code

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Tuple pattern matching")  # section title
    print("=" * 50)  # close section header
    points = [(0, 0), (1, 0), (3, 4), (2, 2)]  # sample (x, y) coordinates to classify
    for x, y in points:  # unpack each coordinate pair
        match (x, y):  # pattern-match on tuple structure
            case (0, 0):  # both coordinates zero
                label = "Origin"  # point at center of axes
            case (0, _):  # x is 0, y can be anything
                label = "On Y-axis"  # vertical axis point
            case (_, 0):  # y is 0, x can be anything
                label = "On X-axis"  # horizontal axis point
            case (a, b) if a == b:  # capture values and require equality
                label = "On diagonal"  # point where x equals y
            case _:  # all other coordinate pairs
                label = "General point"  # generic location in plane
        print(f"  ({x},{y}) → {label}")  # show classification for each point

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — List pattern matching")  # section title
    print("=" * 50)  # close section header
    for sample in [[], [42], [1, 2, 3, 4]]:  # test empty, single, and multi-item lists
        print(f"  {sample} → {head_tail(sample)}")  # show pattern match result for each

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Practical: CLI command router")  # section title
    print("=" * 50)  # close section header
    commands = ["help", "quit", "unknown"]  # simulated user commands to dispatch
    for cmd in commands:  # route each command through match/case
        match cmd:  # match on command string
            case "help":  # user asked for help
                response = "Available: help, quit"  # show available commands
            case "quit":  # user wants to exit
                response = "Goodbye!"  # farewell message
            case _:  # any unrecognized command
                response = f"Unknown command: {cmd}"  # error message with command name
        print(f"  > {cmd} → {response}")  # show command and routed response


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all match/case practice sections
