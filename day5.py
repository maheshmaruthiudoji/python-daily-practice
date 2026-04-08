

"""
Python List Operations Example
------------------------------
This script demonstrates:
- List mutability
- Indexing
- Slicing
- Built-in functions (max, min)
- Sorting (ascending & descending)
- Appending elements
"""

# Initial list
marks = [90, 56, 78, 58]
print("Original list:", marks)

# Modify element (lists are mutable)
marks[1] = 99
print("After updating index 1:", marks)

# Slicing
print("Sliced list (index 1 to 2):", marks[1:3])

# Built-in functions
print("Maximum value:", max(marks))
print("Minimum value:", min(marks))

# Sort in ascending order (small → big)
marks.sort()
print("Ascending order:", marks)

# Sort in descending order (big → small)
marks.sort(reverse=True)
print("Descending order:", marks)

# Append new element
marks.append(34)
print("After appending 34:", marks)

# Sort again in ascending order
marks.sort()
print("Final sorted list:", marks)