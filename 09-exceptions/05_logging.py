"""
05 — Logging Module (Production Standard)
==========================================
Never use print() in production. Use logging with levels and handlers.
"""

import logging
import sys

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)

def process_order(order_id: int, amount: float) -> bool:
    logger.info("Processing order %s, amount=$%.2f", order_id, amount)

    if amount <= 0:
        logger.error("Invalid amount for order %s: %s", order_id, amount)
        return False

    if amount > 10_000:
        logger.warning("Large transaction flagged: order %s", order_id)

    logger.debug("Validation passed for order %s", order_id)
    return True

# Log levels (lowest to highest): DEBUG → INFO → WARNING → ERROR → CRITICAL
logger.debug("Detailed diagnostic info")
logger.info("General operational message")
logger.warning("Something unexpected")
logger.error("Serious problem")
logger.critical("System failure")

print("\n--- Demo ---")
process_order(1001, 250.00)
process_order(1002, -50.00)
process_order(1003, 15000.00)

# Production pattern: configure once at app startup
# Handlers: FileHandler, RotatingFileHandler, StreamHandler
# logger = logging.getLogger("myapp.api")  # hierarchical names
