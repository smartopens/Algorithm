n, m = map(int, input().split(' '))


def dfs(v):
    visited[v] = True

    for e in array[v]:
        if not (visited[e]):
            dfs(e)


array = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split(' '))
    array[x].append(y)
    array[y].append(x)

count = 0
for i in range(1, n + 1):

    if not (visited[i]):
        dfs(i)
        count += 1

print(count)
