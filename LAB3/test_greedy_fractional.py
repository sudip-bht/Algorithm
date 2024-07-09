import unittest
from knapsack_greedy import knapsack_fractional_greedy

class TestBruteForceFractional(unittest.TestCase):
    def test_basic(self):
        weights = [10, 20, 30]
        profits = [60, 100, 120]
        capacity = 52
        result =knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result,(232.0,[(0, 0.2), (1, 1), (2, 1)]))

    def test_empty_input(self):
        weights = []
        profits = []
        capacity = 10
        result =knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, (0,[]))

    def test_zero_capacity(self):
            weights = [10, 20, 30, 40, 50]
            values = [60, 100, 120, 200, 250]
            capacity = 0
            result = knapsack_fractional_greedy(weights, values, capacity)
            self.assertEqual(result, (0,[]))

    def test_all_items_exceed_capacity(self):
        weights = [6, 7, 8]
        profits = [5, 6, 7]
        capacity = 5
        result =knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, (4.375,[(2, 0.625)]))

if __name__ == '__main__':
    unittest.main()
