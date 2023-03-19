import unittest
from tsp_heuristic import tsp_heuristic as tsp

class TestStringMethods(unittest.TestCase):

    def test_tsp(self):
        self.assertEqual(tsp.tsp(tsp.calc_euclidean_distances("dat/tsp/t1.txt")), 10.24)

if __name__ == '__main__':
    unittest.main()