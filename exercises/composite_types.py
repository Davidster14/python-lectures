SUITS = { 'CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS' }
RANKS = [ 'ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO' ]

'''TASK = Create a deck of cards.
    Each card is a tuple of suit and rank.
    '''

def deck()  -> list[tuple]:
    suits = ['CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS']
    ranks = {'ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO'} 
    
    deck =[(suit, rank) for suit in suits for rank in ranks]
    return deck

# Funktionsaufruf

deck_of_cards = deck()
for card in deck_of_cards:
    print(card)

    pass

    ''''Split a deck of cards at a given position._______________________________________________
    Return a tuple containing first and second part of the deck.
    '''

def split(deck, position): #   Teilt das Kartenspiel an der angegebenen Position.
   
    first_part = deck[:position]
    second_part = deck[position:]
    return (first_part, second_part)

deck = deck()
position = 21  # zufällige Position zum Aufteilen des Kartenspiels

first_part, second_part = split(deck, position)
print("_________________________________")
print("\nErster Teil des Kartenspiels:")
print(first_part)
print("___________________________________________________________________")
print("\nZweiter Teil des Kartenspiels:")
print(second_part)
print("______________________________________________________")

pass


''' Show top card from the deck.____________________________________________________'''

def peek(deck: list[tuple]) -> tuple:
    if deck:
        return deck[0]
    else:
        return None
    
top_card = peek(deck)
print("die oberste Karte des Kartenspiels ist die :")
print(top_card)
print("______________________________________")
    
pass



def draw(deck: list[tuple], random=False) -> tuple:
    '''Draw a card from the deck.
    Choose a random card when random=True,
    otherwise choose top card.
    
    Hint: Use the randint() function:
    from random import randint
    '''
    pass

def follows(card, suit=None, rank=None):
    '''Check whether a card follows a given suit and rank.
    Prüfen Sie, ob eine Karte einer bestimmten Farbe und einem bestimmten Rang entspricht.
    zB card  Fach 5 = hearts  und wert??
    '''
    
    pass

def filter_by(deck: list[tuple], suit=None, rank=None) -> list[tuple]:
    '''Filter the deck by the given suit and rank.
    When only suit is given, include cards of all ranks with the given suit.
    When only rank is given, include cards of all suits with the given rank.
    When both are given, only include cards with the given suit and rank.
    When none are given, include all cards (no effect).
    '''
    pass

def has_card(deck: list[tuple], suit=None, rank=None) -> bool:
    '''Check whether a deck has cards of a given suit and rank.
    Prüfen Sie, ob ein Deck Karten einer bestimmten Farbe und eines bestimmten Ranges enthält.
    '''
    pass