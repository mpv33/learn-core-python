"""
11 — raise and Custom Exceptions
==================================

THEORY
------
What:
  Use `raise` to signal errors explicitly. Custom exception classes (inheriting
  from `Exception`) let callers catch domain-specific failures precisely.

Why:
  Built-in exceptions (ValueError, KeyError) are generic. Custom exceptions
  (`ValidationError`, `NotFoundError`) communicate intent and enable targeted handling.

Key rules:
  - `raise ValueError("message")` triggers an exception with a descriptive message.
  - Define custom classes: `class AppError(Exception): pass`.
  - Build hierarchies: base `AppError` → `ValidationError`, `NotFoundError`.
  - Store extra context on the exception: `self.field = field`.
  - `raise NewError("msg") from None` suppresses exception chaining.

When to use:
  - Business rule violations (insufficient funds, invalid email).
  - Missing resources (user not found, file not found).
  - Wrapping low-level errors into application-level exceptions.

Common mistakes:
  - Catching too broadly and losing the original error message.
  - Creating too many exception classes — start with a small hierarchy.
  - Raising exceptions for expected control flow instead of return values.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/11_raise_custom.py
"""


class AppError(Exception):
    """Base exception for our app."""

    pass  # no extra behavior on the base class


class ValidationError(AppError):
    """Invalid input data."""

    def __init__(self, field, message):
        self.field = field  # attribute for programmatic handling
        super().__init__(f"{field}: {message}")  # human-readable message via Exception


class NotFoundError(AppError):
    """Resource not found."""

    pass  # inherits AppError semantics


def withdraw(balance, amount):
    if amount <= 0:  # disallow zero or negative withdrawals
        raise ValueError("Amount must be positive")  # invalid request
    if amount > balance:  # disallow overdrawing the account
        raise ValueError(f"Insufficient funds: balance={balance}, requested={amount}")  # business rule
    return balance - amount  # return remaining balance after successful withdrawal


def get_user(user_id):
    users = {1: "Alice", 2: "Bob"}  # in-memory user store
    if user_id not in users:  # unknown id
        raise NotFoundError(f"User {user_id} not found")  # signal missing resource
    return users[user_id]  # return username for known id


def validate_email(email):
    if "@" not in email:  # missing required character
        raise ValidationError("email", "must contain @")  # field-specific validation error
    return email  # return unchanged when valid


def main() -> None:
    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — raise with built-in exceptions")  # label first block
    print("=" * 50)  # close header

    try:  # demonstrate successful and failing withdrawals
        print(f"Withdraw 50: {withdraw(100, 50)}")  # valid withdrawal
        withdraw(100, 200)  # raises ValueError for insufficient funds
    except ValueError as e:  # handle transaction errors
        print(f"  Transaction failed: {e}")  # show rejection reason

    print("\n" + "=" * 50)  # divider before custom exception demo
    print("PRACTICE 2 — Custom exception hierarchy")  # label second block
    print("=" * 50)  # close header

    try:  # trigger validation failure
        validate_email("invalid-email")  # raises ValidationError
    except ValidationError as e:  # catch custom validation exception
        print(f"Validation failed on '{e.field}': {e}")  # show field name and message

    try:  # trigger not-found failure
        get_user(99)  # raises NotFoundError
    except NotFoundError as e:  # catch custom not-found exception
        print(f"Not found: {e}")  # show lookup failure message

    print(f"User 1: {get_user(1)}")  # successful lookup for contrast

    print("\n" + "=" * 50)  # divider before re-raise demo
    print("PRACTICE 3 — Re-raise with context")  # label third block
    print("=" * 50)  # close header

    try:  # demonstrate wrapping a low-level error in an app-level exception
        try:  # inner parse attempt
            int("not-a-number")  # raises ValueError
        except ValueError:  # swallow original ValueError
            raise AppError("Failed to parse configuration value") from None  # app error, no chain
    except AppError as e:  # catch the wrapped application error
        print(f"AppError: {e}")  # show clean message without ValueError chain


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
