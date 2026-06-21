"""Example application package."""

from .utils import format_greeting

APP_NAME = "MyApp"
VERSION = "1.0.0"

def run():
    print(f"{APP_NAME} v{VERSION} running.")

__all__ = ["APP_NAME", "VERSION", "run", "format_greeting"]
