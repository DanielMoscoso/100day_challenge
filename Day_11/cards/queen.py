from cards.art.art import dict_of_suits


class Queen():
    def __init__(self, suit):
        self.name = "Queen"
        self.value = 10
        self.suit = suit
        self.art = dict_of_suits[self.suit][self.name]

    # This is the string representation of the class itself:
    def __str__(self):
        return f"This card is: {self.name} of {self.suit}. With a value of {self.value}."


# # ---- For debugging: ----
# print(Queen("Clubs"))
# card = Queen("Diamonds")
# print(card.art)
# print("name:", card.name)
# print("suit:", card.suit)
# print("value:", card.value)
# # ---- For debugging: ----
