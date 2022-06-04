# if / elif/ else


# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# Multiple if

# if condition1:
#     do A
# if condition2
#     do B
# if condition3
#     do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster! and please purchase the ticket as per your age")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("YChld tickets are $5")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12")
    # else:
    #     print(f"As you are {age} years old, need to pay $7 to purchase the ticket")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3

    print(f"Your final bill is {bill}$")

        
else:
    print("Sorry, you have to grow taller before you can ride.")