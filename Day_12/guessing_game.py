from art import logo

ATTEMPTS = 10


def check(number):
    print(f"You have {number} attempts remaining to guess the number.")


def easy():
    remaining_attempts = ATTEMPTS
    check(remaining_attempts)
    return remaining_attempts


def hard():
    remaining_attempts = ATTEMPTS - 5
    check(remaining_attempts)
    return remaining_attempts


print("Welcome to the Number Guessing Game!")
print("I am thinking of a number berween 1 and 100.")

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


# print(logo)
