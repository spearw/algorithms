import time


def knapsack(path):

    with open(path) as file:
        lines = file.read().splitlines()

    firstLine = lines[0]

    knapsack_size, number_of_items = firstLine.split(" ")

    knapsack_size = int(knapsack_size)
    number_of_items = int(number_of_items)

    # Previous item
    A = [0 for i in range(knapsack_size + 1)]

    for i in range(1, number_of_items + 1):

        # Current Item
        B = []

        value, weight = lines[i].split(" ")
        weight = int(weight)
        value = int(value)
        for x in range(0, knapsack_size + 1):
            if weight > x:
                # set to previous item value
                B.append(A[x])
            else:
                # bigger of previous item and current item + smaller previous solution
                B.append(max(A[x], (A[x - weight]) + value))

        # copying array probably takes a long time. O(n) time to copy turns into O(n^2) when I do it every iteration
        A = B

    return B[-1]


# print(knapsack("knapsack_test(8).txt"))

start_time = time.time()
print(knapsack("knapsack_test(202).txt"))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
# 2493893
print(knapsack("knapsack1.txt"))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
# 4243395
print(knapsack("knapsack_big.txt"))
print("--- %s seconds ---" % (time.time() - start_time))
