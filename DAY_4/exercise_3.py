import random
name_list = input("Names Seperated by comma. \n").split(", ")

print(f"{name_list[random.randint(0, len(name_list) - 1)]}")