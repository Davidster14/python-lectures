SUITS = { 'CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS' }
RANKS = [ 'ACE', 'KING', 'QUEEN', 'JACK', 'TEN',
         'NINE', 'EIGHT', 'SEVEN', 'SIX', 'FIVE', 'FOUR', 'THREE', 'TWO' ]

def deck() -> list[tuple]:
    '''Create a deck of cards.
    Each card is a tuple of suit and rank.
    '''
    pass

def split(deck, pos: int) -> tuple[list, list]:
    pass

def peek(deck: list[tuple]) -> tuple:
    pass

def draw(deck: list[tuple], random=False) -> tuple:
    pass

# filter by suit
# filter by rank
# contains specific rank