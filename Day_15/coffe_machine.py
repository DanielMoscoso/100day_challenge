import os
import info

# TODO: 1.Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 2.Turn off the Coffee Machine by entering "off" to the prompt.
# TODO: 3.Print report.
# TODO: 4.Check resources sufficient? When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO: 5.Process coins.
# TODO: 6.Check: transaction successful?
#       TODO: 6.1Check that the user has inserted enough money to purchase the drink they selected.
#       TODO: 6.2 If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered.
#       TODO: 6.3 If the user has inserted too much money, the machine should offer change. (The change should be rounded to 2 decimal places).
# TODO: 7. Make Coffee: the ingredients to make the drink should be deducted from the coffee machine resources.
# TODO: 8. Once all resources have been deducted, tell the user “Here is your {drink}. Enjoy!”.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

answer = input("What would you like to do? (M)ake coffee, or print the (R)eport: ").lower()

# Make cofee
if answer == "m":
    answer = input("What would you like? (expresso: $1.5 / latte: $2.5 / cappuccino: 3.0): ").lower()
    # Make expresso
    if answer == "expresso":
        # If the machine has enough water:
        if resources["water"] >= info.MENU["espresso"]["ingredients"]["water"]:
            print("Please insert coins: ")
            quarters = int(input("How many quarters?: ")) / 4
            dimes = int(input("How many dimes?: ")) / 10
            nickles = int(input("How many nickles?: ")) / 20
            pennies = int(input("How many pennies?: ")) / 100
            total = quarters + dimes + nickles + pennies
            if total > info.MENU["espresso"]["cost"]:
                change = total - info.MENU["espresso"]["cost"]
                print(f"Here is ${change} in change.")
                print("Here is your expresso. Enjoy!")
            elif total < info.MENU["espresso"]["cost"]:
                print("Sorry, that is not enough money. Money refunded.")
            else:
                print("Here is your expresso. Enjoy!")
elif answer == "r":
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])
elif answer == "o":
    print("Turning off!")
else:
    print("Wrong input. Bye!")
