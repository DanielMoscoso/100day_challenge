# Simple function
def greet():
    print("1")
    print("2")
    print("3")


greet()


# %%
# Function that allows inputs:
def greet2(name):
    print(f"Hello {name}.")
    print(f"How do you do {name}?")


greet2("John")


# %%
# Function that allows more than one imput:
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")


greet_with("Pedro", "Italy")  # This is ussing a positional arguments.


# %%
# Function with keyword arguments:
def greet_with2(name="NONAME", location="NOWHERE"):  # This is using keyword arguments.
    print(f"Hello {name}.")
    print(f"What is it like in {location}?\n")


greet_with2()
greet_with2("Pedro", "Italy")
greet_with2(name="Pedro", location="Italy")
greet_with2(location="Italy", name="Pedro")


# %%
import math


def paint_calc(height=0, width=0, cover=5):  # A can would normally cover 5 square meters of surface. That is why it is already initiallized.

    number_of_cans = height * width / cover
    return math.ceil(number_of_cans)  # This will round up -> 1.2 = 2


test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5  # Even if this is missing, the function still outputs the right answer.
paint_calc(height=test_h, width=test_w, cover=coverage)


# %%
# Prime number calculator:
def prime_checker(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number!")
    else:
        print("It is a not a prime number!")


prime_checker(6)
