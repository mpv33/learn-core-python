"""
05 — Design Patterns in Python
===============================
Common patterns asked in senior-level interviews.
"""

from abc import ABC, abstractmethod
from functools import lru_cache


# --- Strategy Pattern ---
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str: ...


class CreditCard(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Charged ${amount:.2f} to credit card"


class PayPal(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} via PayPal"


class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process(self, amount: float) -> str:
        return self._strategy.pay(amount)


# --- Factory Pattern ---
class DatabaseConnection:
    def __init__(self, db_type: str):
        self.db_type = db_type

    @classmethod
    def create(cls, db_type: str) -> "DatabaseConnection":
        if db_type not in ("postgres", "mysql", "sqlite"):
            raise ValueError(f"Unknown DB: {db_type}")
        return cls(db_type)


# --- Singleton (module-level — Pythonic way) ---
class _Config:
    def __init__(self):
        self.debug = False
        self.max_connections = 10

config = _Config()  # single instance imported everywhere


# --- Repository Pattern (data access abstraction) ---
class UserRepository:
    def __init__(self):
        self._store: dict[int, dict] = {}

    def save(self, user_id: int, data: dict) -> None:
        self._store[user_id] = data

    def find(self, user_id: int) -> dict | None:
        return self._store.get(user_id)


if __name__ == "__main__":
    checkout = Checkout(CreditCard())
    print(checkout.process(99.99))

    db = DatabaseConnection.create("postgres")
    print(f"DB: {db.db_type}")

    repo = UserRepository()
    repo.save(1, {"name": "Alice"})
    print(f"User: {repo.find(1)}")

    print(f"Config singleton: max_conn={config.max_connections}")
