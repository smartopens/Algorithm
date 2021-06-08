import heapq


def dikstra(start):
    data_heap = []
    distances[start] = 0
    heapq.heappush(data_heap, (0, start))

    while data_heap:
        dist, now = heapq.heappop(data_heap)

        if distances[now] < dist:
            continue

        for i in array[now]:
            cost = dist + i[1]

            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(data_heap, (cost, i[0]))


test_case = int(input())

for _ in range(test_case):
    n, d, c = map(int, input().split(' '))

    array = [[] for _ in range(n + 1)]
    distances = [1e9] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        array[b].append((a, s))

    dikstra(c)
    count = 0
    distance = 0

    for i in distances:
        if i != 1e9:
            count += 1
            if i > distance:
                distance = i

    print(count, distance)
