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
    clear()
    name = input("What is your name?: ")
    bid = int(getpass.getpass('What is your bid?:'))  # This will show dots instead of characters when typing.
    more_people = input('"Are there any more bidders? Type "Yes" or "No": ').lower()

    blind_auction(name, bid)

    if more_people == "no":
        add_people = False

# Output:
print(art.logo)

highest_value = max(auction["bid"])
highest_value_index = auction["bid"].index(highest_value)
winner = auction["name"][highest_value_index]

print(f"The winner is {winner} with {highest_value}")
