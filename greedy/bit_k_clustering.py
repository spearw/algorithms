import networkx.utils
from bitarray import bitarray

# Given list nodes separated by their Hamming distance, what is the largest value of k clusters such that there is a k-clustering with spacing of at least 3?
# Grab smallest separated point until edge is larger than 3, then calculate number of clusters
# Points should be presorted with bitmasks
# Cluster number will be equal to how many separated points are left

# hints
# https://www.coursera.org/learn/algorithms-greedy/discussions/weeks/2/threads/mSGCyQULEemZUwrw3z8SgA
# https://www.coursera.org/learn/algorithms-greedy/discussions/weeks/2/threads/MIX9reZ8EeeorRLf5gxw3A
# https://www.coursera.org/learn/algorithms-greedy/discussions/weeks/2/threads/zv_iBPH7Eeamuwo9wEiniA

def bitmasks(n,m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield bitarray([1]) + x
            for x in bitmasks(n-1,m):
                yield bitarray([0]) + x
        else:
            yield n * bitarray('0')
    else:
        yield n * bitarray('1')

path = "clustering_big.txt"

with open(path) as file:
    lines = file.read().splitlines()

first_line = lines.pop(0).split()
node_number = first_line[0]
bit_number = first_line[1]

nodes = []
unique_nodes = {}

# for i, line in enumerate(lines):
#     b_int = int(line.replace(" ", ""), 2)
#     nodes.append(b_int)
#
#     node = unique_nodes.get(b_int, [])
#     node.append(i)
#     unique_nodes[b_int] = node

# Create union find instance

# Create an array of bit-masks
bitmask_zero = [0]
for b in bitmasks(24, 0):
    bitmask_zero.append(b)
print(bitmask_zero)

bitmask_one = []
for b in bitmasks(24, 1):
    bitmask_one.append(b)
print(bitmask_one)

bitmask_two = []
for b in bitmasks(24, 2):
    bitmask_two.append(b)

print(bitmask_two)

bitmasks = [bitmask_zero[1]] + bitmask_one + bitmask_two

print(bitmasks)

# Iterate over distances & XOR each key with the distance
