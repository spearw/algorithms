from math import dist

def tsp_heuristic(path):
    with open(path) as file:
        remaining_cities = file.read().splitlines()

    num_cities = int(remaining_cities.pop(0))

    current_city = remaining_cities.pop(0)

    for _ in range(num_cities):
        find_closest_city(current_city, remaining_cities)

def find_closest_city(current_city, remaining_cities):
    distances = []
    cord1 = tuple(map(float, current_city.split(' ')))
    for city in remaining_cities:
        cord2 = tuple(map(float, city.split(' ')))
        distances.append(dist(cord1, cord2))
    return min(distances)


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
    print(tsp_heuristic("dat/tsp_heuristic/t1.txt"))
