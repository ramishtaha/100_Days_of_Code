print("Welcome to the rollercoster!\n")
height = int(input("Please Enter Your Height in cm:\n"))

if height > 120:
    print("You can Ride the RollerCoster\n")
    age = int(input("Please Enter Your age in Yrs:\n"))
    if age < 12:
        print("Please Pay $5.\n")
    elif age <= 18:
        print("Please Pay $7.\n")
    else:
        print("Please Pay $12.\n")
else:
    print("Sorry you have to grow Taller before you can ride.")