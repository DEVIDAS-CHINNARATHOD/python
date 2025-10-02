# Day 3: Working with Lists in Python

print("==== Creating Lists ====")
fruits = ["apple", "banana", "cherry"]
numbers = [5, 2, 9, 1]
mixed = [1, "hello", True, 3.14]
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

print("\n==== Accessing Elements ====")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice of fruits:", fruits[1:3])

print("\n==== Modifying Elements ====")
fruits[1] = "orange"
print("After modification:", fruits)

print("\n==== Adding Elements ====")
fruits.append("mango")
print("After append:", fruits)
fruits.insert(1, "kiwi")
print("After insert:", fruits)
fruits.extend(["grape", "pineapple"])
print("After extend:", fruits)

print("\n==== Removing Elements ====")
fruits.remove("kiwi")
print("After remove:", fruits)
popped_item = fruits.pop()
print("After pop:", fruits, "| Popped item:", popped_item)
del fruits[1]
print("After del index 1:", fruits)
fruits.clear()
print("After clear:", fruits)

print("\n==== List Operations ====")
a = [1, 2, 3]
b = [4, 5, 6]
print("Concatenation:", a + b)
print("Repetition:", a * 2)
print("Is 2 in a?", 2 in a)

print("\n==== List Functions ====")
numbers = [5, 2, 9, 1]
print("Original numbers:", numbers)
print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
numbers.sort()
print("After sort:", numbers)
numbers.reverse()
print("After reverse:", numbers)

print("\n==== Looping Through a List ====")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
