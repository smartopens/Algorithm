import heapq
import sys

input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = [[]*(v+1) for _ in range(v+1)]
distance = [1e9]*(v+1)

def dikstra(s):
    heap = []
    heapq.heappush(heap,(0,s))
    distance[s] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for y, dist_tmp in graph[now]:
            dist2 = dist + dist_tmp
            if distance[y] > dist + dist_tmp:
                distance[y] = dist + dist_tmp
                heapq.heappush(heap, (dist2,y))

    return

for _ in range(e):
    x, y, weight = map(int, input().split())
    graph[x].append((y,weight))

dikstra(k)

for i in range(1,v+1):
    if distance[i] == 1e9:
        print("INF")
        continue

    print(distance[i])

