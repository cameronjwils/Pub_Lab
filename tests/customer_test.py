import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
        def setUp(self):
            self.Customer_1 = Customer("Jack Jarvis", 74, 35.00)
            self.Customer_2 = Customer("Victor McDade", 75, 30.00)
            self.Customer_3 = Customer("Winston Ingram", 72, 25.00)
            self.Customer_4 = Customer("Thomas 'Tam' Mullen", 70, 100.00)

        def test_customer_can_reduce_cash(self):
            self.Customer_1.reduce_cash(5.50)
            self.assertEqual(29.50, self.Customer_1.wallet)
