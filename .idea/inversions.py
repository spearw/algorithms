import unittest


def findInversions(a):

    if len(a) == 1:
        return 0

    leftHalf = a[: len(a) // 2]
    rightHalf = a[len(a) // 2 :]

    inversions = findSplitInversions(leftHalf, rightHalf)
    inversions = inversions + findInversions(leftHalf)
    inversions = inversions + findInversions(rightHalf)

    return inversions


def findSplitInversions(leftHalf, rightHalf):

    inversions = 0
    length = len(leftHalf) + len(rightHalf)
    output = []
    i = 0
    j = 0

    for k in range(length):
        if leftHalf[i] < rightHalf[j]:
            output.append(leftHalf[i])
            i += 1
            if i == len(leftHalf):
                return inversions
        else:
            output.append(rightHalf[j])
            j += 1
            if len(leftHalf) > 1:
                inversions = inversions + len(leftHalf[i - 1 : -1])
            else:
                inversions = inversions + 1
            if j == len(rightHalf):
                return inversions

    return inversions


class MultiplyTest(unittest.TestCase):
    def testNoInversions(self):
        self.assertEqual(findInversions([1, 2, 3, 4, 5, 6]), 0)

    def testOneSplitInversion(self):
        self.assertEqual(findInversions([2, 1]), 1)

    def testOneSplitInversionWithLargerList(self):
        self.assertEqual(findInversions([1, 2, 4, 3, 5, 6]), 1)

    def testLeftSideInversion(self):
        self.assertEqual(findInversions([1, 3, 2, 4, 5, 6]), 1)

    def testRightSideInversion(self):
        self.assertEqual(findInversions([1, 2, 3, 5, 4, 6]), 1)

    def testLargeSplitInversions(self):
        self.assertEqual(findInversions([1, 3, 4, 2, 5, 6]), 2)

    def testMultipleInversions(self):
        self.assertEqual(findInversions([1, 4, 3, 2, 5, 6]), 3)


with open("../inversions-file.txt") as f:
    lines = f.read().splitlines()
    print(findInversions(lines))
