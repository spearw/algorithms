from math import dist

def tsp_heuristic(path):
    with open(path) as file:
        remaining_cities = file.read().splitlines()

    num_cities = int(remaining_cities.pop(0))

    # Grab first line, convert to tuple
    current_city = tuple(map(float, remaining_cities.pop(0).split(' ')))
    path = [1]

    while len(remaining_cities) > 0:
        current_city = find_closest_city(current_city, remaining_cities)
        remaining_cities.remove(f"{int(current_city[0])} {current_city[1]} {current_city[2]}")
        path.append(int(current_city[0]))

    path.append(1)
    return path

def find_closest_city(current_city, remaining_cities):
    distances = {}
    cord1 = current_city
    for city in remaining_cities:
        cord2 = tuple(map(float, city.split(' ')))
        distances[cord2[0]] = [dist(cord1[1:], cord2[1:]), cord2]
    next_city = min(distances, key=distances.get)
    return distances[next_city][1]


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
