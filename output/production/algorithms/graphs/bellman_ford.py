
def bellman_ford(path, source):

    print("Starting Bellman-Ford")

    edges = []

    with open(path) as file:
        lines = file.read().splitlines()

    for line in lines:
        edges.append(line.split())

    num_v_e = edges.pop(0)
    num_vertices = int(num_v_e[0])
    num_edges = int(num_v_e[1])
    # create empty array with size equal to num vertices + 1 because of the lack of a 0 index in vertices
    # note that index 0 will always remain empty
    incoming_edges = [[] for i in range(num_vertices + 1)]
    print("Created edges")

    for edge in edges:
        ## Take node at head of edge and add it to an array for constant lookup of incoming edge lengths and nodes
        #Append to existing entry
        vertex = incoming_edges[int(edge[1])]
        if vertex != 0:
            vertex.append([edge[0], edge[2]])
        else:
            #Create new entry
            vertex = [edge[0], edge[2]]
        incoming_edges[int(edge[1])] = vertex

    a = [[float('inf') for i in range(num_vertices + 1)] for v in range(num_edges)]

    print("Completed setup")

    # Set up base case
    for i, v in enumerate(a[0]):
        if (i == source):
            a[0][i] = 0

    print("Completed base case")

    for i in range(1, num_edges):
        for v in range(num_vertices + 1):

            min_incoming = min(list(map(lambda x: int(x[1]) + a[i-1][int(x[0])], incoming_edges[v])), default=float('inf'))
            a[i][v] = min(a[i-1][v],
                          min_incoming)

        # Check improvement - break if same as previous
        if a[i] == a[i-1]:
            final_edge_score = i
            break
        if i % 1000 == 0: print(f"Completed paths with {i} edges")

    final_edge_score = i

    # Check for negative cycle, return false if detected
    for i, p in enumerate(a[final_edge_score]):
        if (a[final_edge_score][i] < a[final_edge_score - 1][i]):
            return False

    # Return final row, excluding 0th index vertex (which doesn't exist)
    return a[final_edge_score][1:]



if __name__ == "__main__":
    # print(bellman_ford("dat/all_pair_shortest_paths/example.txt", 1))
    print(bellman_ford("dat/all_pair_shortest_paths/negative_cycle.txt", 1))
