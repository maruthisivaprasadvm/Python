# Don't change the code below
age = input("What is your age?\n")

# Write your code below this line

maxage = 90

age_in_int = int(age)

weeks = (maxage - age_in_int) * 52

days = (maxage - age_in_int) * 365

months = (maxage - age_in_int) * 12

print(f"you have {days} days, {weeks} weeks, and {months} months left.")