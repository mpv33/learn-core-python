"""
06 — Bytes, Bytearray, and Encoding
====================================
Used in: network I/O, file binary mode, cryptography, APIs.
"""

text = "Hello, 世界"
encoded = text.encode("utf-8")
print(f"Text:    {text}")
print(f"Bytes:   {encoded}")
print(f"Length:  {len(encoded)} bytes (not {len(text)} chars)")

decoded = encoded.decode("utf-8")
print(f"Decoded: {decoded}")

# bytes — immutable
b = b"ASCII only"
print(f"\nbytes literal: {b}")

# bytearray — mutable
ba = bytearray(b"hello")
ba[0] = ord("H")
print(f"bytearray: {ba}")

# Common encoding error handling
raw = b"\xff\xfe"
try:
    raw.decode("utf-8")
except UnicodeDecodeError as e:
    print(f"\nDecode error: {e}")
    print(f"Safe decode:  {raw.decode('utf-8', errors='replace')}")

# hex representation (debugging binary data)
print(f"\nHex: {encoded.hex()}")
