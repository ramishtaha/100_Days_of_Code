# from os import system, name
import os

bids = {}

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

def add_bidder(name, bid):
    bids[name] = bid

def max_bid(bids):
    max_bid = 0
    max_bidder = ""
    for bidder in bids:
        if bids[bidder] > max_bid:
            max = bids[bidder]
            max_bidder = bidder
    print(f"The winner is {max_bidder} with a bid of ${max}")


print("Welcome to Secret Auction")
from art import logo
print(logo)
choice = "yes"
while choice == "yes":
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    add_bidder(name, price)
    choice = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if choice == "yes":
        clear()

max_bid(bids)
