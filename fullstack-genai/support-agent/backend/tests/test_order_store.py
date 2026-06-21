from pathlib import Path

from app.services.order_store import OrderStore

SAMPLE_ORDERS = Path(__file__).resolve().parents[2] / "sample-data" / "orders.json"


def test_order_lookup_found():
    store = OrderStore(str(SAMPLE_ORDERS))
    order = store.get("ORD-1001")
    assert order is not None
    assert order["status"] == "shipped"


def test_order_lookup_missing():
    store = OrderStore(str(SAMPLE_ORDERS))
    assert store.get("ORD-9999") is None


def test_extract_order_id():
    assert OrderStore.extract_order_id("Where is order ORD-1003?") == "ORD-1003"
    assert OrderStore.extract_order_id("no id here") is None
