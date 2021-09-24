# from Day_11.cards.art import art  # IDE
# from Day_11.cards import deck  # IDE
from cards.art import art  # Console
from cards import deck  # Console
import random
import os
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# The cards in the deck have equal probabilities of being drawn.
# The computer is the dealer.


def clear():
    """
    This function is used for clearing the entire screen.
    If you IDE does not support it, then you might want to see it
    in action when running on command line.
    """
    # For windows
    if os.name == 'nt':
        os.system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def shuffle(deck):
    """
    This function shuffles the deck.
    """
    random.shuffle(deck)  # This is inplace, so no new variable needs to be created.


def play():
    """
    This function is where the fun begins. It starts the game.
    All the logic is inside it.
    """
    def deal():
        """
        This nested function deals a card to whoever calls it.
        It is nested because it will not be able to access the parameters
        inside the 'play()' function otherwise; They would be outside the scope.
        """
        return deck_of_cards.cards.pop(0)

    # Game starts:
    play_again = True
    while play_again:
        clear()
        print(art.logo)

        deck_of_cards = deck.Deck()
        shuffle(deck_of_cards.cards)
        # # --------- For debugging: ---------
        # print("The first card of the deck is: ")
        # print(deck_of_cards.cards[0].name)
        # print(deck_of_cards.cards[0].suit)
        # print("Value: ", deck_of_cards.cards[0].value, "\n")
        # --------- For debugging: ---------

        player_hand = []
        computer_hand = []
        blackjack = False

        # First deal of hands:
        player_hand.append(deal())
        player_hand.append(deal())
        computer_hand.append(deal())

        # =============================== Calculations: ===============================
        player_hand_total = 0
        for card in player_hand:
            player_hand_total += card.value

        computer_hand_total = 0
        for card in computer_hand:
            computer_hand_total += card.value
        # =============================== Calculations: ===============================

        # --------------------------- Output: ---------------------------
        # Player:
            print("Your hand is: ")
            # Artwork:
            for card in player_hand:
                print(f"{card.art}")
            for card in player_hand:
                print(f"{card.name} of {card.suit}")
            print(f"Your current score is: {player_hand_total}.\n")

        print("-----------------------------------")
        print("Computer's hand is:")
        # Artwork:
        for card in computer_hand:
            print(f"{card.art}")
        print(art.dict_of_suits["Blank"])  # This simulates the upside down card the dealer has.
        for card in computer_hand:
            print(f"{card.name} of {card.suit}")
        print(f"Computer's current score is: {computer_hand_total}.\n")
        # --------------------------- Output: ---------------------------

        print("-----------------------------------")
        # >>>>>>>>>>>>>>> User's BlackJack: <<<<<<<<<<<<<<<
        if player_hand_total == 20:
            for card in player_hand:
                if card.name == "Ace":
                    blackjack = True
        # >>>>>>>>>>>>>>> User's BlackJack: <<<<<<<<<<<<<<<
        # >>>>>>>>>>>>>>>>>>>>>>> Repeating if player decides to: >>>>>>>>>>>>>>>>>>>>>>>
        repeat = True
        while repeat:
            answer = input(f"Type (Y)es to get another card, type (N)o to pass: ").lower()
            clear()
            if answer == "y":
                player_hand.append(deal())
                if computer_hand_total < 17:
                    computer_hand.append(deal())
            elif answer == "n" and blackjack is False:  # First draw. Computer must take card.
                if computer_hand_total < 17:
                    computer_hand.append(deal())
                repeat = False

            # ============================= Calculations: =============================
            player_hand_total = 0
            for card in player_hand:
                # If your hand is 12+ and you get an Ace, then its value would be 1, not 10.
                if player_hand_total > 11 and card.name == "Ace":
                    player_hand_total += 1
                else:
                    player_hand_total += card.value

            computer_hand_total = 0
            for card in computer_hand:
                # If your hand is 12+ and you get an Ace, then its value would be 1, not 10.
                if computer_hand_total > 11 and card.name == "Ace":
                    computer_hand_total += 1
                else:
                    computer_hand_total += card.value
            # ============================= Calculations: =============================

            # ----------------------- Output: -----------------------
            print("Your hand is: ")
            # Artwork:
            for card in player_hand:
                print(f"{card.art}")
            for card in player_hand:
                print(f"{card.name} of {card.suit}")
            print(f"Your current score is: {player_hand_total}.\n")

            print("-----------------------------------")
            print("Computer's hand is:")
            # Artwork:
            for card in computer_hand:
                print(f"{card.art}")
            for card in computer_hand:
                print(f"{card.name} of {card.suit}")
            print(f"Computer's current score is: {computer_hand_total}.\n")
            # ----------------------- Output: -----------------------

            # End of game:
            if player_hand_total <= 21:
                # >>>>>>>>>>>>>>> User's BlackJack: <<<<<<<<<<<<<<<
                if blackjack:
                    print("BLACKJACK!!! You win!\n")
                    break
                # >>>>>>>>>>>>>>> User's BlackJack: <<<<<<<<<<<<<<<
                elif player_hand_total > computer_hand_total and answer == "n":
                    print("You win, congrats!\n")
                    break
                else:
                    pass
            else:
                print("BUSTED! Computer wins! Sorry.\n")
                break

            if computer_hand_total <= 21:
                # >>>>>>>>>> Computer's BlackJack: <<<<<<<<<<
                if computer_hand_total == 20:
                    for card in computer_hand:
                        if card.name == "Ace":
                            print("COMPUTER'S BLACKJACK!!! You lose, sorry!\n")
                            break
                # >>>>>>>>>> Computer's BlackJack: <<<<<<<<<<

                elif computer_hand_total > player_hand_total and answer == "n":
                    print("Computer wins! Sorry.\n")
                    break
            else:
                print("COMPUTER BUSTED! You win, congrats!\n")
                break

            if answer == "n" and computer_hand_total < 21 and player_hand_total < 21 and player_hand_total == computer_hand_total and blackjack is False:
                print("DRAW!\n")
                break
            print("-----------------------------------")
        # ------ For debugging: ------
        # print(f"{player_first_card.name} of {player_first_card.suit} with a value of {player_first_card.value} has been removed.")
        # print(f"There are {len(deck_of_cards.cards)} cards left in the deck \n")
        # #
        # print("Now, the new first card of the deck is: ")
        # print(deck_of_cards.cards[0].name)
        # print(deck_of_cards.cards[0].suit)
        # print("Value: ", deck_of_cards.cards[0].value, "\n")
        # ------ For debugging: ------
        answer2 = input("Do you want to play again? (Y)es or (N)o?: ").lower()
        if answer2 == "n":
            print("\nGreat, see you next time!\n")
            play_again = False
        elif answer2 == "y":
            # You need this in order to end the recursion when the user types "(N)o" in the final question.
            # It ends the repetition, and starts a fresh game.
            play_again = False
            play()
        else:
            print("\nThat is not a correct input. Bye!\n")
            play_again = False


# Rady player one:
if __name__ == '__main__':
    play()
