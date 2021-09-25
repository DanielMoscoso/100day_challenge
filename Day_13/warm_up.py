# ------------------- DEBUGGING -------------------

# ==================================== DONE ====================================
# %%
# # # Describe Problem
# def my_function():
#     for i in range(1, 20):  # The range function is not inclusive, so it has to be 21
#         if i == 20:
#             print("You got it")
#
# print()
# my_function()
# ==================================== DONE ====================================

# %%
# ==================================== DONE ====================================
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  # randint() is inclusive, and when int hits '6', then the list is out of boundaries.
# print(dice_imgs[dice_num])
# ==================================== DONE ====================================

# %%
# ==================================== DONE ====================================
# # # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:  # Right now the year "1994" is in sort of a limbo. If it is less but not included = milenial, if it is more and not included = Gen Z.
#     print("You are a millenial.")
# elif year > 1994:  # It should check if the year ">= 1994":inclusive or "> 1993":from 1994 and up excluding 1993.
#     print("You are a Gen Z.")
# ==================================== DONE ====================================

# %%
# ==================================== DONE ====================================
# # Fix the Errors
# age = input("How old are you?")  # The data type here is "str" and you are trying to compare it to an "int" in the next line.
# if age > 18:
# print("You can drive at age {age}.")  # Indentation here. AND you need to be using an "f" string litteral.
# ==================================== DONE ====================================

# %%
# ==================================== DONE ====================================
# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))  # Here you are checking if the input is equal to 'word_per_page'. Nothing more. You might want to assign it.
total_words = pages * word_per_page
# ==================================== DONE ====================================

# %%
# Use a Debugger
# ==================================== DONE ====================================
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)  # This should be inside the "for loop" otherwise it will overwrite the list, with the "new_item".
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
# ==================================== DONE ====================================
