import math

def tsp_heuristic(path):
    with open(path) as file:
        remaining_cities = file.read().splitlines()

    num_cities = int(remaining_cities.pop(0))

    first_city = [0, remaining_cities.pop(0)]

    current_city = first_city
    path = [1]
    pathlength = 0.0

    while len(remaining_cities) > 0:
        current_city = find_closest_city(current_city[1], remaining_cities)
        remaining_cities.remove(current_city[1])
        path.append(int(current_city[1].split(' ')[0]))
        pathlength += current_city[0]

    current_city = find_closest_city(current_city[1], [first_city[1]])
    path.append(int(current_city[1].split(' ')[0]))
    pathlength += current_city[0]

    print(path)
    return math.floor(pathlength)

def find_closest_city(current_city, remaining_cities):
    distances = {}
    cord1 = tuple(map(float, current_city.split(' ')))
    for city in remaining_cities:
        cord2 = tuple(map(float, city.split(' ')))
        distances[cord2[0]] = [math.dist(cord1[1:], cord2[1:]), city]
    next_city = min(distances, key=distances.get)
    return distances[next_city]

if __name__ == "__main__":
    # print(tsp(calc_euclidean_distances("dat/tsp/tsp.txt")))
    print(tsp_heuristic("dat/tsp_heuristic/nn.txt"))
