"""File handling in Python refers to the process of creating
, opening, reading, writing, and closing files."""
file = open("day49.txt", "r")
content = file.read()
print(content)
file.close()
