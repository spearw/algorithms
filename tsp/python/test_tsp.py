import unittest
from tsp import euclidean_tsp as tsp

class TestStringMethods(unittest.TestCase):

    def test_tsp(self):
        self.assertEqual(tsp.tsp(tsp.calc_euclidean_distances("dat/tsp/t1.txt")), 10.24)
        self.assertEqual(tsp.tsp(tsp.calc_euclidean_distances("dat/tsp/t2.txt")), 12.36)
        self.assertEqual(tsp.tsp(tsp.calc_euclidean_distances("dat/tsp/t3.txt")), 14.0)

if __name__ == '__main__':
    unittest.main()