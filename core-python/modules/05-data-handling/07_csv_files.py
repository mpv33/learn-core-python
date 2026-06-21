"""
07 — CSV Files
==============

THEORY
------
What:
  CSV (Comma-Separated Values) is a simple tabular text format. Python's `csv`
  module reads and writes rows with proper quoting and escaping.

Why:
  Spreadsheets, data exports, and legacy systems use CSV extensively. It's the
  simplest structured file format for tabular data.

Key rules:
  - Always pass `newline=""` when opening CSV files on Windows.
  - `csv.reader` / `csv.writer` work with lists; `DictReader` / `DictWriter` use dicts.
  - First row is often headers — `DictReader` treats it as field names automatically.
  - Specify `encoding="utf-8"` for text mode file opens.
  - `writer.writeheader()` writes column names for DictWriter.

When to use:
  - Importing/exporting spreadsheet data, reports, or database dumps.
  - Simple ETL pipelines where JSON/XML is overkill.

Common mistakes:
  - Omitting `newline=""` — extra blank lines on Windows.
  - Manual string splitting instead of `csv` module — breaks on quoted commas.
  - Not handling encoding — non-ASCII characters corrupt without UTF-8.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/07_csv_files.py
"""

import csv  # read and write comma-separated values
from pathlib import Path  # resolve paths relative to this script


def main() -> None:
    demo_file = Path(__file__).parent / "students.csv"  # output path for student demo

    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Write CSV with csv.writer")  # label first block
    print("=" * 50)  # close header

    rows = [  # table data as list of rows
        ["name", "age", "grade"],  # header row with column names
        ["Alice", 20, "A"],  # first student record
        ["Bob", 22, "B"],  # second student record
        ["Carol", 21, "A"],  # third student record
    ]
    with open(demo_file, "w", newline="", encoding="utf-8") as f:  # newline="" for Windows
        writer = csv.writer(f)  # create row-oriented CSV writer
        writer.writerows(rows)  # write all rows at once
    print("CSV written.")  # confirm file creation

    print("\n" + "=" * 50)  # divider before DictReader demo
    print("PRACTICE 2 — Read CSV with DictReader")  # label second block
    print("=" * 50)  # close header

    print("Students:")  # label parsed output
    with open(demo_file, "r", encoding="utf-8") as f:  # open CSV for reading
        reader = csv.DictReader(f)  # first row becomes field names; yield dicts
        for row in reader:  # iterate over each data row
            print(f"  {row['name']}: age={row['age']}, grade={row['grade']}")  # access by header

    print("\n" + "=" * 50)  # divider before DictWriter demo
    print("PRACTICE 3 — Write CSV with DictWriter")  # label third block
    print("=" * 50)  # close header

    dict_file = Path(__file__).parent / "products.csv"  # separate CSV for dict writing
    products = [  # records as list of dicts
        {"id": 1, "name": "Laptop", "price": 999.99},  # first product
        {"id": 2, "name": "Mouse", "price": 29.99},  # second product
        {"id": 3, "name": "Keyboard", "price": 79.99},  # third product
    ]
    with open(dict_file, "w", newline="", encoding="utf-8") as f:  # open new CSV for writing
        writer = csv.DictWriter(f, fieldnames=["id", "name", "price"])  # declare column order
        writer.writeheader()  # write header row from fieldnames
        writer.writerows(products)  # write each dict as one CSV row
    print(f"{dict_file.name} written.")  # confirm second CSV file

    print("\n" + "=" * 50)  # divider before custom delimiter demo
    print("PRACTICE 4 — Custom delimiter (TSV)")  # label fourth block
    print("=" * 50)  # close header

    tsv_file = Path(__file__).parent / "data.tsv"  # tab-separated values file
    with open(tsv_file, "w", newline="", encoding="utf-8") as f:  # open TSV for writing
        writer = csv.writer(f, delimiter="\t")  # tab instead of comma
        writer.writerow(["city", "population"])  # header row
        writer.writerow(["Mumbai", 20400000])  # first data row
        writer.writerow(["Delhi", 16700000])  # second data row
    with open(tsv_file, "r", encoding="utf-8") as f:  # read back TSV
        tsv_reader = csv.reader(f, delimiter="\t")  # tab-delimited reader
        for row in tsv_reader:  # print each row
            print(f"  {row}")  # display tab-separated row

    demo_file.unlink()  # delete students.csv demo file
    dict_file.unlink()  # delete products.csv demo file
    tsv_file.unlink()  # delete TSV demo file
    print("\nDemo files cleaned up.")  # confirm removal


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
