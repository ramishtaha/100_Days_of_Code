print("Welcome to the Life in Weeks Calculator")
age = int(input("Please Enter Your Current Age:\n"))
yrs_remaining = 90 - age
days = yrs_remaining * 365
weeks = yrs_remaining * 52
months = yrs_remaining * 12

print(f"You have {days} days, {weeks} weeks, {months} months and {yrs_remaining} Years left.")