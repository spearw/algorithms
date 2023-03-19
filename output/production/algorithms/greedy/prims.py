import unittest


def prims(path):

    with open(path) as file:
        lines = file.read().splitlines()

    firstLine = lines.pop(0)
    nodes = {}

    for line in lines:
        splitline = line.split()
        nodeId = splitline[0]
        path = splitline[1]
        length = splitline[2]

        node = nodes.get(int(nodeId), [])
        node.append([int(path), int(length)])
        nodes[int(nodeId)] = node

        node2 = nodes.get(int(path), [])
        node2.append([int(nodeId), int(length)])
        nodes[int(path)] = node2

    V = list(range(1, int(firstLine.split()[0]) + 1))
    X = [1]
    T = []
    cost = 0

    print(nodes)

    for edge in nodes[1]:
        T.append(edge)

    while X != V:
        minLength = None
        nextEdge = None
        for e in T:
            if minLength is None:
                if e[0] in X:
                    continue
                else:
                    minLength = e[1]
                    nextEdge = e[0]
            elif e[1] < minLength:
                if e[0] in X:
                    continue
                minLength = e[1]
                nextEdge = e[0]

        cost = cost + minLength
        X.append(nextEdge)
        X.sort()

        if nextEdge in nodes:
            for edge in nodes[nextEdge]:
                T.append(edge)

    return cost


print(prims("prims.txt"))
print(prims("prims_test.txt"))
print(prims("prims_test2.txt"))

# class primsTest(unittest.TestCase):
#     def firstCaseSubtraction(self):
#         self.assertEqual(prims("prims_test.txt"), 3)
#
#     def firstCaseRatio(self):
#         self.assertEqual(prims("prims_test2.txt"), 7)
