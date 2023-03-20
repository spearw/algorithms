import unittest
from tsp.python.tsp_heuristic import tsp_heuristic as tsp

class TestStringMethods(unittest.TestCase):

    def test_tsp(self):
        self.assertEqual(tsp("dat/tsp_heuristic/t1.txt"), [1, 3, 2, 5, 6, 4, 1])

if __name__ == '__main__':
    unittest.main()