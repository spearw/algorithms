import unittest


def multiply(x, y, depth=0):
    if (x < 10) and (y < 10):
        print("depth (in calc): " + str(depth))
        return x * y * (10 ** depth)
    else:
        print("int: " + str(x))
        firstDigit = int(str(x)[0])
        restOfNum = int((str(x)[1:]))
        print("first digit: " + str(firstDigit))
        print("rest of num: " + str(restOfNum))
        print("depth: " + str(depth))
        return multiply(firstDigit, y) + multiply(restOfNum, y, depth + 1)


class MultiplyTest(unittest.TestCase):
    def testSingleDigit(self):
        self.assertEqual(multiply(2, 4), 8)

    def testDoubleDigit(self):
        self.assertEqual(multiply(11, 2), 22)

    def testTripleDigit(self):
        self.assertEqual(multiply(111, 2), 222)
