import unittest
from knapsack_bruteforce import knapsack_fractional_bruteforce

class TestBruteForceFractional(unittest.TestCase):
    def test_basic(self):
        weights = [10, 20, 30]
        profits = [60, 100, 120]
        capacity = 50
        result =knapsack_fractional_bruteforce(weights, profits, capacity)
        self.assertEqual(result,(240.0,[(0, 1), (1, 1), (2, 0.6666666666666666)]))

    def test_empty_input(self):
        weights = []
        profits = []
        capacity = 10
        result =knapsack_fractional_bruteforce(weights, profits, capacity)
        self.assertEqual(result, (0,[]))

    def test_zero_capacity(self):
            weights = [10, 20, 30, 40, 50]
            values = [60, 100, 120, 200, 250]
            capacity = 0
            result = knapsack_fractional_bruteforce(weights, values, capacity)
            self.assertEqual(result, (0,[]))

    def test_all_items_exceed_capacity(self):
        weights = [6, 7, 8]
        profits = [5, 6, 7]
        capacity = 5
        result =knapsack_fractional_bruteforce(weights, profits, capacity)
        self.assertEqual(result, (4.375,[(2, 0.625)]))

if __name__ == '__main__':
    unittest.main()
