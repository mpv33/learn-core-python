"""Example application package."""

from .utils import format_greeting  # relative import of utility helper

APP_NAME = "MyApp"  # public application name constant
VERSION = "1.0.0"  # semantic version string

def run():  # package entry function called from main.py
    print(f"{APP_NAME} v{VERSION} running.")  # log startup banner

__all__ = ["APP_NAME", "VERSION", "run", "format_greeting"]  # explicit public API exports
