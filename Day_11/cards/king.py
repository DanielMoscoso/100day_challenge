from Day_11.cards.art.art import dict_of_suits


class King():
    def __init__(self, suit):
        self.name = "King"
        self.value = 10
        self.suit = suit
        self.art = dict_of_suits[self.suit][self.name]


# # # ---- For debugging: ----
# card = King("Clubs")
# print(card.art)
# print("name:", card.name)
# print("suit:", card.suit)
# print("value:", card.value)
# # # ---- For debugging: ----
