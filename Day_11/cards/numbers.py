from cards.art.art import dict_of_suits


class Number():
    def __init__(self, suit, number):
        self.name = str(number)
        self.value = number
        self.suit = suit
        self.art = dict_of_suits[self.suit][self.value]

    # This is the string representation of the class itself:
    def __str__(self):
        return f"This card is: {self.name} of {self.suit}. With a value of {self.value}."


# # ---- For debugging: ----
# print(Number("Clubs", 2))
# card = Number("Clubs", 2)
# print(card.art)
# print(f"name: {card.name}, data type: {type(card.name)}")
# print("suit:", card.suit)
# print("value:", card.value)
# print(f"value: {card.value}, data type: {type(card.value)}")
# # ---- For debugging: ----
