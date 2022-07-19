t = int(input())


def dfs(x, y, tx, ty, c):
    global ans, space

    return


def updateSpace(x, y, r, c):
    global space

    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            space[i][j] = c

    return


for _ in range(t):
    sx, sy, tx, ty = map(int, input().split())
    space = [[0] * 1000 for _ in range(1000)]
    di = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ans = 1e9
    n = int(input())

    for c in range(n):
        x, y, r = map(int, input().split())
        updateSpace(x, y, r, c)

    sc = space[sx][sy]
    dfs(sx, sy, tx, ty, c)
