import unittest
from matrix import *

class Teste_length(unittest.TestCase):

    def test_sizee(self):
        arr = [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual(size(arr), 10)

    def test_sumArray(self):
        arr = [1,2,3,4]
        self.assertEqual(sumArray(arr), 10)

    



if __name__=="__main__":
    unittest.main()
        