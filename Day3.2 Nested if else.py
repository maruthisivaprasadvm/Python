# Nested if/else Syntax

# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# if / elif / else
from re import A


# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster! and please purchase the ticket as per your age")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5 for the ticket")
    elif age >= 12 and age <= 18:
        print("You have to pay $7 for the ticket")
    elif age > 18:
        print("You have to pay $12 for the ticket")
    # else:
    #     print(f"As you are {age} years old, need to pay $7 to purchase the ticket")
        
else:
    print("Sorry, you have to grow taller before you can ride.")