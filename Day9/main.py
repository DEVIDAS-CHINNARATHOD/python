# Lists and Tuples in Python

# List operations
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

fruits.append("mango")
fruits.insert(1, "orange")
print("After adding items:", fruits)

fruits.remove("banana")
popped_item = fruits.pop()
print("After removing items:", fruits)
print("Popped item:", popped_item)

fruits[1] = "grape"
print("After updating:", fruits)

print("First two fruits:", fruits[:2])
print("Reversed list:", fruits[::-1])

for fruit in fruits:
    print("Fruit:", fruit)

fruits.sort()
print("Sorted list:", fruits)

# Tuple operations
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

print("First element:", numbers[0])
print("Last two elements:", numbers[-2:])

count_20 = numbers.count(20)
index_30 = numbers.index(30)
print("Count of 20:", count_20)
print("Index of 30:", index_30)

for num in numbers:
    print("Number:", num)
