# Python Operators - All in One Program

print("==== Arithmetic Operators ====")
a = 10
b = 3
print("a =", a, "b =", b)
print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponent: a ** b =", a ** b)

print("\n==== Comparison Operators ====")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n==== Logical Operators ====")
x = True
y = False
print("x =", x, "y =", y)
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n==== Assignment Operators ====")
c = 5
print("c =", c)
c += 2
print("c += 2:", c)
c -= 1
print("c -= 1:", c)
c *= 3
print("c *= 3:", c)
c /= 2
print("c /= 2:", c)
c //= 2
print("c //= 2:", c)
c %= 2
print("c %= 2:", c)
c **= 3
print("c **= 3:", c)

print("\n==== Bitwise Operators ====")
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print("p =", p, "q =", q)
print("p & q (AND):", p & q)
print("p | q (OR):", p | q)
print("p ^ q (XOR):", p ^ q)
print("~p (NOT):", ~p)
print("p << 1 (Left Shift):", p << 1)
print("p >> 1 (Right Shift):", p >> 1)

print("\n==== Identity Operators ====")
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("m =", m, "n =", n, "o =", o)
print("m is n:", m is n)
print("m is o:", m is o)
print("m is not o:", m is not o)

print("\n==== Membership Operators ====")
s = "hello world"
print("'h' in s:", 'h' in s)
print("'z' in s:", 'z' in s)
print("'z' not in s:", 'z' not in s)
