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
# %%
# There is an easier and more clever way of checking the conditionals:

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
images = [rock, paper, scissors]

# Your answer is Rock:
if answer >= 3 or answer < 0:  # A very large number, or a negative number as your answer.
    print("That was not allowed, you lose.")
elif answer == 0 and computers_choice == 2:
    print(f"Your choice:\n{images[answer]}\n\n")
    print(f"Computer's choice:\n{images[computers_choice]}\n")
    print("You win! Congrats!")
elif answer == 2 and computers_choice == 0:  # You chose scissors and the computer rock.
    print(f"Your choice:\n{images[answer]}\n\n")
    print(f"Computer's choice:\n{images[computers_choice]}\n")
    print("You lose!")
elif answer < computers_choice:  # You chose paper and the computer scissors.
    print(f"Your choice:\n{images[answer]}\n\n")
    print(f"Computer's choice:\n{images[computers_choice]}\n")
    print("You lose!")
elif answer > computers_choice:  # You chose scissors and the computer paper.
    print(f"Your choice:\n{images[answer]}\n\n")
    print(f"Computer's choice:\n{images[computers_choice]}\n")
    print("You win! Congrats!")
elif answer == computers_choice:  # Any time there is a tie.
    print(f"Your choice:\n{images[answer]}\n\n")
    print(f"Computer's choice:\n{images[computers_choice]}\n")
    print("Tie!")
