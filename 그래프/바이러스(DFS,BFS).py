from collections import deque

n = int(input())
m = int(input())
array = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)

visited = [False] * (n + 1)


def bfs(v):
    q = deque([v])
    count = -1
    while q:
        v = q.popleft()

        if not (visited[v]):
            visited[v] = True
            count += 1
            for e in array[v]:
                q.append(e)
    print(count)


bfs(1)
