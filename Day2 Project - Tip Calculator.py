#Welcome to the tip calculator
#Each person should pay (150.00 / 5 ) * 1.12

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $ "))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split_bill = int(input("How many people to split the bill? "))

calculate_tip_percentage = ( tip_percentage / 100 )
#print(calculate_tip_percentage)

total_bill_of_percentage =  ( total_bill * calculate_tip_percentage )
#print(total_bill_of_percentage)

final_total_bill = ( total_bill + total_bill_of_percentage )
#print(final_total_bill)

each_person_pay = final_total_bill / split_bill
bill_per_person = "{:.2f}".format(each_person_pay)

#print(f"Each person should pay: $ {each_person_pay}")
print(f"Each person should pay: $ {bill_per_person}")