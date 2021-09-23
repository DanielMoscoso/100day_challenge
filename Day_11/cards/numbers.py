# from Day_11.cards.art.art import dict_of_suits  # IDE
from cards.art.art import dict_of_suits  # Console


class Number():
    def __init__(self, suit, number):
        self.name = str(number)
        self.value = number
        self.suit = suit
        self.art = dict_of_suits[self.suit][self.value]


# # ---- For debugging: ----
# card = Number("Clubs", 2)
# print(card.art)
# print(f"name: {card.name}, data type: {type(card.name)}")
# print("suit:", card.suit)
# print("value:", card.value)
# print(f"value: {card.value}, data type: {type(card.value)}")
# # ---- For debugging: ----
