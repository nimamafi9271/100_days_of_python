# Day 9 project
# This is the code for Blind Auction
from art import logo
from functions import find_highest_bidder

print(logo)
terminate = False
bids = {}
while not terminate:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there anymore bidders? Type 'yes' or 'no'").lower()
    if should_continue == 'yes':
        print("\n"*100)
    elif should_continue == 'no':
        terminate = True
        find_highest_bidder(bids)