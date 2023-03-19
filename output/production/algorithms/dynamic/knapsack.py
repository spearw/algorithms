import time


def knapsack(path):

    with open(path) as file:
        lines = file.read().splitlines()

    firstLine = lines[0]

    knapsack_size, number_of_items = firstLine.split(" ")

    knapsack_size = int(knapsack_size)
    number_of_items = int(number_of_items)

    # Nested list is y, x
    A = [[None] * (number_of_items + 1) for i1 in range(knapsack_size + 1)]

    for x in range(0, knapsack_size + 1):
        A[x][0] = 0

    for i in range(1, number_of_items + 1):
        value, weight = lines[i].split(" ")
        # print(value, weight)
        for x in range(0, knapsack_size + 1):
            if int(weight) > x:
                # set to previous value
                A[x][i] = A[x][i - 1]
            else:
                A[x][i] = max(A[x][i - 1], A[x - int(weight)][i - 1] + int(value))

        # for row in A:
        #     print(row)

    return A[knapsack_size][number_of_items]


# print(knapsack("knapsack_test(8).txt"))
start_time = time.time()
print(knapsack("knapsack_test(202).txt"))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(knapsack("knapsack1.txt"))
print("--- %s seconds ---" % (time.time() - start_time))
