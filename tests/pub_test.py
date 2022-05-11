import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Clansman", 500.00)
        self.drink_1 = Drinks("Vodka Martini", 10.00, 40)
        self.drink_2 = Drinks("Mojito", 12.50, 40)
        self.drink_3 = Drinks("Kopparberg", 4.00, 4)
        self.drink_4 = Drinks("Stella Artois", 5.50, 5)
        self.Customer_1 = Customer("Jack Jarvis", 74, 35.00)
        self.Customer_2 = Customer("Victor McDade", 75, 30.00)
        self.Customer_3 = Customer("Winston Ingram", 72, 25.00)
        self.Customer_4 = Customer("Thomas 'Tam' Mullen", 70, 100.00)

    def test_pub_has_name(self):
        self.assertEqual("Clansman", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(self.drink_1.price)
        self.assertEqual(510.00, self.pub.till)
        
    def test_check_age(self):
        result = self.Customer_1.check_age(self.Customer_1.age)
        self.assertEqual(True, result)
