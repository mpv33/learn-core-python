"""
19 — Design Patterns in Python

THEORY
------
What: Reusable solutions to common software design problems — Strategy, Factory, Singleton,
      Repository, and others adapted to Python's dynamic nature.
Why:  Communicate architecture intent; decouple components; enable testing and extension.
Key rules:
  - Strategy: inject behavior via interface/Protocol; swap at runtime.
  - Factory: classmethod create() validates and constructs the right type.
  - Singleton: module-level instance is the Pythonic approach (not complex metaclass).
When to use: Payment methods, DB backends, plugin systems, data access layers.
Common mistakes: Over-engineering simple code with patterns; Singleton abuse; pattern
                 names without actual decoupling benefit.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/19_design_patterns.py
"""

from abc import ABC, abstractmethod  # abstract base classes for strategy pattern


class PaymentStrategy(ABC):  # abstract payment interface
    @abstractmethod
    def pay(self, amount: float) -> str: ...  # each strategy implements pay()


class CreditCard(PaymentStrategy):  # concrete credit card strategy
    def pay(self, amount: float) -> str:  # charge amount to card
        return f"Charged ${amount:.2f} to credit card"


class PayPal(PaymentStrategy):  # concrete PayPal strategy
    def pay(self, amount: float) -> str:  # pay amount via PayPal
        return f"Paid ${amount:.2f} via PayPal"


class Checkout:  # context object delegating payment to strategy
    def __init__(self, strategy: PaymentStrategy):  # inject chosen payment strategy
        self._strategy = strategy

    def process(self, amount: float) -> str:  # execute payment through strategy
        return self._strategy.pay(amount)


class DatabaseConnection:  # connection wrapper selected by factory method
    def __init__(self, db_type: str):  # store database type label
        self.db_type = db_type

    @classmethod
    def create(cls, db_type: str) -> "DatabaseConnection":  # validate and construct instance
        if db_type not in ("postgres", "mysql", "sqlite"):  # reject unsupported types
            raise ValueError(f"Unknown DB: {db_type}")
        return cls(db_type)  # return configured connection object


class _Config:  # private config class instantiated once below
    def __init__(self):  # default configuration values
        self.debug = False
        self.max_connections = 10


config = _Config()  # single instance imported everywhere (Pythonic singleton)


class UserRepository:  # in-memory persistence layer for users
    def __init__(self):  # initialize empty storage dict
        self._store: dict[int, dict] = {}

    def save(self, user_id: int, data: dict) -> None:  # upsert user record by id
        self._store[user_id] = data

    def find(self, user_id: int) -> dict | None:  # fetch user record or None
        return self._store.get(user_id)


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Strategy pattern")  # section header
    print("=" * 50)  # close header divider
    checkout = Checkout(CreditCard())  # checkout using credit card strategy
    print(checkout.process(99.99))  # process sample payment
    paypal_checkout = Checkout(PayPal())  # swap to PayPal strategy
    print(paypal_checkout.process(49.99))  # process with different strategy

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Factory pattern")  # section header
    print("=" * 50)  # close header divider
    db = DatabaseConnection.create("postgres")  # create postgres connection via factory
    print(f"DB: {db.db_type}")  # show selected database type

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Repository pattern")  # section header
    print("=" * 50)  # close header divider
    repo = UserRepository()  # create in-memory user repository
    repo.save(1, {"name": "Alice"})  # persist user id 1
    print(f"User: {repo.find(1)}")  # retrieve saved user

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Module-level singleton")  # section header
    print("=" * 50)  # close header divider
    print(f"Config singleton: max_conn={config.max_connections}")  # read shared config instance


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
