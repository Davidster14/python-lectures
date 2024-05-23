SUITS = { 'CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS' }
RANKS = [ 'ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO' ]

'''TASK = Create a deck of cards.
    Each card is a tuple of suit and rank.
    '''

def deck():  #-> list[tuple]:
    suits = ['CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS']
    ranks = ['ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO'] 
    
    deck =[(suit, rank) for suit in suits for rank in ranks]
    return deck

# Funktionsaufruf

deck_of_cards = deck()
for card in deck_of_cards:
    print(card)

    pass


    ''''Split a deck of cards at a given position.
    Return a tuple containing first and second part of the deck.
    '''
def split(deck, pos: int): #-> tuple[list, list]:

    pass

def peek(deck: list[tuple]) -> tuple:
    '''Show top card from the deck.
    '''
    pass

def draw(deck: list[tuple], random=False) -> tuple:
    '''Draw a card from the deck.
    Choose a random card when random=True,
    otherwise choose top card.
    '''
    pass

# filter by suit
# filter by rank
# contains specific rank