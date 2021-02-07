print("Welcome to Leap Year Checker!!")
year = int(input("Please, Enter the Year:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The Year {year} is a leap year.")
        else:
            print(f"The Year {year} is not a leap year.")
    else:
        print(f"The Year {year} is a leap year.")
else:
    print(f"The Year {year} is not a leap year.")