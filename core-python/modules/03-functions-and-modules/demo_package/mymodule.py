"""Utility functions for the demo package."""

# Package version constant
APP_VERSION = "1.0.0"

# Public greeting function
def greet(name: str) -> str:
    # Return a greeting string with the given name
    return f"Hello from mymodule, {name}!"

# Public addition function
def add(a, b):
    # Return sum of two values
    return a + b

# Private helper (underscore prefix is a convention, not enforced)
def _internal_helper():
    """Prefix with _ to indicate 'private' (convention only)."""
    # Return internal string — not meant for external use
    return "internal"
