import unittest
from src.pub import Pub
from src.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Clansman", 500.00)
        self.drink_1 = Drinks("Vodka Martini", 10.00, 40)
        self.drink_2 = Drinks("Mojito", 12.50, 40)
        self.drink_3 = Drinks("Kopparberg", 4.00, 4)
        self.drink_4 = Drinks("Stella Artois", 5.50, 5)

    def test_pub_has_name(self):
        self.assertEqual("Clansman", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.pub.till)

    # Arranged
    def test_increase_till(self):
        # Act
        self.pub.increase_till(self.drink_1.price)
        # Asserting
        self.assertEqual(510.00, self.pub.till)
