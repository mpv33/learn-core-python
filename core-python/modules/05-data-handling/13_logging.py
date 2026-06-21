"""
13 — Logging Module (Production Standard)
=========================================

THEORY
------
What:
  Python's `logging` module provides structured, level-based messages with
  timestamps, logger names, and configurable handlers (console, file, rotation).

Why:
  Replace `print()` in production — logs can be filtered by severity, routed to
  files, and integrated with monitoring tools (Datadog, CloudWatch, ELK).

Key rules:
  - Levels (low→high): DEBUG → INFO → WARNING → ERROR → CRITICAL.
  - `logging.basicConfig(...)` sets global defaults (once at startup).
  - `logger = logging.getLogger(__name__)` — one logger per module.
  - Use lazy formatting: `logger.info("Order %s", order_id)` not f-strings.
  - Handlers: StreamHandler (console), FileHandler, RotatingFileHandler.

When to use:
  - Any production script, API, or long-running service.
  - Debugging with DEBUG level; operational events with INFO/WARNING.
  - ERROR/CRITICAL for failures requiring attention.

Common mistakes:
  - Using `print()` instead of logging in production code.
  - Calling `basicConfig()` multiple times — only the first call takes effect.
  - Logging at DEBUG in production — floods output and hurts performance.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/13_logging.py
"""

import logging  # structured application logging
import sys  # access stdout for log stream configuration

logger = logging.getLogger(__name__)  # module-level logger named after this file


def process_order(order_id: int, amount: float) -> bool:
    logger.info("Processing order %s, amount=$%.2f", order_id, amount)  # log normal workflow event

    if amount <= 0:  # invalid business input
        logger.error("Invalid amount for order %s: %s", order_id, amount)  # log error and reject
        return False  # signal failure

    if amount > 10_000:  # unusually large transaction
        logger.warning("Large transaction flagged: order %s", order_id)  # log warning for review

    logger.debug("Validation passed for order %s", order_id)  # verbose diagnostic detail
    return True  # order accepted


def main() -> None:
    logging.basicConfig(  # one-time global logging setup
        level=logging.DEBUG,  # emit DEBUG and all higher-severity messages
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",  # structured format
        datefmt="%H:%M:%S",  # short time format in log lines
        stream=sys.stdout,  # send log records to standard output
    )

    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Log levels")  # label first block
    print("=" * 50)  # close header

    logger.debug("Detailed diagnostic info")  # lowest severity; hidden if level is INFO+
    logger.info("General operational message")  # routine informational event
    logger.warning("Something unexpected")  # potential problem, execution continues
    logger.error("Serious problem")  # operation failed but app may continue
    logger.critical("System failure")  # highest severity; may abort application

    print("\n" + "=" * 50)  # divider before business function demo
    print("PRACTICE 2 — Logging in business functions")  # label second block
    print("=" * 50)  # close header

    process_order(1001, 250.00)  # normal order succeeds
    process_order(1002, -50.00)  # invalid amount triggers error log
    process_order(1003, 15000.00)  # large amount triggers warning log

    print("\n" + "=" * 50)  # divider before logger hierarchy demo
    print("PRACTICE 3 — Logger hierarchy and naming")  # label third block
    print("=" * 50)  # close header

    api_logger = logging.getLogger("myapp.api")  # hierarchical child logger
    db_logger = logging.getLogger("myapp.db")  # another child logger
    api_logger.info("API request received")  # log from api subsystem
    db_logger.info("Database query executed")  # log from db subsystem
    print(f"Root logger: {logging.getLogger().name or 'root'}")  # empty string means root
    print(f"Module logger: {logger.name}")  # shows __main__ or module path


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
