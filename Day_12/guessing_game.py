from art import logo
import random

ATTEMPTS = 10


def check(number):
    print(f"You have {number} attempts remaining to guess the number.\n")


def easy():
    remaining_attempts = ATTEMPTS
    check(remaining_attempts)
    return remaining_attempts


def hard():
    remaining_attempts = ATTEMPTS - 5
    check(remaining_attempts)
    return remaining_attempts


# print(logo)
print("Welcome to the Number Guessing Game!")

# Choose the game difficulty:
incorrect_input = True
while incorrect_input:
    difficulty = input("Choose a difficulty. type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        remaining = easy()
        incorrect_input = False
    elif difficulty == "hard":
        remaining = hard()
        incorrect_input = False
    else:
        print("That is not a correct input. Try again, please.")

# First statement, and generation of random number:
print("I am thinking of a number berween 1 and 100. (It is a whole number)\n")
random_number = random.randint(0, 100)

# Calculations and output:
guess = int(input("Make a guess: "))
if guess > random_number or guess < random_number:
    if guess > random_number:
        print("Too high.\n")
    elif guess < random_number:
        print("Too low.\n")
    else:
        pass

    remaining -= 1
    check(remaining)
else:
    print("Correct!")
