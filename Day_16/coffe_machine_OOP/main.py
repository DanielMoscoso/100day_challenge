from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art
import os
# # - You might need to use this if the IDE is currently running on a different directory -
# import os
# os.getcwd()
# os.chdir("C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_16\\coffe_machine_OOP")
# # - You might need to use this if the IDE is currently running on a different directory -

coffees = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()


def clear():
    """
    This function is used for clearing the entire screen.
    If you IDE does not support it, then you might want to see it
    in action when running on command line.
    """
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def artwork():
    print(art.logo)
    print(art.letters)
    print("Welcome to your favorite vending machine!!")


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

    artwork()

    repeat = True
    while repeat:
        answer = input("\nWhat would you like to do? (M)ake coffee, or print the (R)eport: ").lower()

        # Make cofee
        if answer == "m":
            drink = input("\nWhat would you like? (espresso: $1.5 / latte: $2.5 / cappuccino: 3.0): ").lower()
            drink_class = coffees.find_drink(drink)
            drink_class.ingredients
            if machine.is_resource_sufficient(drink_class):  # Brewing is independent of money inserted!! It is dependent of the ingredients.
                money_machine.make_payment(drink_class.cost)
                machine.make_coffee(drink_class)
            else:  # If there are not enough ingredients to make a coffee:
                repeat = False  # Get out to the main menu.
        # Get the report:
        elif answer == "r":
            clear()
            artwork()
            machine.report()
            money_machine.report()
        # Hidden answer: for turning the machine off.
        elif answer == "off":
            clear()
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
