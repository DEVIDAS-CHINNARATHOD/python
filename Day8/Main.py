def add(a, b):
    return a + b

def greet(name):
    print("Hello", name)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

def is_even(num):
    return num % 2 == 0

x = add(5, 10)
print("Addition:", x)

greet("Devidas")

num = 5
print("Factorial of", num, "is", factorial(num))

print("2 raised to 4 is", power(2, 4))

print("Is 8 even?", is_even(8))
