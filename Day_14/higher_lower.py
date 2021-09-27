import os
import art
import game_data
import random


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


def right_choice(first_item, second_item):
    """
    This function takes 2 arguments: the first and the second choice, and returns
    which one has bigger follower counts, or in other words, the correct answer.
    """
    if first_item["follower_count"] > second_item["follower_count"]:
        return "a"
    else:
        return "b"


def play():
    current_score = 0
    answer = ""
    correct_answer = ""
    keep_playing = True

    print(art.logo)

    while keep_playing:
        first_choice = random.choice(game_data.data)
        second_choice = random.choice(game_data.data)

        # # -------------- For debugging --------------
        # print(first_choice["follower_count"])
        # print(second_choice["follower_count"], "\n")
        # # -------------- For debugging --------------

        print(f"Compare {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
        print(art.vs)
        print(f"Against {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}\n")

        answer = input("Who has more followers? 'A' or 'B'?: ").lower()
        correct_answer = right_choice(first_choice, second_choice)

        if answer == correct_answer:
            current_score += 1
            print(f"You are right! Current score {current_score}")
            clear()
        else:
            print(f"Sorry, that is wrong. Final score {current_score}")

            answer2 = input("Do you want to play again? Type (Y)es or (N)o: ").lower()
            if answer2 == "y":
                clear()
                play()
            else:
                return


play()
