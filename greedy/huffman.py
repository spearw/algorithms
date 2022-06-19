import heapq
import sys


def huffman(path):

    with open(path) as file:
        lines = file.read().splitlines()

    firstLine = int(lines.pop(0))

    if firstLine < 2000:
        sys.setrecursionlimit(firstLine + 3)
    else:
        return None

    heap = []
    merges = {}

    for i, line in enumerate(lines):
        tuple = (int(line), str(i))
        heap.append(tuple)

    heapq.heapify(heap)
    return combine(heap, merges)


def combine(heap, merges):

    min1 = heapq.heappop(heap)
    min2 = heapq.heappop(heap)

    keys = min1[1].split(",")
    for key in keys:
        length = merges.get(key, 0)
        length += 1
        merges[key] = length

    keys = min2[1].split(",")
    for key in keys:
        length = merges.get(key, 0)
        length += 1
        merges[key] = length

    tuple = (min1[0] + min2[0], min1[1] + "," + min2[1])
    heapq.heappush(heap, tuple)

    if len(heap) > 1:
        return combine(heap, merges)

    return heap, merges


print(huffman("huffman-test(min2,max5).txt"))
print(huffman("huffman-test2(min3,max6).txt"))

heap, merges = huffman("huffman.txt")

l = list(merges.values())
print(l[0])
print(l[-1])
