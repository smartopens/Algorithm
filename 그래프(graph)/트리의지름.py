from collections import deque

n = int(input())


def bfs(start):
    q = deque([start])
    visited = [-1] * (n + 1)
    visited[start] = 0
    max_d_n = [0, 0]

    while q:
        x = q.popleft()

        for y, w in arr[x]:
            if visited[y] == -1:
                visited[y] = visited[x] + w
                q.append(y)
                if max_d_n[0] < visited[y]:
                    max_d_n[0], max_d_n[1] = visited[y], y

    return max_d_n


arr = [[] for _ in range(n + 1)]

for _ in range(n):
    info = list(map(int, input().split()))

    for i in range(0, len(info) - 3, 2):
        arr[info[0]].append((info[i + 1], info[i + 2]))

dist, node = bfs(1)
dist, node = bfs(node)
print(dist)
