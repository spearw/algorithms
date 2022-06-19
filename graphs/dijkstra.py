
def dijkstra(path, source):

    with open(path) as file:
        lines = file.read().splitlines()

    edges = []

    for line in lines:
        edges.append(line.split())

    num_v_e = edges.pop(0)
    num_vertices = int(num_v_e[0])
    num_edges = int(num_v_e[1])

    # Create and organize nodes by outgoing edges
    vertices = {}

    for edge in edges:
        # get node dict entry, if it exists
        outgoing_edges = vertices.get(int(edge[0]), [])
        outgoing_edges.append([int(edge[1]),int(edge[2])])
        vertices.update({int(edge[0]): outgoing_edges})

    processed_vertices = [source]
    # Shortest path from node s to s
    shortest_paths = [[source, 0]]

    while len(processed_vertices) != num_vertices:

        shortest_path = float('inf')
        next_node = None

        for path in shortest_paths:

            outgoing_edges = vertices.get(path[0])

            for edge in outgoing_edges or []:

                node_index = edge[0]
                weight = edge[1]
                # Check if node has been visited
                if node_index not in processed_vertices:
                    if path[1] + weight < shortest_path:
                        shortest_path = path[1] + weight
                        next_node = node_index

        if next_node is not None:
            processed_vertices.append(next_node)
            shortest_paths.append([next_node, shortest_path])
        else:
            break

    return shortest_paths

if __name__ == "__main__":
    print(dijkstra("dat/all_pair_shortest_paths/example.txt", 1))
