from math import dist
import time

import itertools


def tsp(graph, precision=2):
    start_time = time.time()

    num_cities = len(graph)
    subsets = gen_subsets(num_cities)
    final_path = float('inf')
    paths = [[]]

    # Generate base cases
    paths[0] = list(map(lambda x: [x, 0], graph[0]))

    print(f"Based cases completed in --- {time.time() - start_time} seconds ---")

    # Iterate over increasing path lengths
    for i in range(1, num_cities - 1):

        # Add new path length to paths
        paths.append({})

        # Calculate paths
        for city_set in subsets:
            destination_city = city_set[0]
            for path in city_set:
                if not type(path) == int:
                    if len(path) == i:

                        # take shortest path of all possible ways
                        items = list(map(str, path))
                        permutations_list = list(itertools.permutations(items, len(items)))
                        shortest_path = float('inf')
                        for permutation in permutations_list:
                            try:
                                new_path_length = paths[i-1][int(''.join(map(str, permutation)))][0]
                                end_hop_length = graph[destination_city][int(permutation[0])]
                                shortest_path = min(shortest_path, new_path_length + end_hop_length)
                            except:
                                continue

                        paths[i][int(f"{destination_city}{''.join(map(str, path))}")] = [shortest_path, city_set[0]]
                    elif len(path) > i:
                        # Move on to next city_set
                        pass
        print(f"Path of length {i} completed in --- {time.time() - start_time} seconds ---")

    # Calculate final hop
    for path in paths[-1]:
        final_path = min(final_path, paths[0][int(str(path)[0])][0] + paths[-1][path][0])

    print(f"TSP of {num_cities} cities completed in --- {time.time() - start_time} seconds ---")
    return round(final_path, precision)

def gen_subsets(num_cities):
    all_combinations = []
    # 0 is assumed starter city, thus removed from sets for being special case
    for city in range(1, num_cities):
        combinations = [city]
        city_set = list(range(1, num_cities))
        city_set.remove(city)
        for i in range(1, num_cities):
            for combination in itertools.combinations(city_set, i):
                combinations.append(combination)
        all_combinations.append(combinations)
    return all_combinations

def calc_euclidean_distances(path):

    with open(path) as file:
        lines = file.read().splitlines()

    num_cities = int(lines.pop(0))
    answer = lines.pop()
    all_distances = []
    # Calculate distance between every city, and store in 2-d list
    for line1 in lines:
        distances = []
        for line2 in lines:
            cord1 = tuple(map(float, line1.split(' ')))
            cord2 = tuple(map(float, line2.split(' ')))
            distances.append(dist(cord1, cord2))
        all_distances.append(distances)

    return all_distances


if __name__ == "__main__":
    # print(tsp(calc_euclidean_distances("dat/tsp/tsp.txt")))
    print(tsp(calc_euclidean_distances("dat/tsp/t2.txt")))
