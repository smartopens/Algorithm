from collections import deque
import sys

sys.setrecursionlimit(1000000)

def detect(d, a, x, y):
    global di, n, m

    for d2 in d:
        dx,dy = di[d2]

        while 0 <= x + dx < n and 0 <= y + dy < m and a[x + dx][y + dy] != 6:
            x = x + dx
            y = y + dy
            a[x][y] = 7

    return a

def dfs(case, c, area):
    global cctvs, moveCase, ans

    if c == case:
        tempa = 0
        for r in area:
            tempa += r.count(0)

        ans = min(ans, tempa)
        return

    a = [x[:] for x in area]
    (i, (x, y)) = cctvs[c]

    for d in moveCase[i]:
        newA = detect(d,a,x,y)
        dfs(case,c+1,newA)
        a = [x[:] for x in area]

    return


di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
moveCase = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 3], [1, 0], [2, 1], [3, 2]],
            [[0, 2, 3], [1, 3, 0], [2, 0, 1], [3, 1, 2]], [[0, 1, 2, 3]]
            ]
cctvs = deque()
ans = sys.maxsize

for r in range(n):
    for c in range(m):
        if 0 < area[r][c] < 6:
            cctvs.append((area[r][c], (r, c)))

case = len(cctvs)
dfs(case, 0, area)
print(ans)