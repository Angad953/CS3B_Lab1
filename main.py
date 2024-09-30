import random


def main():
    """Print info about the student and play a card game."""
    deck = Deck()
    """Print information about myself and important policies."""
    print("My name is Angad Sandhu.")
    print("My Student ID is 20617284.")
    print("My email is angadssandhu09@gmail.com.")
    print("Some of the discussed policies include:")
    print("1. Assignments can be submitted up to a week late with a 15% late"
          " penalty.")
    print("2. Regrades can be requested no later than one week after the"
          " assignment has been returned.")
    print("3. You can contact the professor through Canvas Inbox and Canvas"
          " Discussion Forums.")
    while True:
        print("Press 1 to view your current cards and the deck.")
        print("Press 2 to deal a card.")
        print("Press 3 to shuffle the deck.")
        print("Press 4 to quit.")
        user_choice = input()
        try:
            user_input = int(user_choice)
        except ValueError:
            print("Please enter a number  only")
            continue
        match user_input:
            case 1:
                print(f"{'-' * 8}Your cards{'-' * 8}")
                for card in deck.dealt_cards:
                    print(card)
                print(f"{'-' * 8}The deck{'-' * 8}")
                for card in deck.deck_cards:
                    print(card)
            case 2:
                deck.deal()
            case 3:
                deck.shuffle()
            case 4:
                break


class Card:
    """Store the suit and value of a single card."""
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
              'K']

    def __init__(self, suit, value):
        """
        Set the suit and value variables.
        :param suit: (str) Suit of a card
        :param value: (str) Value of a card
        """
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} {self.value}"


class Deck:
    """Create a deck of cards."""
    def __init__(self):
        """Create a deck of cards."""
        self.deck_cards = [Card(suit, value) for suit in Card.suits
                           for value in Card.values]
        self.dealt_cards = []

    def deal(self):
        """Deal a card."""
        self.dealt_cards.append(self.deck_cards[0])
        self.deck_cards.remove(self.deck_cards[0])

    def shuffle(self):
        """Shuffle the deck."""
        if len(self.deck_cards) != 52:
            raise ValueError("Deck must have 52 cards to shuffle.")
        random.shuffle(self.deck_cards)


if __name__ == "__main__":
    main()
