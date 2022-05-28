# clearscreen cls
# Ctrl + l - shortcut for clearscreen

# Shift + ENter to run the block of code in VSCODE



print(len("95637+12"))

score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")


def a_function(a_parameter):    
    a_variable = 15    
    return a_parameter 
    a_function(10)
    print(a_variable)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

print('Hello Python - I am coming')

print("Hello Python - I am coming !!!")

from socket import SIO_RCVALL


print("Hello " + input("What is your name?"))

# Write your code below this line
input("What is your name?")
print(len(input("What is your name?")))

name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("What is your name")
length = len(name)
print(length)


# Dont' change the code below
# change variables the values a and b

a = input("a:")
b = input("b:")

# write your code below this line
c = a
a = b
b = c

print(a)
print(b)

# 1.5 Variables naming convention

# Quiz

time_until_midnight = "5"
print("There are "+ time_until_midnight + " hours till midnight")
