# from Day_11.cards.art.art import dict_of_suits  # IDE
from cards.art.art import dict_of_suits  # Console


class Ace():
    def __init__(self, suit):
        self.name = "Ace"
        self.value = 10
        self.suit = suit
        self.art = dict_of_suits[self.suit][self.name]


# # ---- For debugging: ----
# card = Ace("clubs")
# print(card.art)
# print("name:", card.name)
# print("suit:", card.suit)
# print("value:", card.value)
# # ---- For debugging: ----
