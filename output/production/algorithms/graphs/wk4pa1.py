from graphs.johnson import johnson

def smallest_path(path):
    shortest_path = float('inf')
    all_paths = johnson(path)
    if not all_paths: return False
    for vertex in all_paths:
        for path in all_paths[vertex]:
            shortest_path = min(path[1],
                                shortest_path)
    return shortest_path

if __name__ == "__main__":
    print(smallest_path("dat/all_pair_shortest_paths/input_random_14_16.txt"))
    # print(smallest_path("dat/all_pair_shortest_paths/g1.txt"))
    # print(smallest_path("dat/all_pair_shortest_paths/g2.txt"))
    print(smallest_path("dat/all_pair_shortest_paths/g3.txt"))
