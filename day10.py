"""
Python Loop Operations - Complete Guide

This script demonstrates:
- for loop
- while loop
- break, continue, pass
- range()
- nested loops
- loop with else
- iteration over data structures
"""

# 1. for loop with list
numbers = [1, 2, 3, 4]
print("For loop (list):")
for num in numbers:
    print(num)

# 2. for loop with range()
print("\nRange loop:")
for i in range(5):  # 0 to 4
    print(i)

# 3. range with start, stop, step
print("\nRange with step:")
for i in range(1, 10, 2):
    print(i)

# 4. while loop
print("\nWhile loop:")
i = 1
while i <= 3:
    print(i)
    i += 1

# 5. break (stop loop)
print("\nBreak example:")
for i in range(5):
    if i == 3:
        break
    print(i)

# 6. continue (skip iteration)
print("\nContinue example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 7. pass (do nothing)
print("\nPass example:")
for i in range(3):
    if i == 1:
        pass
    print(i)

# 8. Nested loops
print("\nNested loops:")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# 9. Loop with else
print("\nLoop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished")

# 10. Iterating over string
print("\nLoop over string:")
for ch in "Python":
    print(ch)

# 11. Iterating over dictionary
print("\nLoop over dictionary:")
marks = {"maths": 90, "science": 85}
for key, value in marks.items():
    print(key, ":", value)

# 12. Enumerate (index + value)
print("\nEnumerate example:")
names = ["Mahesh", "Rahul", "Amit"]
for index, name in enumerate(names):
    print(index, name)

# 13. Zip (multiple lists together)
print("\nZip example:")
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for a, b in zip(list1, list2):
    print(a, b)

# 14. List comprehension (short loop)
print("\nList comprehension:")
squares = [x*x for x in range(5)]
print(squares)

# 15. Infinite loop (use carefully)
# while True:
#     print("Running forever...")
#     break   # prevent infinite run