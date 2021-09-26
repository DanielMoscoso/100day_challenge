import os
import art
import game_data
import random


def right_choice(first_item, second_choice):
    """
    This function takes 2 arguments: the first and the second choice, and returns
    which one has bigger follower counts, or in other words, the correct answer.
    """
    if first_choice["follower_count"] > second_choice["follower_count"]:
        return "a"
    else:
        return "b"


current_score = 0
answer = ""
correct_answer = ""
keep_playing = True

while keep_playing:
    first_choice = random.choice(game_data.data)
    second_choice = random.choice(game_data.data)

    print(first_choice["follower_count"])
    print(second_choice["follower_count"], "\n")

    print(f"Compare {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}\n")
    print(f"Against {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}\n")

    answer = input("Who has more followers? 'A' or 'B'?: ").lower()
    correct_answer = right_choice(first_choice, second_choice)

    if answer == correct_answer:
        current_score += 1
        print(f"You are right! Current score {current_score}")
    else:
        print(f"Sorry, that is wrong. Final score {current_score}")
        keep_playing = False
