import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]
vi = [[0]*n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
width = 0
width_list = []

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1


def dfs(y,x,g_num,cnt):
    global width
    vi[y][x] = g_num
    width = max(width, width+1)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < m and 0 <= nx < n:
            if vi[ny][nx] == 0 and board[ny][nx] == 0:
                dfs(ny,nx,g_num, cnt + 1)


g_num = 1
for y in range(m):
    for x in range(n):
        if vi[y][x] == 0 and board[y][x] == 0:
            dfs(y,x,g_num,1)
            g_num += 1
            width_list.append(width)
            width = 0

width_list.sort()
print(g_num-1)
for i in range(len(width_list)):
    if i == len(width_list) -1:
        print(width_list[i], end='')
        break
    print(width_list[i], end = ' ')