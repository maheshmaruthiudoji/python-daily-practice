"""
Python Dictionary Operations - Complete Guide

This script demonstrates:
- Creating dictionary
- Adding & updating values
- Accessing elements
- Built-in methods
- Looping
- Nested dictionary
- Dictionary comprehension
- Copying & clearing
"""

# 1. Create dictionary
marks = {
    "maths": 99,
    "science": 94,
    "chemistry": 98
}
print("Original dictionary:", marks)

# 2. Type
print("Type:", type(marks))

# 3. Access values
print("\nMaths marks:", marks["maths"])
print("Physics (safe):", marks.get("physics"))

# 4. Add / Update
marks["maths"] = 100
marks["english"] = 92
print("\nAfter update:", marks)

# 5. Keys, Values, Items
print("\nKeys:", marks.keys())
print("Values:", marks.values())
print("Items:", marks.items())

# 6. Remove elements
marks.pop("science")   # remove specific
print("\nAfter pop:", marks)

marks.popitem()        # remove last item
print("After popitem:", marks)

# 7. Looping
print("\nLooping through dictionary:")
for key, value in marks.items():
    print(key, ":", value)

# 8. Nested dictionary
students = {
    "student1": {"name": "Mahesh", "marks": 95},
    "student2": {"name": "Rahul", "marks": 88}
}
print("\nNested dictionary:", students)
print("Student1 name:", students["student1"]["name"])

# 9. Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print("\nDictionary comprehension (squares):", squares)

# 10. Copy dictionary
marks_copy = marks.copy()
print("\nCopied dictionary:", marks_copy)

# 11. Clear dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("Cleared dictionary:", temp)

# 12. Update multiple values
marks.update({"physics": 85, "biology": 90})
print("\nAfter update():", marks)

# 13. Check key existence
print("\nIs 'maths' present?", "maths" in marks)

# 14. Length
print("Length:", len(marks))

# 15. Default value using setdefault
marks.setdefault("history", 80)
print("\nAfter setdefault:", marks)



