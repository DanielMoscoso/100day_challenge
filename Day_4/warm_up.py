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
