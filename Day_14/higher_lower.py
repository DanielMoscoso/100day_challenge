import os
import art
import game_data
import random


def score(first_item, second_item, answer, current_score):
    """
    This function takes 4 arguments: The first and second random choice the computer
    makes, the answer from the user, and the current score to calculate if the user
    was right or wrong. Then updates the score accordingly.
    """
    if answer == "a" and first_choice["follower_count"] > second_choice["follower_count"]:
        print("You are right!")
        return current_score + 1
    elif answer == "b" and first_choice["follower_count"] < second_choice["follower_count"]:
        print("You are right!")
        return current_score + 1
    else:
        print("Sorry, that is wrong.")
        return current_score


first_choice = random.choice(game_data.data)
second_choice = random.choice(game_data.data)
current_score = 0
keep_going = True

print(first_choice["follower_count"])
print(second_choice["follower_count"], "\n")

print(f"Compare {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}\n")

print(f"Against {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}\n")

answer = input("Who has more followers? 'A' or 'B'?: ").lower()

current_score = score(first_choice, second_choice, answer, current_score)
print(current_score)
