"""
Python File Handling - Complete Guide
------------------------------------
This script demonstrates:
- Opening files (read, write, append)
- Reading file content
- Writing & appending data
- File modes
- Using with statement (best practice)
- File pointer methods
- Working with text & lines
"""

# 1. Writing to a file (creates file if not exists)
file = open("sample.txt", "w")
file.write("Hello, this is Python file handling.\n")
file.write("Learning file operations.\n")
file.close()

# 2. Reading entire file
file = open("sample.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()

# 3. Reading line by line
file = open("sample.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())
file.close()

# 4. Append mode (add content without deleting old data)
file = open("sample.txt", "a")
file.write("This line is added later.\n")
file.close()

# 5. Using 'with' (best practice - auto close)
with open("sample.txt", "r") as file:
    print("\nUsing with statement:")
    print(file.read())

# 6. Read specific number of characters
with open("sample.txt", "r") as file:
    print("\nFirst 10 characters:", file.read(10))

# 7. File pointer methods
with open("sample.txt", "r") as file:
    print("\nPointer position:", file.tell())
    file.read(5)
    print("After reading 5 chars, position:", file.tell())
    file.seek(0)
    print("After seek(0), position:", file.tell())

# 8. Reading lines into list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("\nLines as list:", lines)

# 9. Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multi.txt", "w") as file:
    file.writelines(lines)

print("\nMultiple lines written to multi.txt")

# 10. File modes explanation
"""
'r'  -> Read (error if file not exists)
'w'  -> Write (overwrite file)
'a'  -> Append (add to file)
'x'  -> Create (error if file exists)
'r+' -> Read + Write
"""

# 11. Check file existence (safe handling)
import os

if os.path.exists("sample.txt"):
    print("\nFile exists")
else:
    print("\nFile does not exist")

# 12. Exception handling (important)
try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nError: File not found")