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

# Reading the files:
with open("./Input/Names/invited_names.txt", "r") as file:
    names_raw = file.read()

with open("./Input/Letters/starting_letter.txt") as template:
    template_raw = template.read()

# Getting all the names:
names = names_raw.split("\n")

# Writing the file:
for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        new_letter = template_raw.replace("[name]", name)

        final_letter.write(new_letter)
