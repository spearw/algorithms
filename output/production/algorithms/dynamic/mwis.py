def mwis(path):

    with open(path) as file:
        lines = file.read().splitlines()

    firstLine = int(lines.pop(0))
    lines_copy = lines.copy()

    subproblems = []
    subproblems.append(0)
    subproblems.append(int(lines.pop(0)))

    for i, line in enumerate(lines):
        subproblems.append(max(subproblems[-1], subproblems[-2] + int(line)))

    max_sum = subproblems[-1]

    chosen_points = []
    included = []

    # try lines_copy next
    i = len(subproblems) - 1

    while i >= 1:

        if subproblems[(i - 1)] >= subproblems[(i - 2)] + int(lines_copy[i - 1]):
            i -= 1
        else:
            chosen_points.append(lines_copy[i - 1])
            included.append(i)
            i -= 2

    return included, chosen_points, max_sum


print(mwis("mwis_test.txt"))
included, chosen_points, max_sum = mwis("mwis_test2.txt")
print(included)

included, chosen_points, max_sum = mwis("mwis.txt")
print(included)

print(1 in included)
print(2 in included)
print(3 in included)
print(4 in included)
print(17 in included)
print(117 in included)
print(517 in included)
print(997 in included)
