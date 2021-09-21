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


print(add(1, 1))
print(calculator(1, 1, "+"))
print(calculator(1, 1, "-"))
print(calculator(1, 1, "*"))
print(calculator(1, 1, "/"))
print(calculator(1, 1, "%"))
