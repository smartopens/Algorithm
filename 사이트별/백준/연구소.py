from collections import deque
from itertools import combinations

n, m = map(int, input().split(' '))
board = []

for _ in range(n):
    board.append(list(map(int, input().split(' '))))

zeros = deque()

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            zeros.append((r,c))

def bfs():
    global b, ans
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False]*m for _ in range(n)]
    twos = deque()

    for r in range(n):
        for c in range(m):
            if b[r][c] == 2:
                twos.append((r, c))

    while twos:
        x,y = twos.popleft()

        for dx, dy in directions:
            nx, ny = x+ dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if b[nx][ny] == 0:
                        b[nx][ny] = 2
                        visited[nx][ny] = True
                        twos.append((nx,ny))
    sum = 0

    for bi in (b):
        sum += bi.count(0)

    ans = max(ans, sum)
    return

ans = 0

for combi in combinations(zeros,3):
    b = [x[:] for x in board]
    for x,y in combi:
        b[x][y] = 1

    bfs()

print(ans)
