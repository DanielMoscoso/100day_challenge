# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
os.getcwd()
os.chdir("/Users/Daniel/Documents/Python/100days/Day_24/mail_merge")

with open("./Input/Names/invited_names.txt", "r") as file:
    text = file.read()

names = text.split("\n")
