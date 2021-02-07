num_char = len(input("What is your name?\n"))
# print("Your Name has " + num_char + " Characters.")  This Line gives Type Error because num_char is of integer Data Type.

print(type(num_char)) #This Line prints The type of num_char i.e. <class 'int'>

# type conversion
new_num_char = str(num_char)

# Now This line works flawlessly
print("Your Name has " + new_num_char + " Characters.")