import info
import art

# TODO: 1.Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 2.Turn off the Coffee Machine by entering "off" to the prompt.
# TODO: 3.Print report.
# TODO: 4.Check resources sufficient? When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO: 5.Process coins.
# TODO: 6.Check: transaction successful?
#       TODO: 6.1 Check that the user has inserted enough money to purchase the drink they selected.
#       TODO: 6.2 If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered.
#       TODO: 6.3 If the user has inserted too much money, the machine should offer change. (The change should be rounded to 2 decimal places).
# TODO: 7. Make Coffee: the ingredients to make the drink should be deducted from the coffee machine resources.
# TODO: 8. Once all resources have been deducted, tell the user “Here is your {drink}. Enjoy!”.


def calculations():
    """
    Here is where the total ammount of money the user inserted in the machine is calculated.
    """
    quarters = int(input("How many quarters?: ")) / 4
    dimes = int(input("How many dimes?: ")) / 10
    nickles = int(input("How many nickles?: ")) / 20
    pennies = int(input("How many pennies?: ")) / 100

    total = quarters + dimes + nickles + pennies
    return total


def espresso(resources):
    """
    Here is where the espresso coffee is made: It checks if the user inserted
    enough money to pay for the coffee. If they did, then the coffee is made,
    and if there is any change, it returns it to the user along with the coffee.
    """
    print("Please insert coins: ")
    total = calculations()
    if total > info.MENU["espresso"]["cost"]:
        change = total - info.MENU["espresso"]["cost"]
        print(f"Here is ${round(change, 2)} in change.")  # This will roung the answer up to 2 decimal places.
        print("Here is your espresso. Enjoy!")
    elif total < info.MENU["espresso"]["cost"]:
        print("Sorry, that is not enough money. Money refunded.")
        return 0  # No charge: return money.
    else:
        print("Here is your espresso. Enjoy!")

    return resources["money"] + info.MENU["espresso"]["cost"]


def latte(resources):
    """
    Here is where the latte coffee is made: It checks if the user inserted
    enough money to pay for the coffee. If they did, then the coffee is made,
    and if there is any change, it returns it to the user along with the coffee.
    """
    print("Please insert coins: ")
    total = calculations()
    if total > info.MENU["latte"]["cost"]:
        change = total - info.MENU["latte"]["cost"]
        print(f"Here is ${round(change, 2)} in change.")  # This will roung the answer up to 2 decimal places.
        print("Here is your latte. Enjoy!")
    elif total < info.MENU["latte"]["cost"]:
        print("Sorry, that is not enough money. Money refunded.")
        return 0  # No charge: return money.
    else:
        print("Here is your latte. Enjoy!")

    return resources["money"] + info.MENU["latte"]["cost"]


def cappuccino(resources):
    """
    Here is where the cappuccino coffee is made: It checks if the user inserted
    enough money to pay for the coffee. If they did, then the coffee is made,
    and if there is any change, it returns it to the user along with the coffee.
    """
    print("Please insert coins: ")
    total = calculations()
    if total > info.MENU["cappuccino"]["cost"]:
        change = total - info.MENU["cappuccino"]["cost"]
        print(f"Here is ${round(change, 2)} in change.")  # This will roung the answer up to 2 decimal places.
        print("Here is your cappuccino. Enjoy!")
    elif total < info.MENU["cappuccino"]["cost"]:
        print("Sorry, that is not enough money. Money refunded.")
        return 0  # No charge: return money.
    else:
        print("Here is your cappuccino. Enjoy!")

    return resources["money"] + info.MENU["cappuccino"]["cost"]


def brew_profit(answer, resources):
    """
    Here is where the profit from the coffe that is being made is calculated,
    an returned.
    """
    if answer == "espresso":
        profit = espresso(resources)
    elif answer == "latte":
        profit = latte(resources)
    elif answer == "cappuccino":
        profit = cappuccino(resources)
    else:
        pass

    return profit


def brew(resources, answer):
    """
    Here is where the all the previous conditions for brewing the coffee are checked:
    if there are enough ingredients in their individual reservoirs. It creates a
    truth table, and if there is any ingredient reservoir empty, then it adds a '0'
    to it. At the end, if there are no reservoirs empty, then the function returns True,
    allowing the machine to brew the coffee. Otherwise it would tell the user what ingredients
    are missing.
    """
    table = {}  # Truth table.
    for item in resources:
        if item == "money":  # If the item is money, then do not check it.
            pass
        elif resources[item] >= info.MENU[answer]["ingredients"][item]:
            table[item] = 1
        else:
            table[item] = 0

    # If there is a item in the list with not enough ingredients, look for it and print it.
    if 0 in table.values():
        for item, measure in table.items():
            if measure == 0:
                print(f"Sorry there is not enough {item}.")

        return False
    else:
        return True


def ingredients(materials):
    """
    This function takes all the ingredients from the resouces dictionary, and prints
    them out to the user.
    """
    print(f"\nWater: {materials['water']}ml")
    print(f"Milk: {materials['milk']}ml")
    print(f"Coffee: {materials['coffee']}gr")
    print(f"Money: ${materials['money']}\n")


def play():
    """
    This is where all the fun begins: here is where the brewing machine is housed.
    The machine will ask the user what coffee they want. Then checks if there are
    enough ingredients to brew that coffe. If there are, then asks the user for the
    money and tells them if they inserted enough money. If they did not, then the machine
    tells the user, and returns the money. If the coffee can be properly made, it will be
    given to the user, with their change, if any.
    The user can also see the report of all the ingredients, and there is a hidden answer; 'o'
    for 'off', in case the user needs to turn the machine off for maintenance.
    """
    print(art.logo)
    print(art.letters)
    print("Welcome to your favorite vending machine!!")
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }

    repeat = True
    while repeat:
        answer = input("\nWhat would you like to do? (M)ake coffee, or print the (R)eport: ").lower()

        # Make cofee
        if answer == "m":
            answer = input("\nWhat would you like? (espresso: $1.5 / latte: $2.5 / cappuccino: 3.0): ").lower()
            if brew(resources, answer):  # Brewing is independent of money inserted!! It is dependent of the ingredients.
                resources["money"] = brew_profit(answer, resources)  # Here is where you check if the person inserted the right amount of money.
                if resources["money"] == 0:  # If the machine did not charge, then do not make any coffe.
                    repeat = False  # Get out to the main menu.
                else:
                    resources["water"] -= info.MENU[answer]["ingredients"]["water"]
                    resources["milk"] -= info.MENU[answer]["ingredients"]["milk"]
                    resources["coffee"] -= info.MENU[answer]["ingredients"]["coffee"]
            else:  # If there are not enough ingredients to make a coffee:
                repeat = False  # Get out to the main menu.
        # Get the report:
        elif answer == "r":
            ingredients(resources)
        # Hidden answer: for turning the machine off.
        elif answer == "off":
            print("\nTurning off!")
            repeat = False  # Get out to the main menu.
            return
        else:
            print("\nWrong input. Bye!")
            repeat = False  # Get out to the main menu.
            return

    while input("Hello! type (A)gain to go to main menu, or (E)xit: ").lower() == "a":
        play()
        return


play()
