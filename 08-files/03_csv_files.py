"""03 — CSV Files"""

import csv
from pathlib import Path

demo_file = Path(__file__).parent / "students.csv"

# Write CSV
rows = [
    ["name", "age", "grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Carol", 21, "A"],
]

with open(demo_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("CSV written.")

# Read CSV
print("\nStudents:")
with open(demo_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']}: age={row['age']}, grade={row['grade']}")

# Write with DictWriter
dict_file = Path(__file__).parent / "products.csv"
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
]

with open(dict_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "price"])
    writer.writeheader()
    writer.writerows(products)
print(f"\n{dict_file.name} written.")

demo_file.unlink()
dict_file.unlink()
