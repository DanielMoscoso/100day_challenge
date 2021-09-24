from art import logo
import random

ATTEMPTS = 10


def check(number):
    print(f"You have {number} attempts remaining to guess the number.\n")
    if number == 0:
        print("Game over.")


def easy():
    remaining_attempts = ATTEMPTS
    check(remaining_attempts)
    return remaining_attempts


def hard():
    remaining_attempts = ATTEMPTS - 5
    check(remaining_attempts)
    return remaining_attempts


print(logo)
print("Welcome to the Number Guessing Game!")

# Choose the game difficulty:
incorrect_input = True
while incorrect_input:
    difficulty = input("Choose a difficulty. type 'easy' or 'hard': ").lower()
    if difficulty == "easy" or difficulty == "hard":
        if difficulty == "easy":
            remaining = easy()
        else:
            remaining = hard()

        incorrect_input = False  # Get out of the 'while loop'.
    else:
        print("That is not a correct input. Try again, please.\n")

# First statement, and generation of random number:
print("I am thinking of a number berween 1 and 100. (It is a whole number)\n")
random_number = random.randint(0, 100)

# Calculations and output:
wrong_guess = True
while wrong_guess and remaining > 0:
    guess = int(input("Make a guess: "))
    if guess > random_number or guess < random_number:
        if guess > random_number:
            print("Too high. Try again.\n")
        elif guess < random_number:
            print("Too low. Try again.\n")
        else:
            pass

        remaining -= 1
        check(remaining)
    else:
        print("Correct!")
        wrong_guess = False
