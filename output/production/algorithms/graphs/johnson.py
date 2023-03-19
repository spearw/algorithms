import os
from graphs.bellman_ford import bellman_ford
from graphs.dijkstra import dijkstra
from shutil import copyfile

#TODO: returns negative edge length if input file contains empty line. Handle empty line
def johnson(path):

    # create file with ghost node from pathfile
    base, ext = os.path.splitext(path)
    temp_file_path = base+"_temp"+ext
    reweighted_file_path = base+"_reweight"+ext

    with open(path) as f:
        lines = f.readlines()

    num_vertices, num_edges = lines[0].split()
    ghost_vertex = int(num_vertices) + 1
    new_lines = lines.copy()
    new_lines[0] = str(ghost_vertex) + " " + num_edges + "\n"

    with open(temp_file_path, "w") as f:
        f.writelines(new_lines)
        for i in range (ghost_vertex):
            f.write("\n" + str(ghost_vertex) + " " + str(i) + " 0")

    # run single invocation of bellman-ford with ghost node, excluding path for ghost node
    weights = bellman_ford(temp_file_path, ghost_vertex)
    if not weights:
        # return False if negative cycle
        os.remove(temp_file_path)
        return False

    weights = weights[:-1]
    print(f"Weights: {weights}")
    print(f"Smallest weight: {min(weights)}")

    # reweight edges using those values
    with open (reweighted_file_path, "w") as f:
        f.write(lines.pop(0))
        for line in lines:
           head, tail, cost = line.split()
           reweighted_cost = str(int(cost) + weights[int(head) - 1] - weights[int(tail) - 1])
           f.write(f"{head} {tail} {reweighted_cost}\n")

    # run dijkstra for all edges
    weighted_shortest_paths = {}
    for i in range(1, int(num_vertices) + 1):
        weighted_shortest_paths[i] = dijkstra(reweighted_file_path, i)
        print(weighted_shortest_paths[i])

    # recalculate real shortest paths
    all_shortest_paths = {}
    for source_vertex in weighted_shortest_paths:
        head_weight = weights[source_vertex - 1]
        source_paths = []
        for sink_vertex in weighted_shortest_paths[source_vertex]:
            tail_weight = weights[sink_vertex[0] - 1]
            path_length = sink_vertex[1] - head_weight + tail_weight
            source_paths.append([sink_vertex[0], path_length])

        all_shortest_paths[source_vertex] = source_paths

    # clean up files
    os.remove(temp_file_path)
    os.remove(reweighted_file_path)

    # return all shortest paths
    return all_shortest_paths

if __name__ == "__main__":
    print(johnson("dat/all_pair_shortest_paths/g1.txt"))
