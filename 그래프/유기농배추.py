import sys

sys.setrecursionlimit(100000)

test_case = int(input())


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
            if array[nx][ny] and not (visited[nx][ny]):
                dfs(nx, ny)
        else:
            continue


for _ in range(test_case):
    m, n, k = map(int, input().split())
    array = [[0] * (m) for _ in range(n)]
    visited = [[False] * (m) for _ in range(n)]
    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        array[y][x] = 1

    for i in range(n):
        for j in range(m):

            if array[i][j] == 1 and not (visited[i][j]):
                dfs(i, j)
                result += 1

    print(result)
