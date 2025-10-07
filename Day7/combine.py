print("Welcome to the Number Pattern Game!")

while True:
    print("\nChoose a pattern to print:")
    print("1. Right Triangle")
    print("2. Inverted Triangle")
    print("3. Pyramid")
    print("4. Hollow Square")
    
    choice = int(input("Enter your choice (1-4): "))
    n = int(input("Enter number of rows: "))
    
    if choice == 1:
        print("Right Triangle:")
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end=" ")
            print()
            
    elif choice == 2:
        print("Inverted Triangle:")
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print()
            
    elif choice == 3:
        print("Pyramid:")
        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            print("* " * i)
            
    elif choice == 4:
        print("Hollow Square:")
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    else:
        print("Invalid choice!")

    cont = input("Do you want to print another pattern? (y/n): ").lower()
    if cont != "y":
        print("Thanks for playing! Goodbye.")
        break
