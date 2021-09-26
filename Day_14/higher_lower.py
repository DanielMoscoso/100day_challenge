import os
import art
import game_data
import random


first_choice = random.choice(game_data.data)
second_choice = random.choice(game_data.data)
score = 0

print(first_choice["follower_count"])
print(second_choice["follower_count"], "\n")

print(f"Compare {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}\n")

print(f"Against {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}\n")

answer = input("Who has more followers? 'A' or 'B'?: ").lower()
if first_choice["follower_count"] > second_choice["follower_count"]:
    if answer == "a":
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that is wrong. Final score: {score}")
else:
    if answer == "b":
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that is wrong. Final score: {score}")
