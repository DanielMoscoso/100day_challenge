import random
import art  # Use this if you want to run it in command line.
import words_list  # Use this if you want to run it in command line.
# from Day_7 import art  # Use this if you want to run it in IDE.
# from Day_7 import words_list  # Use this if you want to run it in IDE.
import os

# # This is used for debugging purposes.
# path = os.getcwd()
# print(path)

# NOTE: The game does not see a repeated answer as a "wrong" answer.


# Define our clear function (for when we want to clear the screen after each try):
def clear():
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


# Initialization:
# words = ["ardvark", "baboon", "camel"]  # This is used for debugging purposes.
lives = 6

chosen_word = random.choice(words_list.word_list)
chosen_word_length = len(chosen_word)
missing_letters = chosen_word_length

word_list = []
for letters in chosen_word:
    word_list.append("_")

# Instructions:
print(art.logo)
# print(f"The word is: {chosen_word}")  # This is used for debugging purposes.
print(f"lives remaining: {lives}")
print(f"length of the word: {chosen_word_length}\n\n")
# print(f"missing letters: {missing_letters}\n")  # This is used for debugging purposes.

while lives > 0 and missing_letters > 0:
    guess = input("Guess a letter: ").lower()
    clear()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            word_list[index] = letter

    # This creates the hangman-like output -> underscores and letters (no list):
    hangman = ""
    for letter in word_list:
        hangman += " " + letter

    # This simply counts how many letters are left in the word:
    missing_letters = hangman.count("_")

    # If the person did not answer correctly:
    if hangman.count(guess) == 0:
        print(f'You guessed "{guess}", that is not in the word. You lose a life.')
        lives -= 1

    print(hangman)

    # This gives a simple GUI of the stick-figure hangman:
    if lives == 5:
        print(art.stages[lives])
    elif lives == 4:
        print(art.stages[lives])
    elif lives == 3:
        print(art.stages[lives])
    elif lives == 2:
        print(art.stages[lives])
    elif lives == 1:
        print(art.stages[lives])
    else:
        print(art.stages[lives])

    if guess in word_list:
        print(f'You have already guessed "{guess}". Try again.')

    # print(f"\nmissing letters: {missing_letters}")  # This is used for debugging purposes.
    print(f"lives remaining: {lives}\n")

    # This tells the user if they won or lost at the end of the game:
    if missing_letters == 0 and lives > 0:
        print("You won!\n")
    elif missing_letters > 0 and lives == 0:
        print("You lost!\n")
    else:
        pass

print("Game over!")
# %%
import random
import art  # Use this if you want to run it in command line.
import words_list  # Use this if you want to run it in command line.
# from Day_7 import art  # Use this if you want to run it in IDE.
# from Day_7 import words_list  # Use this if you want to run it in IDE.
import os

# NOTE: The game does not see a repeated answer as a "wrong" answer.


# Define our clear function (for when we want to clear the screen after each try):
def clear():
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


# Initialization:
# words_list = ["ardvark", "baboon", "camel"]  # This is for debugging
lives = 6

chosen_word = random.choice(words_list.word_list)
chosen_word_length = len(chosen_word)
missing_letters = chosen_word_length

word_list = []
for letters in chosen_word:
    word_list.append("_")

print(art.logo)

# Instructions:
print(f"lives remaining: {lives}")
print(f"length of the word: {chosen_word_length}")
# print(f"missing letters: {missing_letters}\n")  # This is used for debugging purposes.

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in word_list:
        print(f'You have already guessed "{guess}". Try again.')

    for position in range(chosen_word_length):
        letter = chosen_word[position]

        if letter == guess:
            word_list[position] = letter

    # Merge all the elements in the list and turn it into a String -> "join()", separating the elements with a space.
    print(f"{' '.join(word_list)}")

    if "_" not in word_list:
        end_of_game = True
        print("You win!\n")

    # This gives a simple GUI of the stick-figure hangman:
    print(art.stages[lives])

    if guess not in chosen_word:
        print(f'You guessed "{guess}", that is not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!\n")

print("Game over!")
