print("Welcome to The Digits sum Calculator!!")

num = input("Enter a Number:\n")
sum = 0
for i in num:
    sum += int(i)

print("The Sum of the Digits is:\n" + str(sum))