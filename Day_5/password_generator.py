import random

print("Welcome to the password generator!\n")
letters_answer = int(input("How many letters would you like in your password?: \n"))
symbols_answer = int(input("How many symbols would you like?: \n"))
numbers_answer = int(input("How many numbers would you like?: \n"))

letters = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
capital_letters = letters.split(", ")
lower_case_letters = letters.lower().split(", ")
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

total_characters = letters_answer + symbols_answer + numbers_answer
pasword = ""
one_capital = 0
one_lower = 0
one_number = 0
one_special = 0
token_letter = 0
token_number = 0
token_special = 0
# for number in range(0, total_characters + 1):
for number in range(1, total_characters + 100):  # This would be better excecuted with a "while loop". It is +100 because there might be the case that when a random number is generated to pick between 1-3, the number 2 (for example) is never picked.
    randomizer = random.randint(0, 3)
    random_capital_letter = random.randint(0, 25)
    random_lower_case_letter = random.randint(0, 25)
    random_number = random.randint(0, 8)
    random_special_character = random.randint(0, 8)
    # # OR -> Might be slightly better since you do not have to count.
    # random_capital_letter = random.choice(capital_letters)
    # random_lower_case_letter = random.choice(lower_case_letters)
    # random_number = random.choice(numbers)
    # random_special_character = random.choice(special_characters)

    # elif randomizer == 1:  # Capital letter
    if(randomizer == 0 and one_capital == 0) or (randomizer == 0 and one_capital > 0 and one_lower > 0 and one_number > 0 and one_special > 0 and token_letter < letters_answer):
        pasword += capital_letters[random_capital_letter]
        # pasword += random_capital_letter  # This is for the alternative "random.choice()".
        one_capital += 1
        token_letter += 1
    # elif randomizer == 1:  # Lower case letter
    elif(randomizer == 1 and one_lower == 0) or (randomizer == 1 and one_capital > 0 and one_lower > 0 and one_number > 0 and one_special > 0 and token_letter < letters_answer):
        pasword += lower_case_letters[random_lower_case_letter]
        # pasword += random_lower_case_letter  # This is for the alternative "random.choice()".
        one_lower += 1
        token_letter += 1
    # elif randomizer == 2:  # Number
    elif(randomizer == 2 and one_number == 0) or (randomizer == 2 and one_capital > 0 and one_lower > 0 and one_number > 0 and one_special > 0 and token_number < numbers_answer):
        pasword += numbers[random_number]
        # pasword += random_number  # This is for the alternative "random.choice()".
        one_number += 1
        token_number += 1
    # else:  # Special character
    elif(randomizer == 3 and one_special == 0) or (randomizer == 3 and one_capital > 0 and one_lower > 0 and one_number > 0 and one_special > 0 and token_special < symbols_answer):
        pasword += special_characters[random_special_character]
        # pasword += random_special_character  # This is for the alternative "random.choice()".
        one_special += 1
        token_special += 1
    else:
        pass

print(f"Your password is: {pasword}\nPassword length: {len(pasword)}\n")
# %%
# Best way: Password generator:
# Greetings and user questions:
print("Welcome to the password generator!\n")
letters_answer = int(input("How many letters would you like in your password?: \n"))
symbols_answer = int(input("How many symbols would you like?: \n"))
numbers_answer = int(input("How many numbers would you like?: \n"))

# First initialization:
letters = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
capital_letters = letters.split(", ")
lower_case_letters = letters.lower().split(", ")
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Create all the characters in the password:
password = []
token_lower_letter = 0
token_capital_letter = 0
for number in range(1, letters_answer + 1):
    # This will make sure that at least one lower case letter, and one capital letter is used in case of 2 letter password.
    if token_lower_letter == 0 or token_lower_letter > 0 and token_capital_letter > 0:
        password.append(random.choice(capital_letters))
        token_lower_letter += 1
    elif token_capital_letter == 0 or token_lower_letter > 0 and token_capital_letter > 0:
        password.append(random.choice(lower_case_letters))
        token_capital_letter += 1
    else:
        pass

for number in range(1, symbols_answer + 1):
    password.append(random.choice(special_characters))

for number in range(1, numbers_answer + 1):
    password.append(random.choice(numbers))

# Randomize it and then create a string from it:
random.shuffle(password)
password_string = ""
for char in password:
    password_string += char

# Final output:
print(f"Your password is: {password_string}\nPassword length: {len(password_string)}\n")
