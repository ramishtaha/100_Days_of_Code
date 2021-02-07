print("Welcome to Trixter's Pizza!!")
size = input("What is the Size of Pizza you want? S, M or L\n")
add_pepperoni = input("Do you Wish to Add Pepperoni? Y or N\n")
extra_cheese = input("Do you wish to Add Extra Cheese? Y or N\n")
total_bill_amount = 0

if size == "S":
    total_bill_amount += 15
    if add_pepperoni == "Y":
        total_bill_amount += 2
elif size == "M":
    total_bill_amount += 20
    if add_pepperoni == "Y":
        total_bill_amount += 3
else:
    total_bill_amount += 25
    if add_pepperoni == "Y":
        total_bill_amount += 3

if extra_cheese == "Y":
    total_bill_amount += 1


print(f"Your total Bill Amount is ${total_bill_amount}")

