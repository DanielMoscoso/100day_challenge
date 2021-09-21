from Day_10 import art
import os


def add(first=0, second=0):
    return first + second


def substract(first=0, second=0):
    return first - second


def multiply(first=0, second=0):
    return first * second


def divide(first=0, second=0):
    return first / second


def modulo(first=0, second=0):
    return first % second


def calculator(first=0, second=0, type=""):
    if type == "+":
        result = add(first, second)
        return result
    elif type == "-":
        result = substract(first, second)
        return result
    elif type == "*":
        result = multiply(first, second)
        return result
    elif type == "/":
        result = divide(first, second)
        return result
    elif type == "%":
        result = modulo(first, second)
        return result
    else:
        return "Wrong input"


# Define our clear function (for when we want to clear the screen after each try):
def clear():
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


# Output:
# Greetings:
print(art.logo)
keep_result = "n"
again = True
while again:
    if keep_result == "n":
        clear()
        first_number = int(input("What is the first number?: "))
        second_number = int(input("What is the second number?: "))
        print("+\n-\n*\n/\n%")
        sign = input("Pick an operation: ")
    elif keep_result == "y":
        first_number = result
        second_number = int(input("What is the second number?: "))
        print("+\n-\n*\n/\n%")
        sign = input("Pick an operation: ")
    else:
        pass

    result = calculator(first_number, second_number, sign)
    if result == "Wrong input":  # If the user inputs the wrong special character, then the calculator closes.
        print(result)
        break

    print(f"{first_number} {sign} {second_number} = {result}")
    keep_result = input(f"Type (Y)es to continue calculating with {result}. Type (N)o to start a new calculation, or (E)xit to end the program:  ").lower()

    if keep_result == "e":
        again = False

# %%
from Day_10 import art
import os


def add(first=0, second=0):
    return first + second


def substract(first=0, second=0):
    return first - second


def multiply(first=0, second=0):
    return first * second


def divide(first=0, second=0):
    return first / second


def modulo(first=0, second=0):
    return first % second


# Define our clear function (for when we want to clear the screen after each try):
def clear():
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


# Output:
# Greetings:
print(art.logo)

clear()
operation_dictionary = {"+": add,
                        "-": substract,
                        "*": multiply,
                        "/": divide,
                        "%": modulo}

first_number = int(input("What is the first number?: "))

for key in operation_dictionary:
    print(key)

should_continue = True
while should_continue:
    symbol = input("Pick an operation: ")
    second_number = int(input("What is the second number?: "))

    operation = operation_dictionary[symbol]
    result = operation(first_number, second_number)

    print(f"{first_number} {symbol} {second_number} = {result}")

    if input(f"Type (Y)es to continue calculating with {result}. Type (N)o to exit:  ").lower() == "y":
        first_number = result
    else:
        should_continue = False
