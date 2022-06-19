import unittest


def dijkstra(path):

    with open(path) as file:
        lines = file.read().splitlines()

    nodes = []

    for line in lines:
        nodes.append(line.split())

    processedVertexes = [1]
    # Shortest path from node s to s
    shortestPaths = [[1, 0]]

    while len(processedVertexes) != len(nodes):

        shortestPath = None
        nextNode = None

        for path in shortestPaths:

            node = nodes[path[0] - 1]

            vertexList = node[1:]
            for vertex in vertexList:

                nodeIndex = int(vertex.split(",")[0])
                length = int(vertex.split(",")[1])
                # have I visited this node?
                if nodeIndex in processedVertexes:
                    continue

                possiblePath = path[1] + length

                if shortestPath == None or possiblePath < shortestPath:
                    shortestPath = possiblePath
                    nextNode = nodeIndex

        processedVertexes.append(nextNode)
        shortestPaths.append([nextNode, shortestPath])

    return shortestPaths


def findPathLength(index, allPaths):

    for path in allPaths:
        if path[0] == index:
            return path[1]


print(dijkstra("../dat/graphs/dijkstraTestCase.txt"))

allPaths = dijkstra("../dat/graphs/dijkstraGraph.txt")

print(allPaths)

print(findPathLength(7, allPaths))
print(findPathLength(37, allPaths))
print(findPathLength(59, allPaths))
print(findPathLength(82, allPaths))
print(findPathLength(99, allPaths))
print(findPathLength(115, allPaths))
print(findPathLength(133, allPaths))
print(findPathLength(165, allPaths))
print(findPathLength(188, allPaths))
print(findPathLength(197, allPaths))
