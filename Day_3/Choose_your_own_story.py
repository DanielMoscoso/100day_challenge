print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

cross_road = (input("You are at a cross road. Where do you want to go? Left or Right?: ")).lower()
if cross_road == "left":
    print("You fell into a hole and died. Game over.")
else:
    pass

lake = (input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat, or "swim" to swim across: ')).lower()
if lake == "wait":
    pass
else:
    print("The lake was infested with piranhas, they ate you alive. Game over.")

doors = (input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door do you choose? (There is no sidequest, easter egg or fourth option. Sorry): ")).lower()
if doors == "blue":
    print("Alligators came out of the door and ate you. Game over")
elif doors == "red":
    print("A fireball engulfed you. Game over.")
elif doors == "yellow":
    print("You found the treasure! Congratulations!")
else:
    print("I said there was no fourth option. You are smitten by the heavens. Game over.")
