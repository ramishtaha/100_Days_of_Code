from art import logo, vs
from game_data import data
from os import system
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



a = random.choice(data)
b = random.choice(data)

def print_choice(c):
    print(f"Compare A: {c['name']},  {c['description']}, from {c['country']}.")

score = 0
cls()
print(logo)
while True:
    print_choice(a)
    print(vs)
    print_choice(b)

    choice = input("Who has more followers? Type 'A' or 'B': ")
    # print(a['follower_count'], b['follower_count'])
    if choice == 'A':
        if not a['follower_count'] > b['follower_count']:
            break
    if choice == "B":
        if not b['follower_count'] > a['follower_count']:
            break
    score += 1
    cls()
    print(logo)
    print(f"You are Right, Current score is: {score}")
    a = b
    b = random.choice(data)

print(f"Sorry, That's wrong. Final Score{score}")