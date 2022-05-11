import unittest
from src.drinks import Drinks 

class TestDrinks(unittest.TestCase):
        def setUp(self):
            self.drink_1 = Drinks("Vodka Martini", 10.00)
            self.drink_2 = Drinks("Mojito", 12.50)
            self.drink_3 = Drinks("Kopparberg", 4.00)
            self.drink_4 = Drinks("Stella Artois", 5.50)

            drinks = []

