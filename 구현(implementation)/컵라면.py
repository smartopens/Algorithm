import heapq

n = int(input())

array = []
heap = []

for _ in range(n):
    a, b = map(int, input().split(' '))
    array.append((a, b))

array.sort()

for i in array:
    a = i[0]
    heapq.heappush(heap, i[1])

    if a < len(heap):
        heapq.heappop(heap)

print(sum(heap))
