import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
        def setUp(self):
            self.Customer_1 = Customers("Jack Jarvis", 35.00)
            self.Customer_2 = Customers("Victor McDade", 30.00)
            self.Customer_3 = Customers("Winston Ingram", 25.00)
            self.Customer_4 = Customers("Thomas 'Tam' Mullen", 100.00)