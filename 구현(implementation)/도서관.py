import heapq

n, m = map(int, input().split(' '))

array = list(map(int, input().split(' ')))

positives = []
negatives = []

largest = max(max(array), -min(array))

for i in array:

    if i > 0:
        heapq.heappush(positives, -i)
    else:
        heapq.heappush(negatives, i)

result = 0

while positives:
    result += heapq.heappop(positives)

    for _ in range(m - 1):
        if positives:
            heapq.heappop(positives)

while negatives:
    result += heapq.heappop(negatives)

    for _ in range(m - 1):
        if negatives:
            heapq.heappop(negatives)

print(result * -2 - largest)
