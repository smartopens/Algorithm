import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def dfs(x,y):

    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if ground[x][y] > ground[nx][ny]:
                dp[x][y] += dfs(nx,ny)

    return dp[x][y]

dfs(0,0)
print(dp[0][0])