import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("hearts", 3)
        self.card_2 = Card("spades", 1)
        self.card_game = CardGame()
        self.cards = [self.card_1, self.card_2]

    def test_check_for_ace(self):
        ace = self.card_game.check_for_ace(self.card_2)
        self.assertEqual(True, ace)

    def test_highest_card(self):
        highest = self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(self.card_1, highest)

    def test_cards_total(self):
        total = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 4", total)

