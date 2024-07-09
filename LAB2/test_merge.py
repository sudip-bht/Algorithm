import unittest
from merge import merge_sort

class TestMerge(unittest.TestCase):
    def test_descending(self):
        input_data=[5,4,3,2,1,8]
        merge_sort(input_data,0,len(input_data)-1)
        self.assertListEqual(input_data,[1,2,3,4,5,8])
    def test_ascending(self):
        input_data=[1,2,3,4,5]
        merge_sort(input_data,0,len(input_data)-1)
        self.assertListEqual(input_data,[1,2,3,4,5])

    def test_empty(self):
        input_data=[];
        merge_sort(input_data,0,len(input_data)-1)
        self.assertListEqual(input_data,[])
    def test_sorting(self):
        input_data=[1,10,5,2,3,8,6,9];
        merge_sort(input_data,0,len(input_data)-1)
        self.assertListEqual(input_data,[1,2,3,5,6,8,9,10])

if __name__=='__main__':
    unittest.main()