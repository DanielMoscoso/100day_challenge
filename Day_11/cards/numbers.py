from Day_11.cards.art.art import dict_of_suits


class number():
    def __init__(self, suit, number):
        self.name = str(number)
        self.value = number
        self.suit = suit
        # self.art = dict_of_suits[self.suit][self.name]  # Not working right now.


# # ---- For debugging: ----
# card = number("clubs", 1)
# # print(card.art)  # Not working right now.
# print(f"name: {card.name}, data type: {type(card.name)}")
# print("suit:", card.suit)
# print("value:", card.value)
# print(f"value: {card.value}, data type: {type(card.value)}")
# # ---- For debugging: ----
