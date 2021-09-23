from Day_11.cards.art import art
from Day_11.cards import deck
import random
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# The cards in the deck have equal probabilities of being drawn.
# The computer is the dealer.


def shuffle(deck):
    random.shuffle(deck)  # This is inplace, so no new variable needs to be created.


def deal():
    return deck_of_cards.cards.pop(0)

# Game starts:
print(art.logo)

deck_of_cards = deck.Deck()
shuffle(deck_of_cards.cards)
# # --------- For debugging: ---------
# print("The first card of the deck is: ")
# print(deck_of_cards.cards[0].name)
# print(deck_of_cards.cards[0].suit)
# print("Value: ", deck_of_cards.cards[0].value, "\n")
# --------- For debugging: ---------

player_hand = []
computer_hand = []

# First deal of hands:
player_hand.append(deal())
player_hand.append(deal())
computer_hand.append(deal())

#  Total value:
player_hand_total = 0
for card in player_hand:
    # If your hand is 12+ and you get an Ace, then its value would be 1, not 10.
    if player_hand_total > 11 and card.name == "Ace":
        player_hand_total += 1
    else:
        player_hand_total += card.value

computer_hand_total = 0
for card in computer_hand:
    # If your hand is 12+ and you get an Ace, then its value would be 1, not 10.
    if computer_hand_total > 11 and card.name == "Ace":
        computer_hand_total += 1
    else:
        computer_hand_total += card.value

# Output:
print("Your hand is: ")
for card in player_hand:
    print(f"{card.name} of {card.suit}")
print(f"Your current score is: {player_hand_total}.\n")

print("Computer's hand is:")
for card in computer_hand:
    print(f"{card.name} of {card.suit}")
print(f"Computer's current score is: {computer_hand_total}.\n")

print("-----------------------------------")
# Repeating if player decides to:
repeat = True
while repeat:
    answer = input(f"Type (Y)es to get another card, type (N)o to pass: ").lower()
    if answer == "y":
        player_hand.append(deal())
        if computer_hand_total < 17:
            computer_hand.append(deal())
    elif answer == "n":  # First draw. Computer must take card.
        if computer_hand_total < 17:
            computer_hand.append(deal())
        repeat = False

    #  Total value:
    player_hand_total = 0
    for card in player_hand:
        # If your hand is 12+ and you get an Ace, then its value would be 1, not 10.
        if player_hand_total > 11 and card.name == "Ace":
            player_hand_total += 1
        else:
            player_hand_total += card.value

    computer_hand_total = 0
    for card in computer_hand:
        # If your hand is 12+ and you get an Ace, then its value would be 1, not 10.
        if computer_hand_total > 11 and card.name == "Ace":
            computer_hand_total += 1
        else:
            computer_hand_total += card.value

    # Output:
    print("Your hand is: ")
    for card in player_hand:
        print(f"{card.name} of {card.suit}")
    print(f"Your current score is: {player_hand_total}.\n")

    print("Computer's hand is:")
    for card in computer_hand:
        print(f"{card.name} of {card.suit}")
    print(f"Computer's current score is: {computer_hand_total}.\n")

    # End of game:
    if player_hand_total <= 21:
        if player_hand_total > computer_hand_total and answer == "n":
            print("You win, congrats!\n")
            break
    else:
        print("BUSTED! Computer wins! Sorry.\n")
        break

    if computer_hand_total <= 21:
        if computer_hand_total > player_hand_total and answer == "n":
            print("Computer wins! Sorry.\n")
            break
    else:
        print("COMPUTER BUSTED! You win, congrats!\n")
        break

    if answer == "n" and computer_hand_total < 21 and player_hand_total < 21 and player_hand_total == computer_hand_total:
        print("DRAW!\n")
        break

    print("-----------------------------------")
# ------ For debugging: ------
# print(f"{player_first_card.name} of {player_first_card.suit} with a value of {player_first_card.value} has been removed.")
# print(f"There are {len(deck_of_cards.cards)} cards left in the deck \n")
# #
# print("Now, the new first card of the deck is: ")
# print(deck_of_cards.cards[0].name)
# print(deck_of_cards.cards[0].suit)
# print("Value: ", deck_of_cards.cards[0].value, "\n")
# ------ For debugging: ------
