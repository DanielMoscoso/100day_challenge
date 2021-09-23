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

player_hand.append(deal())
player_hand.append(deal())
computer_hand.append(deal())


# while player_hand_total < 21:
print("Your cards are: ")
for card in player_hand:
    print(f"{card.name} of {card.suit}")
print(f"Your current score is: {player_hand[0].value + player_hand[1].value}.\n")

print("Computer's first hand is:")
for card in computer_hand:
    print(f"{card.name} of {card.suit}")
print(f"Its current score is: {computer_hand[0].value}.\n")

print("-----------------------------------")
answer = input(f"Type (Y)es to get another card, type (N)o to pass: ").lower()

if answer == "y":
    player_hand.append(deal())
    computer_hand.append(deal())
elif answer == "n":
    computer_hand.append(deal())

# Total value:
player_hand_total = 0
for card in player_hand:
    player_hand_total += card.value

computer_hand_total = 0
for card in computer_hand:
    computer_hand_total += card.value

# Output:
print("Your cards are: ")
for card in player_hand:
    print(f"{card.name} of {card.suit}")
print(f"Your current score is: {player_hand_total}.\n")

print("Computer's hand is:")
for card in computer_hand:
    print(f"{card.name} of {card.suit}")
print(f"Its current score is: {computer_hand_total}.\n")

# ------ For debugging: ------
# print(f"{player_first_card.name} of {player_first_card.suit} with a value of {player_first_card.value} has been removed.")
print(f"There are {len(deck_of_cards.cards)} cards left in the deck \n")
# #
# print("Now, the new first card of the deck is: ")
# print(deck_of_cards.cards[0].name)
# print(deck_of_cards.cards[0].suit)
# print("Value: ", deck_of_cards.cards[0].value, "\n")
# ------ For debugging: ------
