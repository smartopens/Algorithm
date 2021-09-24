import sys

sys.setrecursionlimit(100000)


def dfs(x, y, idx):
    if idx == len(goal):
        return 1
    if check[x][y][idx] != -1:
        return check[x][y][idx]

    check[x][y][idx] = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == goal[idx]:
                check[x][y][idx] += dfs(nx, ny, idx + 1)

    return check[x][y][idx]


n, m, k = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]
goal = list(input().rstrip())
check = [[[-1] * (len(goal))] * m] * n
directions = []

for i in range(1, k + 1):
    directions.extend([(-i, 0), (i, 0), (0, i), (0, -i)])

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == goal[0]:
            ans += dfs(i, j, 1)
print(ans)
