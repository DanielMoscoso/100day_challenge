import random

random_integer = random.randint(1, 10)  # This will generate a random integer between 1 and 10, inclusive.
print(random_integer)

random_float = random.random()  # This will generate a random number between (0,1].
print(random_float)

random_float = random.random() * 5  # This will generate a random FLOATING number between (0,5].
print(random_float)

# %%
# Coin toss:
print("""
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \
  /`       .-'~"-.       `\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
""")

print("Welcome to the heads and tails game.")

answer = input('Type "T" to toss the coin: ').lower()

if answer == "t":
    if random.randint(0, 1):
        print("You got Heads")
    else:
        print("You got Tails")
# %%
# %%
# Random people-picker:
names = input("Give me everybody's names, separated by a coma and a space. ")
names_splitted = names.split(", ")  # The split method does not happen in place.

picked_name = names_splitted[random.randint(0, (len(names_splitted) - 1))]
print(f"{picked_name} is going to buy the meal today!")
# %%
# Now with the method "choice":
names = input("Give me everybody's names, separated by a coma and a space. ")
names_splitted = names.split(", ")  # The split method does not happen in place.

picked_name = random.choice(names_splitted)  # This will pick a random placeholder from a list
print(f"{picked_name} is going to buy the meal today!")
# %%
# %%
# Treasure map:
print("Welcome to the tressure map game. You will have a 3x3 map,\nand your job is to mark your position with and 'x'\n")
print("First you would give the row coordinate, then the column coordinate.")

row1 = ["[]", "[]", "[]"]
row2 = ["[]", "[]", "[]"]
row3 = ["[]", "[]", "[]"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

answer = input("Where do you want to place your x. Remember, Row then Column: ")
first = int(answer[0])
second = int(answer[-1])

map[first - 1][second - 1] = "x"

print(f"{row1}\n{row2}\n{row3}")
