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

    def test_follows(self):
        card = ('SPADES', 'ACE')
        suits = SUITS - {'SPADES'}
        ranks = [ rank for rank in RANKS if rank != 'ACE' ]

        self.assertTrue(follows(card, suit='SPADES'))
        self.assertTrue(follows(card, rank='ACE'))
        self.assertTrue(follows(card, suit='SPADES', rank='ACE'))

        for suit in suits:
            self.assertFalse(follows(card, suit=suit))

        for rank in ranks:
            self.assertFalse(follows(card, rank=rank))

        for suit, rank in [ (suit, rank) for suit in suits for rank in ranks ]:
            self.assertFalse(follows(card, suit=suit, rank=rank))

    def test_filter_by_suit(self):
        suit = 'HEARTS'
        actual = sorted(filter_by(self.deck, suit=suit))
        expected = sorted([c for c in self.deck if c[0] == suit])
        self.assertEquals(actual, expected)

    def test_filter_by_rank(self):
        rank = 'QUEEN'
        actual = sorted(filter_by(self.deck, rank=rank))
        expected = sorted([c for c in self.deck if c[1] == rank])
        self.assertEquals(actual, expected)

    def test_filter_by_suit_and_rank(self):
        suit, rank = 'SPADES', 'ACE'
        actual = sorted(filter_by(self.deck, suit=suit, rank=rank))
        expected = sorted([c for c in self.deck if c == (suit, rank)])
        self.assertEquals(actual, expected)

    def test_has_card_suit(self):
        suit = 'DIAMONDS'
        self.assertEquals(has_card(self.deck, suit=suit), True)
        self.assertEquals(has_card(self.deck[:13], suit=suit), False)

    def test_has_card_rank(self):
        rank = 'ACE'
        self.assertEquals(has_card(self.deck, rank=rank), True)