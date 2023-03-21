import unittest
from tsp.python.tsp_heuristic import tsp_heuristic as tsp

class TestStringMethods(unittest.TestCase):

    def test_tsp(self):
        self.assertEqual(tsp("dat/tsp_heuristic/t1.txt"), 15)
        self.assertEqual(tsp("dat/tsp_heuristic/t2.txt"), 2470)
        self.assertEqual(tsp("dat/tsp_heuristic/t3.txt"), 48581)
        self.assertEqual(tsp("dat/tsp_heuristic/t4.txt"), 188129)

if __name__ == '__main__':
    unittest.main()