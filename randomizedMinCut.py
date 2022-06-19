import random
import copy


def randomEdgeSelection(nodes):

    node = random.choice(nodes)
    connection = random.choice(node[1:])
    edge = [node[0], connection]
    print(edge)
    return edge


def randomizedContraction(nodes):

    mergedGraph = copy.deepcopy(nodes)
    while True:
        mergedGraph = randomMerge(mergedGraph)
        if len(mergedGraph) == 2:
            break
    print(mergedGraph)
    return mergedGraph


def randomMerge(nodes):

    newNodes = []
    edge = randomEdgeSelection(nodes)
    supernode = None
    mergingnode = None

    for node in nodes:
        if node[0] == edge[0]:
            supernode = node
        elif node[0] == edge[1]:
            mergingnode = node
        else:
            # change pointers to supernode
            newNode = []
            for connection in node:
                if connection == edge[1]:
                    connection = edge[0]
                newNode.append(connection)
            newNodes.append(newNode)

    print(supernode, mergingnode)
    while edge[1] in supernode:
        supernode.remove(edge[1])
    for connection in mergingnode[1:]:
        if connection == supernode[0]:
            continue
        else:
            supernode.append(connection)
    print(supernode)

    newNodes.append(supernode)
    print(newNodes)
    return newNodes


def iterateContraction(nodes, iteration):
    minCuts = []
    for i in range(iteration):
        cut = len(randomizedContraction(nodes)[0]) - 1
        minCuts.append(cut)
    return min(minCuts)


with open("kargerMinCut.txt") as f:
    lines = f.read().splitlines()
    nodes = []
    for line in lines:
        nodes.append(line.split())

    print(nodes)
    print(iterateContraction(nodes, 8 * len(nodes)))
