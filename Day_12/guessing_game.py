from art import logo
import random
import os

ATTEMPTS = 10


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


def check(number):
    """
    This function prints outs how many attempts left the player has.
    And also checks if they ran out of attempts. If that is the case,
    then it also outputs 'Game over'.
    """
    print(f"You have {number} attempts remaining to guess the number.\n")
    if number == 0:
        print("Game over.\n")


def easy():
    """
    This function sets the numbers of attempts to its default, which is 10.
    """
    remaining_attempts = ATTEMPTS
    check(remaining_attempts)
    return remaining_attempts


def hard():
    """
    This function sets the number of attempts to 5.
    """
    remaining_attempts = ATTEMPTS - 5
    check(remaining_attempts)
    return remaining_attempts


def play():
    """
    This function is where all the fun begins. It has all game's logics.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!\n")

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
            print("Correct!\n")
            wrong_guess = False


if __name__ == '__main__':
    while (input("Do you want to play? Type (Y)es or (N)o: ")).lower() == "y":
        clear()
        play()
