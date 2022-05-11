import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Clansman", 500.00)

    def test_pub_has_name(self):
        self.assertEqual("Clansman", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500.00, self.pub.till)

    # Arranged
    def test_increase_till(self):
        # Act
        self.pub.increase_till(2.50)
        # Asserting
        self.assertEqual(102.50, self.pub.till)
