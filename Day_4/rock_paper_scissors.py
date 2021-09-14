import random

print("Welcome to the game of Rock, Paper Scisors!\n")
print("The rules are simple; Rock beats Scisors, Scissors beat Paper, and Paper beats Rock.\n")
print("Yo are going to play agains the computer.\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

answer = int(input("To start, type: (0) for Rock, (1) for Paper, and (2) for Scissors. \n"))
computers_choice = random.randint(0, 2)

# Your answer is Rock:
if answer == 0 and computers_choice == 0:
    print(f"Your choice:\n{rock}\n\n")
    print(f"Computer's choice:\n{rock}\n")
    print("Tie!")
elif answer == 0 and computers_choice == 1:
    print(f"Your choice:\n{rock}\n\n")
    print(f"Computer's choice:\n{paper}\n")
    print("You lose!")
elif answer == 0 and computers_choice == 2:
    print(f"Your choice:\n{rock}\n\n")
    print(f"Computer's choice:\n{scissors}\n")
    print("You win! Congrats!")
# Your answer is Paper:
elif answer == 1 and computers_choice == 0:
    print(f"Your choice:\n{paper}\n\n")
    print(f"Computer's choice:\n{rock}\n")
    print("You win! Congrats!")
elif answer == 1 and computers_choice == 1:
    print(f"Your choice:\n{paper}\n\n")
    print(f"Computer's choice:\n{paper}\n")
    print("Tie!")
elif answer == 1 and computers_choice == 2:
    print(f"Your choice:\n{paper}\n\n")
    print(f"Computer's choice:\n{scissors}\n")
    print("You lose!")
# Your answer is Scissors:
elif answer == 2 and computers_choice == 0:
    print(f"Your choice:\n{scissors}\n\n")
    print(f"Computer's choice:\n{rock}\n")
    print("You lose!")
elif answer == 2 and computers_choice == 1:
    print(f"Your choice:\n{scissors}\n\n")
    print(f"Computer's choice:\n{paper}\n")
    print("You win! Congrats!")
elif answer == 2 and computers_choice == 2:
    print(f"Your choice:\n{scissors}\n\n")
    print(f"Computer's choice:\n{scissors}\n")
    print("Tie!")
else:
    print("That was not allowed, you lose.")
