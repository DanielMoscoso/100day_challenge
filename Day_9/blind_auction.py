import getpass
from Day_9 import art
import os

# InitializationÑ
auction = {"name": [], "bid": []}


# Functions:
# Define our clear function (for when we want to clear the screen after each try):
def clear():
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def blind_auction(person="", bid=0):
    auction["name"].append(person)
    auction["bid"].append(bid)


# Logic:
add_people = True
while add_people:
    name = input("What is your name?: ")
    bid = int(getpass.getpass('What is your bid?: $'))  # This will show dots instead of characters when typing.
    more_people = input('"Are there any more bidders? Type "Yes" or "No": \n').lower()

    blind_auction(name, bid)

    if more_people == "no":
        add_people = False
    elif more_people == "yes":
        clear()

# Output:
print(art.logo)

highest_value = max(auction["bid"])
highest_value_index = auction["bid"].index(highest_value)
winner = auction["name"][highest_value_index]

print(f"The winner is {winner} with a bid of $ {highest_value}.")
# %%
from Day_9 import art
import os


# Functions:
# Define our clear function (for when we want to clear the screen after each try):
def clear():
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# Output:
print(art.logo)

bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    should_continue = input('"Are there any more bidders? Type "Yes" or "No": \n').lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
