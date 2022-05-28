# Don't change the code below

height = input("enter your height in m:  ")
weight = input("enter your weight in kg: ")

# print(weight)
# print(height)
# print(type(weight))
# print(type(height))

height1 = float(height)
weight1 = int(weight)

# write your code here

#calculation1
#BMI = ( weight1 / (height1 * height1))

#calculation2
BMI = ( weight1 / (height1 ** 2))

bmi_as_float = float(BMI)
bmi_as_int = int(BMI)

print(bmi_as_float)
print(bmi_as_int)