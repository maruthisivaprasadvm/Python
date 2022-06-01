print("Welcome to the BMI 2.0 Calculator!")

height = float(input("What is your height in m? "))
weight = float(input("What is your weight in kg? "))


# height1 = float(height)
# weight1 = int(weight)

# write your code here

#calculation1
#BMI = ( weight1 / (height1 * height1))

#calculation2
bmi = round(( weight / (height ** 2)),2)

# bmi_as_float = float(bmi)
# bmi_as_int = int(bmi)

# print(bmi_as_float)
# print(bmi_as_int)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your bmi is {bmi}, You are normal weight.")
elif bmi > 25 and bmi < 30:
        print(f"Your bmi is {bmi}, You are overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}, You are obese.")
else: 
    print(f"Your bmi is {bmi}, You are clinically obese")