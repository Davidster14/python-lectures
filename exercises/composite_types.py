SUITS = { 'CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS' }
RANKS = [ 'ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO' ]

def deck() -> list[tuple]:
    '''Create a deck of cards.
    Each card is a tuple of suit and rank.
    '''
    pass

def split(deck, pos: int) -> tuple[list, list]:
    ''''Split a deck of cards at a given position.
    Return a tuple containing first and second part of the deck.
    '''
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