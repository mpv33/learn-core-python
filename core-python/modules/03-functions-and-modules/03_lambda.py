"""
03 — Lambda: Small Anonymous Functions

THEORY
------
What is it?
    A lambda is a one-line anonymous function defined with lambda params: expression.
    Lambdas can take any number of arguments but contain only a single expression
    — no statements, no assignments, no multi-line logic.

Why it matters
    Lambdas shine as short callbacks for sorted(), map(), filter(), and similar
    higher-order functions. They keep call sites concise, but overuse hurts
    readability — prefer def for anything non-trivial.

Key syntax/rules
    - Syntax: lambda x: x * 2 — no return keyword, expression is auto-returned
    - Can have multiple args: lambda a, b: a + b
    - Often passed as key= to sorted(): sorted(items, key=lambda x: x["score"])
    - map(fn, iterable) applies fn to each item; filter(fn, iterable) keeps truthy results
    - Lambdas are expressions — assign to a variable only when reused briefly

When to use
    - Short key functions for sorting or grouping
    - One-off transformations in map/filter (though list comprehensions often read better)
    - Callbacks expected by APIs (GUI events, sort keys)
    - When the function is used once and is truly one line

Common mistakes
    - Using lambda for complex logic — use def with a name instead
    - Assigning lambdas to variables when def is clearer: square = lambda x: x**2
    - Late-binding closure bug in loops: [lambda: i for i in range(3)] captures last i
    - Expecting statements inside lambda — only expressions allowed

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/03_lambda.py
"""


def is_valid_email(email: str) -> bool:  # named function for logic too complex for lambda
    return "@" in email and "." in email.split("@")[-1]  # check @ and dot in domain part


def main() -> None:  # entry point that runs all lambda practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Basic lambda")  # section title
    print("=" * 50)  # close section header
    square = lambda x: x ** 2  # assign a one-line anonymous function
    print(f"square(5) = {square(5)}")  # call the lambda like any function
    add = lambda a, b: a + b  # lambda accepting two arguments
    print(f"lambda add: {add(3, 7)}")  # call lambda with two values

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — sorted with key=lambda")  # section title
    print("=" * 50)  # close section header
    students = [  # list of student dicts with name and score
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 85},
        {"name": "Carol", "score": 98},
    ]
    by_score = sorted(students, key=lambda s: s["score"], reverse=True)  # sort by score descending
    print("Top student:", by_score[0]["name"])  # first item is highest-scoring student

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — map and filter")  # section title
    print("=" * 50)  # close section header
    nums = [1, 2, 3, 4, 5]  # list of integers
    doubled = list(map(lambda x: x * 2, nums))  # map applies lambda to each element
    print(f"Doubled: {doubled}")  # show doubled values
    evens = list(filter(lambda x: x % 2 == 0, nums))  # filter keeps even numbers
    print(f"Evens: {evens}")  # show filtered even numbers

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — When NOT to use lambda")  # section title
    print("=" * 50)  # close section header
    print(f"Valid email: {is_valid_email('user@example.com')}")  # test email validation with def

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: sort by multiple keys")  # section title
    print("=" * 50)  # close section header
    employees = [  # sample records with department and salary
        {"name": "Alice", "dept": "Eng", "salary": 90000},
        {"name": "Bob", "dept": "Eng", "salary": 85000},
        {"name": "Carol", "dept": "HR", "salary": 70000},
    ]
    by_dept_salary = sorted(employees, key=lambda e: (e["dept"], -e["salary"]))  # dept asc, salary desc
    for emp in by_dept_salary:  # print sorted results
        print(f"  {emp['name']}: {emp['dept']}, ${emp['salary']}")  # show each employee row

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — Practical: filter active users")  # section title
    print("=" * 50)  # close section header
    users = [{"name": "A", "active": True}, {"name": "B", "active": False}, {"name": "C", "active": True}]  # user list
    active_names = [u["name"] for u in filter(lambda u: u["active"], users)]  # filter then extract names
    print(f"Active users: {active_names}")  # show names of active users only


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all lambda practice sections
