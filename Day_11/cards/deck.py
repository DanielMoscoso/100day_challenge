from Day_11.cards import ace
from Day_11.cards import jack
from Day_11.cards import king
from Day_11.cards import queen
from Day_11.cards import numbers


class Deck():
    def __init__(self):
        self.cards = []
        self.list_of_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        # This is for all the Aces, Jacks, Kings, and Queens cards:
        for suit in self.list_of_suits:
            self.cards.append(ace.Ace(suit))
            self.cards.append(jack.Jack(suit))
            self.cards.append(king.King(suit))
            self.cards.append(queen.Queen(suit))

        # This is for all the numbers:
        # This will keep track of the suits:
        for suit in self.list_of_suits:
            # This will keep track of the numbers:
            for number in range(2, 11):  # Remember, 'range()' is not inclusive. [2,11)
                self.cards.append(numbers.Number(suit, number))


# # --------------------------- For debugging: ---------------------------
# first_deck = deck()
# # Bulk:
# for card in range(52):
#     print("Name: ", first_deck.cards[card].name)
#     print("Suit:", first_deck.cards[card].suit)
#     print("Value: ", first_deck.cards[card].value, "\n")
#
# print(f"There are currently: {len(first_deck.deck)} cards in the deck")
#
# # Individual card:
# print(first_deck.cards[0].art)
# # --------------------------- For debugging: ---------------------------
