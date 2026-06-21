"""Utility functions for the demo package."""

APP_VERSION = "1.0.0"

def greet(name: str) -> str:
    return f"Hello from mymodule, {name}!"

def add(a, b):
    return a + b

def _internal_helper():
    """Prefix with _ to indicate 'private' (convention only)."""
    return "internal"
