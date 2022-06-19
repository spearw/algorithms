import heapq
from statistics import mean


def medianMaintenance(path):

    with open(path) as file:
        lines = file.read().splitlines()

    highHeap = []
    lowHeap = []

    heapq.heapify(highHeap)
    heapq.heapify(lowHeap)

    medians = []

    for line in lines:

        # Add new line to heaps dependant on value
        if not highHeap:
            heapq.heappush(highHeap, int(line))
        elif int(line) > int(heapq.nsmallest(1, highHeap)[0]):
            heapq.heappush(highHeap, int(line))
        else:
            heapq.heappush(lowHeap, int(line) * -1)

        # Balance Heap sizes
        highHeaplen = len(highHeap)
        lowHeaplen = len(lowHeap)

        if highHeaplen == lowHeaplen:
            median = heapq.nsmallest(1, lowHeap)[0] * -1

            # problem doesn't ask for true median - asks for smaller value
            # median = mean([heapq.nsmallest(1, highHeap)[0], heapq.nsmallest(1, lowHeap)[0] * -1])
        elif highHeaplen == lowHeaplen + 1:
            median = heapq.nsmallest(1, highHeap)[0]
        elif highHeaplen + 1 == lowHeaplen:
            median = heapq.nsmallest(1, lowHeap)[0] * -1
        elif highHeaplen < lowHeaplen:
            heapq.heappush(highHeap, (heapq.heappop(lowHeap) * -1))
            median = heapq.nsmallest(1, lowHeap)[0] * -1

            # median = mean([heapq.nsmallest(1, highHeap)[0], heapq.nsmallest(1, lowHeap)[0] * -1])
        elif highHeaplen > lowHeaplen:
            heapq.heappush(lowHeap, (heapq.heappop(highHeap) * -1))

            median = heapq.nsmallest(1, lowHeap)[0] * -1

            # median = mean([heapq.nsmallest(1, highHeap)[0], heapq.nsmallest(1, lowHeap)[0] * -1])

        medians.append(median)

    return medians


print(medianMaintenance("medianMaintenanceTest1.txt"))
print(medianMaintenance("medianMaintenanceTest2.txt"))

print(sum(medianMaintenance("medianMaintenanceTest1.txt")))
print(sum(medianMaintenance("medianMaintenanceTest2.txt")))
print(sum(medianMaintenance("medianMaintenance.txt")))
