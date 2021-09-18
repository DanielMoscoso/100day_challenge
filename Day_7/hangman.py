import random

# NOTE: The game does not see a repeated answer as a "wrong" answer.

# Initialization:
words = ["ardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(words)
chosen_word_length = len(chosen_word)
missing_letters = chosen_word_length

word_list = []
for letters in chosen_word:
    word_list.append("_")

# Instructions:
print(f"lives remaining: {lives}")
print(f"length of the word: {chosen_word_length}")
# print(f"missing letters: {missing_letters}\n")  # This is used for debuggin purposes.

while lives > 0 and missing_letters > 0:
    guess = input("Guess a letter: ").lower()

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
        lives -= 1

    print(hangman)

    print(f"\nmissing letters: {missing_letters}")
    print(f"lives remaining: {lives}\n")

print("Game over!")
