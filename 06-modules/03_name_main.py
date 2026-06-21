"""03 — if __name__ == '__main__'"""

def main():
    print("Running as main script.")
    print("Useful for: CLI tools, tests, demos.")

def helper():
    return "helper result"

# This block runs ONLY when file is executed directly,
# NOT when imported as a module.
if __name__ == "__main__":
    main()
    print(f"Module name: {__name__}")

# When imported: __name__ == "03_name_main"
# When run directly: __name__ == "__main__"
