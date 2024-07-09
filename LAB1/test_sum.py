import unittest
from sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        input_data=[1,1,1,1,1];
        result=sum(input_data)
        self.assertEqual(result,5)
        
    def test_empty(self):
        input_data=[];
        result=sum(input_data)
        self.assertEqual(result,0)

if __name__=='__main__':
    unittest.main()