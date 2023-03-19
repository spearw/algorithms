def twoSum(path, bounds):

    print(bounds)

    with open(path) as file:
        lines = file.read().splitlines()

    dictionary = {}
    for line in lines:
        dictionary[int(line)] = int(line)

    count = 0

    targets = range(bounds[0], bounds[1] + 1)

    for target in targets:
        for value in dictionary:
            if (target - value) in dictionary:
                count += 1
                break
    return count


print(twoSum("2-SUM-test.txt", [3, 10]))
print(twoSum("2-SUM.txt", [-10000, 10000]))
