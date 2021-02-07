print("Welcome To The Tip Calculator")
bill_amt = int(input("Please Enter the Bill amount\n$"))
tip_percent = int(input("Please Enter the Percentage of Tip you Wanna give? (Example 10, 12 or 14):\n"))
tip =(bill_amt * tip_percent/100)
peoples = int(input("Please Enter the number of Friends you wanna Split bill with:\n"))
person_share = (bill_amt + tip) / peoples
print(f"Each of you should pay ${person_share}")
