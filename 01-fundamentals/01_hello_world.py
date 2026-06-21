"""
01 — Hello World
================

Your first Python program. The print() function sends text to the console.
"""

# Single-line comment: ignored by Python

print("Hello, World!")  # Output: Hello, World!

# print() can take multiple arguments separated by commas
print("Hello", "Python", "Learner")

# You can use single or double quotes for strings
print('Both quote styles work')

"""
Multi-line comment (docstring style).
Often used at the top of files to describe the module.
"""

# sep: separator between items (default is space)
print("a", "b", "c", sep="-")  # a-b-c

# end: what to print after (default is newline)
print("Line 1", end=" | ")
print("Line 2")  # Line 1 | Line 2
