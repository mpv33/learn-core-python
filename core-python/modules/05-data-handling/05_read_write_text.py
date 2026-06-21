"""
05 — Read and Write Text Files
==============================

THEORY
------
What:
  Files store persistent text data on disk. Python's `open()` function (or
  `pathlib.Path` helpers) reads and writes text with explicit encoding (UTF-8).

Why:
  Config files, logs, reports, and data exports all live on disk. File I/O is
  essential for scripts, pipelines, and applications.

Key rules:
  - Always specify `encoding="utf-8"` for text files.
  - Use `with open(...) as f:` — ensures the file closes even on errors.
  - Modes: `"r"` read, `"w"` write (overwrite), `"a"` append, `"x"` exclusive create.
  - `f.read()` loads entire file; iterating `for line in f` is memory-efficient.
  - `pathlib.Path` provides `.read_text()` / `.write_text()` shortcuts.

When to use:
  - Reading config, CSV exports, or log files.
  - Writing reports, generated code, or processed output.
  - Appending to log files without rewriting the whole file.

Common mistakes:
  - Omitting `encoding="utf-8"` — platform-dependent default can corrupt Unicode.
  - Not using `with` — file handles leak if an exception occurs.
  - Using `readlines()` on huge files — loads everything into memory at once.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/05_read_write_text.py
"""

from pathlib import Path  # object-oriented filesystem paths


def main() -> None:
    demo_file = Path(__file__).parent / "sample.txt"  # temp file beside this script

    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Write text to a file")  # label first block
    print("=" * 50)  # close header

    with open(demo_file, "w", encoding="utf-8") as f:  # open for writing; auto-close on exit
        f.write("Line 1: Hello\n")  # write one string including newline
        f.write("Line 2: Python\n")  # write another line
        f.writelines(["Line 3: Files\n", "Line 4: Done\n"])  # write multiple strings
    print(f"Written to {demo_file.name}")  # confirm write using filename only

    print("\n" + "=" * 50)  # divider before read demo
    print("PRACTICE 2 — Read entire file and line by line")  # label second block
    print("=" * 50)  # close header

    with open(demo_file, "r", encoding="utf-8") as f:  # open for reading as text
        content = f.read()  # load full file contents into one string
    print(f"Full content:\n{content}")  # display everything written
    print("Line by line:")  # label streaming read demo
    with open(demo_file, "r", encoding="utf-8") as f:  # reopen for iteration
        for line_num, line in enumerate(f, 1):  # 1-based line numbers
            print(f"  {line_num}: {line.rstrip()}")  # strip trailing newline before print

    print("\n" + "=" * 50)  # divider before append demo
    print("PRACTICE 3 — Append and inspect file metadata")  # label third block
    print("=" * 50)  # close header

    with open(demo_file, "a", encoding="utf-8") as f:  # append mode adds at end
        f.write("Line 5: Appended\n")  # write extra line without overwriting
    with open(demo_file, "r", encoding="utf-8") as f:  # reopen for list-based read
        lines = f.readlines()  # read all lines into a list
    print(f"Total lines after append: {len(lines)}")  # report line count
    print(f"Exists: {demo_file.exists()}")  # True while file is on disk
    print(f"Size: {demo_file.stat().st_size} bytes")  # file size from metadata

    print("\n" + "=" * 50)  # divider before pathlib shortcut demo
    print("PRACTICE 4 — pathlib read_text / write_text shortcuts")  # label fourth block
    print("=" * 50)  # close header

    quick_file = Path(__file__).parent / "quick.txt"  # second temp file for pathlib demo
    quick_file.write_text("Written via pathlib!\n", encoding="utf-8")  # one-call write
    print(f"Pathlib read: {quick_file.read_text(encoding='utf-8').strip()}")  # one-call read
    quick_file.unlink()  # delete pathlib demo file
    demo_file.unlink()  # delete main demo file
    print("Demo files cleaned up.")  # confirm removal


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
