import unittest
import random

from exercises.composite_types import *

class TestCards(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.seed = 1337
        self.deck = [ (suit, rank) for suit in SUITS for rank in RANKS ]
        self.deck.sort()
    
    def test_deck(self):
        self.assertEquals(sorted(deck()), self.deck)

    def test_split(self):
        pos = 13
        fst, snd = split(self.deck, pos)
        self.assertEquals(fst, self.deck[:pos])
        self.assertEquals(snd, self.deck[pos:])
    
    def test_peek(self):
        self.assertEqual(peek(self.deck), self.deck[-1])
    
    def test_draw(self):
        card = self.deck[-1]
        self.assertEqual(draw(self.deck), card)

    def test_draw_random(self):
        random.seed(self.seed)
        card = self.deck[random.randint(0, len(self.deck)-1)]
        random.seed(self.seed)
        self.assertEqual(draw(self.deck, random=True), card)