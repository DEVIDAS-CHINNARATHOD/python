#Fun with input and output 
#Day 1
boy_name = input("Enter Boy's name: ")
boy_age = int(input(f"Enter {boy_name}'s age: "))

girl_name = input("Enter Girl's name: ")
girl_age = int(input(f"Enter {girl_name}'s age: "))

print(f"{boy_name} loves {girl_name}")
print("The age difference is", abs(boy_age -girl_age))

if girl_age >=18 and boy_age >=21:
    print("They can marry")
else:
    print("They cannot marry")


