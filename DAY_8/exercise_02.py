#Write your code below this line 👇

def prime_checker(number):
    for i in range (2, number):
        if number % i == 0:
            return print(f"Number {number} is not a Prime.")
    return print(f"Number {number} is a Prime.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



