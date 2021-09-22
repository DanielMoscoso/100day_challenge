from Day_11.cards import ace
from Day_11.cards import jack
from Day_11.cards import king
from Day_11.cards import queen
from Day_11.cards import numbers

deck = []
list_of_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

# This is for all the Aces, Jacks, Kings, and Queens cards:
for specials in list_of_suits:
    deck.append(ace.Ace(specials))
    deck.append(jack.Jack(specials))
    deck.append(king.King(specials))
    deck.append(queen.Queen(specials))


# ---- For debugging: ----
for card in range(4):
    print(deck[card].name)
    print("value:", deck[0].value)
    print(deck[card].suit)
    print(deck[card].art)

print(f"There are currently: {len(deck)} cards in the deck")
# ---- For debugging: ----
