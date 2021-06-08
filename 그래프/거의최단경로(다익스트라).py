import heapq
from collections import deque


def dikstra():
    heap = []
    heapq.heappush(heap, (0, s))
    distances[s] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + graph[now][i]

            if distances[i] > cost:
                distances[i] = cost
                heapq.heappush(heap, (cost, i))


def bfs():
    q = deque([d])

    while q:
        v = q.popleft()

        if v == s:
            continue

        for prev_v, prev_c in re_graph[v]:

            if distances[prev_v] + graph[prev_v][v] == distances[v]:
                if (prev_v, v) not in reverse_list:
                    reverse_list.append((prev_v, v))
                    q.append(prev_v)


while True:
    n, m = map(int, input().split(' '))
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split(' '))

    graph = [dict() for _ in range(n)]
    re_graph = [[] for _ in range(n)]

    for _ in range(m):
        x, y, cost = map(int, input().split(' '))
        graph[x][y] = cost
        re_graph[y].append((x, cost))

    distances = [1e9] * (n)
    reverse_list = list()
    dikstra()
    bfs()

    for pre_v, v in reverse_list:
        del graph[pre_v][v]

    distances = [1e9] * (n)
    dikstra()

    if distances[d] == 1e9:
        print(-1)
    else:
        print(distances[d])
