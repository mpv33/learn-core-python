"""Demo package — groups related modules."""

# Relative import from sibling module inside the package
from .mymodule import greet, add, APP_VERSION

# Define which names are exported when using from demo_package import *
__all__ = ["greet", "add", "APP_VERSION"]
