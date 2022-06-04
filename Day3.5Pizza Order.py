# Multiple if

# if condition1:
#     do A
# if condition2
#     do B
# if condition3
#     do C


print("Welcome to Python Pizza Deliverables!")
size = input("What size pizza do you want? S, M or L size: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese  = input("Do you want extra cheese? Y or N: ")


if size == "S":
    small_pizza = 15    
if size == "M":
    medium_pizza = 20
if size == "L":
    large_pizza = 25
        
    
if add_pepperoni == "Y" and size == "S":
    bill = small_pizza + 2
if add_pepperoni == "Y" and size == "M":
    bill = medium_pizza + 3
if add_pepperoni == "Y" and size == "L":
    bill = large_pizza + 3

if add_pepperoni == "N" and size == "S":
    bill = small_pizza 
if add_pepperoni == "N" and size == "M":
    bill = medium_pizza 
if add_pepperoni == "N" and size == "L":
    bill = large_pizza


    
if extra_cheese == "N":
    final_bill = bill
    print(f"Your final bill is : {final_bill}$")
if  extra_cheese == "Y":
    final_bill = bill + 1
    print(f"Your final bill is : {final_bill}$")

        

    # print(f"Please reorder with proper pizza details")