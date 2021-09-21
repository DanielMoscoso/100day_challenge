from Day_10 import art


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
        return "Wrong input."


# Output:
# Greetings:
# print(art.logo)
keep_result = "n"
for number in range(2):
    if keep_result == "n":
        first_number = int(input("What is the first number?: "))
        second_number = int(input("What is the second number?: "))
        print("+\n-\n*\n/\n%")
        sign = input("Pick and operation: ")
    elif keep_result == "y":
        first_number = result
        second_number = int(input("What is the second number?: "))
        print("+\n-\n*\n/\n%")
        sign = input("Pick and operation: ")
    else:
        pass

    result = calculator(first_number, second_number, sign)
    print(f"{first_number} {sign} {second_number} = {result}")
    keep_result = input(f"Type (Y)es to continue calculating with {result}. Or type (N)o to start a new calculation: ").lower()
