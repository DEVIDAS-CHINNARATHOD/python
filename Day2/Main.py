text = "   Hello World! Python is fun.   "

# 1. upper() - Convert to uppercase
print("upper():", text.upper())

# 2. lower() - Convert to lowercase
print("lower():", text.lower())

# 3. strip() - Remove leading/trailing whitespace
print("strip():", text.strip())

# 4. replace() - Replace substring
print("replace():", text.replace("Python", "Java"))

# 5. split() - Split string into list
print("split():", text.split())

# 6. find() - Find index of substring (-1 if not found)
print("find():", text.find("World"))

# 7. count() - Count occurrences of substring
print("count():", text.count("o"))

# 8. startswith() - Check if string starts with substring
print("startswith():", text.strip().startswith("Hello"))

# 9. endswith() - Check if string ends with substring
print("endswith():", text.strip().endswith("fun."))

# 10. capitalize() - Capitalize first character
print("capitalize():", text.strip().capitalize())
