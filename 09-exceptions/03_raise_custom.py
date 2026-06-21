"""03 — raise and Custom Exceptions"""

# raise — manually trigger an exception
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance={balance}, requested={amount}")
    return balance - amount

try:
    print(f"Withdraw 50: {withdraw(100, 50)}")
    withdraw(100, 200)
except ValueError as e:
    print(f"  Transaction failed: {e}")

# Custom exception hierarchy
class AppError(Exception):
    """Base exception for our app."""
    pass

class ValidationError(AppError):
    """Invalid input data."""
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    """Resource not found."""
    pass

def get_user(user_id):
    users = {1: "Alice", 2: "Bob"}
    if user_id not in users:
        raise NotFoundError(f"User {user_id} not found")
    return users[user_id]

def validate_email(email):
    if "@" not in email:
        raise ValidationError("email", "must contain @")
    return email

try:
    validate_email("invalid-email")
except ValidationError as e:
    print(f"\nValidation failed on '{e.field}': {e}")

try:
    get_user(99)
except NotFoundError as e:
    print(f"Not found: {e}")

# Re-raise with context
try:
    int("not-a-number")
except ValueError:
    raise AppError("Failed to parse configuration value") from None
