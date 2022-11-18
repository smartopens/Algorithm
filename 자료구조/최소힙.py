import heapq

n = int(input())
result = []
heap = []

for _ in range(n):
    data = int(input())

    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for i in result:
    print(i)
