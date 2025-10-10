# File handling examples: write, read, append, and check

file_name = "sample.txt"

# Write to file
with open(file_name, "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("Python file handling is easy.\n")

# Read from file
with open(file_name, "r") as f:
    content = f.read()
    print("File content:\n", content)

# Append to file
with open(file_name, "a") as f:
    f.write("This line was appended.\n")

# Read lines one by one
with open(file_name, "r") as f:
    for line in f:
        print("Line:", line.strip())

# Check if file exists
import os
if os.path.exists(file_name):
    print("File exists:", file_name)
else:
    print("File not found.")
