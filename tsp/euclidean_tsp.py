import time

from math import dist

import itertools


def tsp(graph, precision=2):
    start_time = time.time()
    num_cities = len(graph)
    subsets = gen_subsets(num_cities)
    final_path = float('inf')
    paths = [[]]

    # Generate base cases
    for i in range(0, num_cities):
        paths[0].append([graph[0][i], 0])

    print("Base cases completed")

    # Iterate over increasing path lengths
    for i in range(1, num_cities - 1):

        # Add new path length to paths
        paths.append({})

        # Calculate paths for each increasing length, starting with length 1
        for path_set in subsets:
            # Skip placeholder set
            if len(path_set) == 0:
                continue
            for route in path_set:
                destination_city = route[0]
                path = route[1]

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

                paths[i][int(f"{destination_city}{''.join(map(str, path))}")] = [shortest_path, path_set[0]]

        print(f"Paths of length {i} calculations completed")

    # Calculate final hop
    for path in paths[-1]:
        final_path = min(final_path, paths[0][int(str(path)[0])][0] + paths[-1][path][0])

    print("--- %s seconds ---" % (time.time() - start_time))
    return round(final_path, precision)

def gen_subsets(num_cities):
    #TODO: gen better. Should be sorted by len, so can just grab the appropriate parts. Sort combinations as they come out into final buckets based on size
    all_combinations = []
    for i in range(num_cities):
        all_combinations.append([])
    # 0 is assumed starter city, thus removed from sets for being special case
    for city in range(1, num_cities):
        combinations = [city]
        city_set = list(range(1, num_cities))
        city_set.remove(city)
        for i in range(1, num_cities):
            for combination in itertools.combinations(city_set, i):
                all_combinations[len(combination)].append([city, combination])
    return all_combinations

def calc_euclidean_distances(path):

    with open(path) as file:
        lines = file.read().splitlines()

    num_cities = int(lines.pop(0))
    print(f"Number of cities: {num_cities}")
    answer = lines.pop()
    print(f"Answer: {answer}")
    all_distances = []
    # Calculate distance between every city, and store in 2-d list
    for line1 in lines:
        distances = []
        for line2 in lines:
            cord1 = tuple(map(float, line1.split(' ')))
            cord2 = tuple(map(float, line2.split(' ')))
            distances.append(dist(cord1, cord2))
        all_distances.append(distances)

    print(f"distances: {all_distances}")
    return all_distances


if __name__ == "__main__":
    print(tsp(calc_euclidean_distances("dat/tsp/tsp.txt")))
