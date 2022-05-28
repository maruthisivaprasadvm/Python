
# Data Types
# numbers
# Operations
# Type Conversion
# f-StringS


# Data Types
# string, int, float, boolean

from decimal import DivisionByZero
from signal import pthread_sigmask
from winreg import ExpandEnvironmentStrings


print("Hello")

print("Hello"[0])
print("Hello"[4])

print("123")

print("123"+"456")

# Integer

print(123)
print(123+456)
123_456_789

# float

print(3.14159)
print(type(3.141569))

# Boolean

True
False

# Quiz

mystery = 734_529.678
print(mystery)

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

num_char = len(input("What is your name?"))
print("Your name has "+ num_char + " characters.")

num_char = len(input("What is your name?"))
print("Your name has "+ str(num_char) + " characters.")

type(num_char)

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print(new_num_char)
print("Your name has "+ new_num_char + " characters.")

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

print( 70 + 100.50 )

# Operators

#  print(3 + 5)
#  print(7 - 4)
#  print(3 * 2)
#  print(6 / 3)
#  type(print(6 / 3))
#  print( 2 ** 3)

 #Priority of Operators calculations

# PEMDAS

#  Parentheses  ()
#  Exponents    **
#  Multiplication * /
#  Division 
#  Addition      + - 
#  Subtraction

print( 3 * 3 + 3 / 3 - 3)
# 7.0

print( 3 * (3 + 3) / 3 - 3)
#3.0

print(int(8/3))
print(round(8/3))
print(round(8/3,2))

print(8//3)
print(type(8//3))
print(type(8//2))
print(type(8/2))
result = 4 /2
print(result)


score = 0

# User scores a point

score = score + 1

print(score)

# Rewrite the above code as below

score = 1

# User scores a point

score +=  1

print(score)

#f-String -- used to display combining different data types variables as a single string

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, your winning is {isWinning}")
