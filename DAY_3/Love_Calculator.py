print("Welcome to The Love Calculator!!!\n")
name1 = input("What is your name?\n").lower()
name2 = input("What is their's name?\n").lower()

# true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
# love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

# I did code the above lines but I think the lower ones are better
name = name1 + name2
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

true_love = int(str(true) + str(love))

if true_love < 10 or true_love > 90:
    print(f"Your Score is {true_love}, You go together like coke and mentos.")
elif true_love > 45 and true_love < 55:
    print(f"Your Score is {true_love}, You are Alright There")
else:
    print(f"Your Score is {true_love}")