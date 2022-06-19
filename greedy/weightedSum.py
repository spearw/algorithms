import unittest


def weightedSum(path, ratio=True):

    with open(path) as file:
        lines = file.read().splitlines()

    numberOfJobs = lines.pop(0)

    jobs = []

    for line in lines:
        splitline = line.split()
        weight = splitline[0]
        length = splitline[1]

        if ratio:
            jobs.append([float(weight) / float(length), int(weight), int(length)])
        else:
            jobs.append([float(weight) - float(length), int(weight), int(length)])

    jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)

    lines.sort(key=lambda x: (x[0], x[1]), reverse=True)

    weightedCompletionTimes = []
    completionTime = 0

    for job in jobs:

        completionTime = completionTime + job[2]
        weightedCompletionTime = completionTime * job[1]
        weightedCompletionTimes.append(weightedCompletionTime)

    return sum(weightedCompletionTimes)


print(weightedSum("jobs.txt", ratio=False))
print(weightedSum("jobs.txt", ratio=True))
# print(weightedSum("jobs_test.txt", ratio=False))
# print(weightedSum("jobs_test.txt", ratio=True))
# print(weightedSum("jobs_test2.txt", ratio=False))
# print(weightedSum("jobs_test2.txt", ratio=True))


class SumTest(unittest.TestCase):
    def firstCaseSubtraction(self):
        self.assertEqual(weightedSum("jobs_test.txt", ratio=False), 68615)

    def firstCaseRatio(self):
        self.assertEqual(weightedSum("jobs_test.txt", ratio=True), 67247)

    def secondCaseSubtraction(self):
        self.assertEqual(weightedSum("jobs_test2.txt", ratio=False), 32780)

    def secondCaseRatio(self):
        self.assertEqual(weightedSum("jobs_test2.txt", ratio=True), 32104)
