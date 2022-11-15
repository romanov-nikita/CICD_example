import unittest
from Accountant import *


class Test(unittest.TestCase):
    def test_income(self):
        acc = Accountant()
        value = 1000
        acc.set_income(value)
        self.assertEqual(acc.get_income(), value)
        self.assertEqual(acc.get_summary(), value)

    def test_outcome(self):
        acc = Accountant()
        value = 1000
        acc.set_outcome(value)
        self.assertEqual(acc.get_outcome(), value)
        self.assertEqual(acc.get_summary(), -1 * value)
