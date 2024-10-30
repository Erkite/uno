# Uno
# Peyton Wall
# 2024-10-07 wrote the UnoCard class, functions, and doctests
# 2024-10-08 wrote create_deck, deal_hands, and hand_score functions and their doctests
# 2024-10-08 fixed doctests and approached all possibilities

import random

class UnoCard:
    def __init__(self, color, rank):
        """
        this give a card a color and rank
        
        >>> card1 = UnoCard('R', '5')
        >>> card2 = UnoCard('G', 'S')
        >>> card3 = UnoCard('K', 'W')
        >>> str(card1)
        'R5'
        >>> repr(card1)
        "UnoCard('R', '5')"
        >>> str(card2)
        'GS'
        >>> repr(card2)
        "UnoCard('G', 'S')"
        >>> str(card3)
        'KW'
        >>> repr(card3)
        "UnoCard('K', 'W')"
        """
        self.color = color
        self.rank = rank
    
    def can_be_played_on(self, other):
        """
        this determines if this card can be played next

        by the way the card can be played if they match in color or rank or
        if this card is a wild or draw four
        
        >>> UnoCard('Y', 'D').can_be_played_on(UnoCard('Y', '8'))
        True
        >>> UnoCard('Y', 'D').can_be_played_on(UnoCard('B', '8'))
        False
        >>> UnoCard('K', 'W').can_be_played_on(UnoCard('G', '8'))
        True
        >>> UnoCard('B', 'D').can_be_played_on(UnoCard('R', 'D'))
        True
        >>> UnoCard('G', '9').can_be_played_on(UnoCard('G', '9'))
        True
        """
        if self.color == 'K':  # wild or draw 4 can be played on any card
            return True
        if other.color == 'K':  # any card can be played on a wild or draw 4
            return True
        return self.color == other.color or self.rank == other.rank
    
    def score_value(self):
        """
        Returns the score value of the card.
        Number cards are worth their face value, special cards are worth 20 points,
        and Wild/Draw Four cards are worth 50 points.
        
        >>> UnoCard('R', '5').score_value()
        5
        >>> UnoCard('B', 'S').score_value()
        20
        >>> UnoCard('K', 'W').score_value()
        50
        >>> UnoCard('G', '0').score_value()
        0
        """
        if self.rank.isdigit():  # check if it's the 0-9 cards
            return int(self.rank)
        elif self.rank in ['S', 'D', 'R']:  # check if it's a skip, draw 2, or a reverse
            return 20
        else:  # else it has to be a wild or draw 4 cause there's no other options
            return 50
    def __str__(self):
        """
        returns the string of the card
        
        >>> str(UnoCard('R', '5'))
        'R5'
        >>> str(UnoCard('Y', 'D'))
        'YD'
        >>> str(UnoCard('G', '0'))
        'G0'
        >>> str(UnoCard('B', '9'))
        'B9'
        >>> str(UnoCard('K', 'W'))
        'KW'
        """
        return f"{self.color}{self.rank}"

    def __repr__(self):
        """
        returns a string for debugging
        
        >>> repr(UnoCard('R', '5'))
        "UnoCard('R', '5')"
        >>> repr(UnoCard('G', '0'))
        "UnoCard('G', '0')"
        >>> repr(UnoCard('K', 'F'))
        "UnoCard('K', 'F')"
        """
        return f"UnoCard('{self.color}', '{self.rank}')"

def create_deck():
    """
    check the length of deck1 and add 1 to the sum for every black card in deck1 (should be 8)
    >>> deck1 = create_deck()
    >>> len(deck1)
    108
    >>> sum(1 for card in deck1 if card.color == 'K')
    8
    """
    colors = ['R', 'Y', 'G', 'B']
    deck = []

    # add 1 "0" card for each color
    for color in colors:
        deck.append(UnoCard(color, '0'))

    # add 2 copies of (1-9, S, D, R) for each color
    for color in colors:
        for rank in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'D', 'R']:
            deck.append(UnoCard(color, rank))
            deck.append(UnoCard(color, rank))

    # add 4 wild and 4 draw 4 cards
    for number in range(4):
        deck.append(UnoCard('K', 'W'))
        deck.append(UnoCard('K', 'F'))

    random.shuffle(deck)

    return deck

def deal_hands(deck, num_hands):
    """
    this deals 7 cards to each hand
    
    >>> deck = create_deck()
    >>> hands = deal_hands(deck, 2)
    >>> len(hands[0])
    7
    >>> len(hands[1])
    7
    >>> len(deck)
    94

    >>> deck1 = create_deck()
    >>> hands1 = deal_hands(deck, 16)
    >>> len(hands1[0])
    6
    >>> len(hands1[1])
    6
    >>> len(hands1[2])
    6
    >>> len(hands1[3])
    6
    >>> len(hands1[4])
    6
    >>> len(hands1[5])
    6
    >>> len(hands1[6])
    6
    >>> len(hands1[7])
    6
    >>> len(hands1[8])
    6
    >>> len(hands1[9])
    6
    >>> len(hands1[10])
    6
    >>> len(hands1[11])
    6
    >>> len(hands1[12])
    6
    >>> len(hands1[13])
    6
    >>> len(hands1[14])
    5
    >>> len(hands1[15])
    5
    >>> len(deck)
    0
    """
    hands = [[] for number in range(num_hands)]
    for number in range(7):  # deal 7 cards to each hand
        for hand in hands:
            if deck:  # make sure there are cards left to deal
                hand.append(deck.pop(0))
    return tuple(hands)

def hand_score(hand):
    """
    gives the total score value of a hand
    
    >>> hand = [UnoCard('R', '5'), UnoCard('B', 'S'), UnoCard('K', 'W')]
    >>> hand_score(hand)
    75
    >>> hand = [UnoCard('R', '0'), UnoCard('Y', '9'), UnoCard('G', 'D')]
    >>> hand_score(hand)
    29
    """
    return sum(card.score_value() for card in hand)

if __name__ == "__main__":
    import doctest
    doctest.testmod()