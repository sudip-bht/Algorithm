import unittest
from selectionsort import selection_sort;

class TestInsertion(unittest.TestCase):
    
    def test_descending(self):
        input_data=[5,4,3,2,1]
        sortedarray=selection_sort(input_data)
        self.assertListEqual(sortedarray,[1,2,3,4,5])
    
    def test_ascending(self):
        input_data=[1,2,3,4,5]
        sortedarray=selection_sort(input_data)
        self.assertListEqual(sortedarray,[1,2,3,4,5])

    def test_empty(self):
        input_data=[];
        sortedarray=selection_sort(input_data)
        self.assertListEqual(sortedarray,[])
    
    def test_sorting(self):
        input_data=[1,10,5,2,3,8,6,9];
        sortedarray=selection_sort(input_data)
        self.assertListEqual(sortedarray,[1,2,3,5,6,8,9,10])

if __name__=='__main__':
    unittest.main()