from Day_11.cards import ace
from Day_11.cards import jack
from Day_11.cards import king
from Day_11.cards import queen
from Day_11.cards import numbers


class Deck():
    def __init__(self):
        self.deck = []
        self.list_of_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        # This is for all the Aces, Jacks, Kings, and Queens cards:
        for suit in list_of_suits:
            self.deck.append(ace.Ace(suit))
            self.deck.append(jack.Jack(suit))
            self.deck.append(king.King(suit))
            self.deck.append(queen.Queen(suit))

        # This is for all the numbers:
        # This will keep track of the suits:
        for suit in list_of_suits:
            # This will keep track of the numbers:
            for number in range(2, 11):  # Remember, 'range()' is not inclusive. [2,11)
                self.deck.append(numbers.Number(suit, number))


# # --------------------------- For debugging: ---------------------------
# first_deck = deck()
# # Bulk:
# for card in range(52):
#     print("Name: ", first_deck.deck[card].name)
#     print("Suit:", first_deck.deck[card].suit)
#     print("Value: ", first_deck.deck[card].value, "\n")
#
# print(f"There are currently: {len(first_deck.deck)} cards in the deck")
#
# # Individual card:
# print(first_deck.deck[0].art)
# # --------------------------- For debugging: ---------------------------
