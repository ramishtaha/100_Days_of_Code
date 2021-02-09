import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = ''
attempts = 0


while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == 'easy':
        attempts = 10
        break
    if difficulty == 'hard':
        attempts = 5
        break


while attempts > 0:
    print(f"You have {attempts} attempts remaining.")

    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        print("Guess again.")
    elif guess < number:
        print("Too low.")
        print("Guess again.")
    else:
        print(f"You got it! the answer was {number}")

