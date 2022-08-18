import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distances = [0] + [1e9]*(n)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append((y,1))
    graph[y].append((x,1))

def dikstra(s):
    heap = []
    distances[s] = 1
    heapq.heappush(heap,(1,s))

    while heap:
        dist, now = heapq.heappop(heap)

        if distances[now] < dist:
            continue

        for next_node in graph[now]:
            dist2 = dist + next_node[1]
            if dist2 < distances[next_node[0]]:
                distances[next_node[0]] = dist2
                heapq.heappush(heap,(dist2,next_node[0]))

dikstra(1)
max_dist = max(distances)
ans_node = 0
ans_num = 0

for i in range(len(distances)):
    if distances[i] == max_dist:
        ans_node = i
        break

for i in distances:
    if i == max_dist:
        ans_num += 1

print(ans_node, max_dist-1,ans_num)