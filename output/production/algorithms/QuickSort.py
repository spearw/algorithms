import unittest
from statistics import median


def quickSortInversionsCounter(arr, pivotIndex):

    if len(arr) < 2:
        return 0

    pivot = arr[pivotIndex]
    j = 1
    i = 1

    arr[pivotIndex] = arr[0]
    arr[0] = pivot
    for value in arr:
        if value == arr[0]:
            continue
        else:
            if value > pivot:
                # keep i the same, advance j
                j = j + 1
            else:
                # swap element at i with element at j
                tempJ = arr[j]
                arr[j] = arr[i]
                arr[i] = tempJ
                i = i + 1
                j = j + 1
    arr[0] = arr[i - 1]
    arr[i - 1] = pivot

    leftPartition = arr[0 : i - 1]
    if pivotIndex != len(arr):
        rightPartition = arr[i:]

    # print(arr)
    # print(f'left par: {leftPartition}')
    # print(f'right par: {rightPartition}')
    count = len(arr) - 1
    count = count + quickSortInversionsCounter(leftPartition, pivotIndex)
    count = count + quickSortInversionsCounter(rightPartition, pivotIndex)

    return count


def medianPivotQuickSortInversionsCounter(arr):

    if len(arr) < 2:
        return 0

    if len(arr) % 2 == 0:
        potentialPivots = [arr[0], arr[int((len(arr) / 2) - 1)], arr[-1]]
    else:
        potentialPivots = [arr[0], arr[int((len(arr) / 2))], arr[-1]]
    pivotIndex = arr.index(median(potentialPivots))

    pivot = arr[pivotIndex]
    j = 1
    i = 1

    arr[pivotIndex] = arr[0]
    arr[0] = pivot
    for value in arr:
        if value == arr[0]:
            continue
        else:
            if value > pivot:
                # keep i the same, advance j
                j = j + 1
            else:
                # swap element at i with element at j
                tempJ = arr[j]
                arr[j] = arr[i]
                arr[i] = tempJ
                i = i + 1
                j = j + 1
    arr[0] = arr[i - 1]
    arr[i - 1] = pivot

    leftPartition = arr[0 : i - 1]
    if pivotIndex != len(arr):
        rightPartition = arr[i:]

    # print(arr)
    # print(f'left par: {leftPartition}')
    # print(f'right par: {rightPartition}')
    count = len(arr) - 1
    count = count + medianPivotQuickSortInversionsCounter(leftPartition)
    count = count + medianPivotQuickSortInversionsCounter(rightPartition)

    return count


class ComparisonsTest(unittest.TestCase):
    def testSingleFirstIndex(self):
        self.assertEqual(0, quickSortInversionsCounter([1], 0))

    def testDoubleFirstIndex(self):
        self.assertEqual(1, quickSortInversionsCounter([0, 1], 0))

    def testVideoExampleSortFirstIndex(self):
        self.assertEqual(15, quickSortInversionsCounter([3, 8, 2, 5, 1, 4, 7, 6], 0))

    def testsinglelastindex(self):
        self.assertEqual(0, quickSortInversionsCounter([1], -1))

    def testDoubleLastIndex(self):
        self.assertEqual(1, quickSortInversionsCounter([0, 1], -1))

    def testVideoExampleSortLastIndex(self):
        self.assertEqual(15, quickSortInversionsCounter([3, 8, 2, 5, 1, 4, 7, 6], -1))

    def testDoubleMedianIndex(self):
        self.assertEqual(1, medianPivotQuickSortInversionsCounter([0, 1]))

    def testVideoExampleMedianIndex(self):
        self.assertEqual(
            13, medianPivotQuickSortInversionsCounter([3, 8, 2, 5, 1, 4, 7, 6])
        )


with open("QuickSort.txt") as f:
    lines = f.read().splitlines()
    print(quickSortInversionsCounter(lines, 0))
    print(quickSortInversionsCounter(lines, -1))
    print(medianPivotQuickSortInversionsCounter(lines))
