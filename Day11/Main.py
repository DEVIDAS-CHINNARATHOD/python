try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print("Division result:", result)
finally:
    print("Execution completed.")

x = -5
if x < 0:
    raise Exception("Negative value not allowed.")