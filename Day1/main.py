print("Basics of Python")

# Simple arithmetic operations
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")  

name = "Alice"
age = 30
# Demonstrating type checking
print(type(name)) 
print(type(age))
print(f"{name} is {age} years old.")

#type conversion
age_str = str(age)
print(f"Age as string: {age_str}, Type: {type(age_str)}")

# Control structures
if age < 18:
    print(f"{name} is a minor.")
elif age < 65:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a senior.")   

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")   
# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
