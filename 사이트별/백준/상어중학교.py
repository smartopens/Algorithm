from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
group = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def rotate():
    global board

    boardTmp = [[0] * n for _ in range(n)]
    c = 0

    for b in board:
        for j in range(n):
            boardTmp[j][c] = b.pop()
        c += 1

    board = deepcopy(boardTmp)
    return

def move(x,y):

    while x + 1 < n and board[x+1][y] == -2:
        x = x + 1

    return x,y

def fallBlock():
    global board,group

    for r in range(n-1,-1,-1):
        for c in range(n-1,-1,-1):
            if board[r][c] >= 0:
                tr,tc = r+1, c

                if 0<= tr < n and board[tr][tc] == -2:
                    nr, nc = move(tr,tc)
                    board[nr][nc] = board[r][c]
                    board[r][c] = -2
    return

def gravity(a):
    for i in range(n-2, -1, -1):  # 밑에서 부터 체크
        for j in range(n):
            if a[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0<=r+1<n and a[r+1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r+1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break

def rot90(a):
    new_a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i] = a[i][j]

    return new_a

def make_group(r, c, gNum, color):
    global board,group
    group[r][c] = [gNum]
    vi[r][c] = 1
    q = deque([(r, c, 0, 1)])
    rains = deque([])
    rainMax, sizeMax = 0,1

    while q:
        x, y, rainBow, size = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and vi[nx][ny] == 0:
                if board[nx][ny] == color:
                    vi[nx][ny] = 1
                    sizeMax += 1
                    group[nx][ny] = [gNum]
                    q.append((nx,ny,rainBow,size+1))
                elif board[nx][ny] == 0:
                    if group[nx][ny] == 0:
                        group[nx][ny] = [gNum]
                    else:
                        group[nx][ny].append(gNum)
                    vi[nx][ny] = 1
                    sizeMax += 1
                    rainMax += 1
                    rains.append((nx,ny))
                    q.append((nx, ny, rainBow, size + 1))

    for x,y in rains:
        vi[x][y] = 0
    return [sizeMax,rainMax,r,c,gNum]

while True:
    isBreak = True
    group = [[0] * n for _ in range(n)]
    vi = [[0] * n for _ in range(n)]
    blocks = []
    group_num = 1

    for r in range(n):
        for c in range(n):
            if board[r][c] > 0 and vi[r][c] == 0:
                tmp = make_group(r, c, group_num, board[r][c])
                if tmp[0] >= 2:
                    blocks.append(tmp)
                    isBreak = False

                group_num += 1

    if isBreak:
        break
    blocks.sort(key = lambda x: (x[0],x[1],x[2],x[3]), reverse = True)
    bNum = 0
    g,s = blocks[0][4], blocks[0][0]


    for r in range(n):
        for c in range(n):
            if group[r][c] != 0  and g in group[r][c]:
                board[r][c] = -2
                bNum += 1

    ans += s ** 2

    fallBlock()
    rotate()
    fallBlock()

print(ans)