"""
Python Set Operations - Complete Guide
-------------------------------------
This script demonstrates:
- Creating sets
- Uniqueness (no duplicates)
- Adding & removing elements
- Set operations (union, intersection, difference)
- Membership testing
- Set methods
"""

# 1. Creating a set (duplicates removed automatically)
languages = {"Python", "Java", "C++", "Python"}
print("Unique languages:", languages)

# 2. Type
print("Type:", type(languages))

# 3. Adding elements
languages.add("JavaScript")
print("\nAfter adding:", languages)

# 4. Removing elements
languages.remove("Java")   # error if not found
print("After remove:", languages)

languages.discard("Ruby")  # no error if not found
print("After discard (no error):", languages)

# 5. Pop element (random removal)
removed = languages.pop()
print("Popped element:", removed)
print("After pop:", languages)

# 6. Length
print("\nLength:", len(languages))

# 7. Membership test
print("Is 'Python' in set?", "Python" in languages)

# 8. Another set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 9. Union (all elements)
print("\nUnion:", set1 | set2)

# 10. Intersection (common elements)
print("Intersection:", set1 & set2)

# 11. Difference
print("Difference (set1 - set2):", set1 - set2)

# 12. Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)

# 13. Set methods
print("\nUnion method:", set1.union(set2))
print("Intersection method:", set1.intersection(set2))

# 14. Subset & Superset
a = {1, 2}
b = {1, 2, 3, 4}
print("\nIs a subset of b?", a.issubset(b))
print("Is b superset of a?", b.issuperset(a))

# 15. Copy & Clear
copy_set = set1.copy()
print("\nCopied set:", copy_set)

temp = {10, 20}
temp.clear()
print("Cleared set:", temp)

# 16. Frozen set (immutable set)
frozen = frozenset([1, 2, 3])
print("\nFrozen set:", frozen)