"""
Python Tuple Operations - Complete Guide
---------------------------------------
This script demonstrates:
- Tuple immutability
- Indexing & slicing
- Built-in functions (len, count, index)
- Iteration
- Tuple packing & unpacking
- Nested tuples
- Membership testing
- Concatenation & repetition
"""

# 1. Basic Tuple (Immutable)
t = (10, 20, 30)
print("Original tuple:", t)
print("First element:", t[0])

# 2. Tuple with duplicate values
t = (1, 2, 3, 2)
print("\nLength:", len(t))
print("Count of 2:", t.count(2))
print("Index of 3:", t.index(3))

# 3. Slicing
print("\nSlicing (1 to 2):", t[1:3])

# 4. Iteration
print("\nIterating through tuple:")
for i in t:
    print(i)

# 5. Tuple Packing
packed = 1, 2, 3
print("\nPacked tuple:", packed)

# 6. Tuple Unpacking
a, b, c = packed
print("Unpacked values:", a, b, c)

# 7. Nested Tuple
nested = (1, (2, 3), (4, 5))
print("\nNested tuple:", nested)
print("Access nested value:", nested[1][0])

# 8. Membership Test
print("\nIs 2 in tuple?", 2 in t)
print("Is 5 not in tuple?", 5 not in t)

# 9. Concatenation
t1 = (1, 2)
t2 = (3, 4)
print("\nConcatenated tuple:", t1 + t2)

# 10. Repetition
print("Repeated tuple:", t1 * 3)

# 11. Single Element Tuple
single = (5,)
print("\nSingle element tuple:", single)

# 12. Tuple Conversion
lst = [10, 20, 30]
converted = tuple(lst)
print("\nList to tuple:", converted)