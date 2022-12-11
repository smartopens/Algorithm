import sys
from copy import deepcopy
sys.setrecursionlimit(10**6)

n = int(input())

board1 = [list(input().strip()) for _ in range(n)]
board2 = deepcopy(board1)
vi = [[0]*n for _ in range(n)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

for r in range(n):
    for c in range(n):
        if board2[r][c] == "R":
            board2[r][c] = "G"

g_num1,g_num2 = 0, 0

def dfs(x,y,c,b):
    vi[x][y] = 1

    for i in range(4):
        nx, ny = x + dr[i], y + dc[i]

        if 0 <= nx < n and 0 <= ny < n:
            if b[nx][ny] == c and vi[nx][ny] == 0:
                dfs(nx, ny, c, b)



for r in range(n):
    for c in range(n):
        if vi[r][c] == 0:
            dfs(r,c,board1[r][c], board1)

            g_num1 += 1

vi = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if vi[r][c] == 0:
            dfs(r,c,board2[r][c], board2)
            g_num2 += 1

print(g_num1, g_num2)