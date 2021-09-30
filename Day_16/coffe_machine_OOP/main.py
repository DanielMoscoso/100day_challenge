from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# # - You might need to use this if the IDE is currently running on a different directory -
# import os
# os.getcwd()
# os.chdir("C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_16\\coffe_machine_OOP")
# # - You might need to use this if the IDE is currently running on a different directory -

coffees = Menu()

coffees.get_items()


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
            print("Turning off!")
            repeat = False  # Get out to the main menu.
        else:
            print("Wrong input. Bye!")
            repeat = False  # Get out to the main menu.

    while input("Hello! type (A)gain to go to main menu, or (E)xit: ").lower() == "a":
        play()
        return


play()
