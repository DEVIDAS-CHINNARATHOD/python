# 1. Right-angled Triangle
print("Right-angled Triangle:")
for i in range(1, 6):
    print("* " * i)
print("\n")

# 2. Inverted Triangle
print("Inverted Triangle:")
for i in range(5, 0, -1):
    print("* " * i)
print("\n")

# 3. Pyramid Pattern
print("Pyramid Pattern:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
print("\n")

# 4. Hollow Square
print("Hollow Square:")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

# 5. Diamond Pattern
print("Diamond Pattern:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * (2*i - 1))
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * (2*i - 1))
