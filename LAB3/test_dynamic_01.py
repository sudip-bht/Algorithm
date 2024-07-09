import unittest
from  knapsack_dynamic import knapsack_01_dynamic
class TestSum(unittest.TestCase):
        def test_basic(self):
            weights =[10, 20, 30, 40, 50]
            values = [60, 100, 120, 200, 250]
            capacity = 100
            result = knapsack_01_dynamic(weights, values, capacity)
            self.assertEqual(result, (510,[0, 3, 4],))
        def test_all_items_exceed_capacity(self):
            weights = [10, 20, 30, 40, 50]
            values = [60, 100, 120, 200, 250]
            capacity = 9
            result = knapsack_01_dynamic(weights, values, capacity)
            self.assertEqual(result, (0,[])) 
        def test_empty_input(self):
            weights = []
            profits = []
            capacity = 10
            result =knapsack_01_dynamic(weights, profits, capacity)
            self.assertEqual(result, (0,[])) 
        def test_zero_capacity(self):
            weights = [10, 20, 30, 40, 50]
            values = [60, 100, 120, 200, 250]
            capacity = 0
            result = knapsack_01_dynamic(weights, values, capacity)
            self.assertEqual(result, (0,[]))
        def test_negative_capacity(self):
            weights = [10, 20, 30, 40, 50]
            values = [-60, 100, 120, 200, 250]
            capacity = -10
            result = knapsack_01_dynamic(weights, values, capacity)
            self.assertEqual(result, (0,[]))
    
if __name__=='__main__':
    unittest.main()