from Day_11.cards.art.art import dict_of_suits


class Jack():
    def __init__(self, suit):
        self.name = "Jack"
        self.value = 10
        self.suit = suit
        self.art = dict_of_suits[self.suit][self.name]


# # ---- For debugging: ----
# card = Jack("clubs")
# print(card.art)
# print("name:", card.name)
# print("suit:", card.suit)
# print("value:", card.value)
# # ---- For debugging: ----
