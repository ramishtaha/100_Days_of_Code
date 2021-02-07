print("Welcome to the rollercoster!\n")
height = int(input("Please Enter Your Height in cm:\n"))
ticket_price = 0

if height > 120:
    print("You can Ride the RollerCoster\n")
    age = int(input("Please Enter Your age in Yrs:\n"))
    if age < 12:
        print("Child Tickets are $5.\n")
        ticket_price += 5
    elif age <= 18:
        print("Youth Tickets are $7.\n")
        ticket_price += 7
    else:
        print("Adult Tickets are $12.\n")
        ticket_price += 12

    wants_photo = input("Do you want Photos to be Taken? Y or N.\n")
    if wants_photo == "Y":
        ticket_price += 3
    
    if (age >= 45 and age <= 55):
        print("Sir, you are going through Midlife crisis your ticket will be on the house!!")
        ticket_price = 0
    else:
        print(f"Your Total Ticket Price is ${ticket_price}")

else:
    print("Sorry you have to grow Taller before you can ride.")