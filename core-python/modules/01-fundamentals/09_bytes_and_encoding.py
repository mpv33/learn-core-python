"""
09 — Bytes, Bytearray, and Encoding: Binary Data in Python

THEORY
------
What is it?
    str holds Unicode text; bytes holds raw byte values (0–255). encode() converts
    str → bytes; decode() converts bytes → str. bytes is immutable; bytearray is
    mutable. b"..." literals hold ASCII-only byte sequences.

Why it matters
    Network I/O, file binary mode, cryptography, and APIs all use bytes. UTF-8 is
    the web standard — one character can be multiple bytes. Mishandling encoding
    causes mojibake and UnicodeDecodeError in production.

Key syntax/rules
    - text.encode("utf-8")           → bytes object from Unicode string
    - raw.decode("utf-8")            → str from bytes (specify encoding explicitly)
    - b"ASCII only"                  → bytes literal (ASCII characters only)
    - bytearray(b"hello")            → mutable byte sequence
    - errors="replace" / "ignore"    → handle invalid bytes on decode
    - encoded.hex()                  → hex string for debugging binary data

When to use
    - Reading/writing binary files (images, PDFs, network packets)
    - HTTP request/response bodies and socket communication
    - Hashing and encryption (operate on bytes, not str)
    - bytearray when you need in-place byte modification

Common mistakes
    - Assuming len(bytes) == len(str) for non-ASCII text
    - Decoding without specifying encoding (relies on locale default)
    - Concatenating str + bytes (TypeError — encode or decode first)
    - Using latin-1 or ascii when you mean utf-8

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/09_bytes_and_encoding.py
"""


def main() -> None:  # entry point that runs all bytes/encoding practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Encode and decode UTF-8")  # section title
    print("=" * 50)  # close section header
    text = "Hello, 世界"  # Unicode string with ASCII and non-ASCII characters
    encoded = text.encode("utf-8")  # convert text to raw bytes using UTF-8 encoding
    print(f"Text:    {text}")  # show original human-readable string
    print(f"Bytes:   {encoded}")  # show byte representation (b'...' prefix)
    print(f"Length:  {len(encoded)} bytes (not {len(text)} chars)")  # bytes count can exceed char count
    decoded = encoded.decode("utf-8")  # convert bytes back to a Unicode string
    print(f"Decoded: {decoded}")  # should match original text after round-trip

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — bytes vs bytearray")  # section title
    print("=" * 50)  # close section header
    b = b"ASCII only"  # bytes literal: only ASCII characters allowed
    print(f"bytes (immutable): {b}")  # display immutable bytes object
    ba = bytearray(b"hello")  # create mutable byte sequence from bytes
    ba[0] = ord("H")  # change first byte to uppercase H (ASCII code 72)
    print(f"bytearray (mutable): {ba}")  # show modified mutable bytes → bytearray(b'Hello')

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Error handling on decode")  # section title
    print("=" * 50)  # close section header
    raw = b"\xff\xfe"  # invalid UTF-8 byte sequence for demo
    try:
        raw.decode("utf-8")  # attempt strict decode — will raise an error
    except UnicodeDecodeError as e:  # catch decoding failure without crashing program
        print(f"Decode error: {e}")  # show why strict decoding failed
        print(f"Safe decode:  {raw.decode('utf-8', errors='replace')}")  # replace bad bytes with replacement char

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Hex representation")  # section title
    print("=" * 50)  # close section header
    print(f"Hex: {encoded.hex()}")  # show bytes as hexadecimal string for inspection
    print(f"From hex: {bytes.fromhex(encoded.hex())}")  # round-trip hex back to bytes

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Practical: file header sniffing")  # section title
    print("=" * 50)  # close section header
    png_header = b"\x89PNG\r\n\x1a\n"  # first 8 bytes of any valid PNG file
    pdf_header = b"%PDF"  # PDF files start with this ASCII magic bytes
    samples = [("image.png", png_header), ("doc.pdf", pdf_header)]  # fake filenames with headers
    for filename, header in samples:  # check each sample file header
        kind = "PNG image" if header.startswith(b"\x89PNG") else "PDF document"  # detect file type
        print(f"  {filename}: {kind} (header: {header[:4].hex()})")  # show detected type and hex


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all bytes/encoding practice sections
