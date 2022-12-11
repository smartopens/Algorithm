from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

m, s = map(int, input().split())
smell = [[0] * 4 for _ in range(4)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
board = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(m):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1].append(d - 1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

def move(sx, sy):
    maxFish = 0
    paths = []
    sharkDi = {2: "1", 0: "2", 6: "3", 4: "4"}
    q = deque([[sx, sy, 0, 0, "", [[0] * 4 for _ in range(4)]]])

    while q:
        x, y, fish, cnt, path, vi = q.popleft()
        tmp = 0

        if cnt >= 3:
            if maxFish < fish:
                paths = [path]
                maxFish = fish
            elif maxFish == fish:
                paths.append(path)
            continue

        for i in range(4):
            vi2 = deepcopy(vi)
            di = 2 * i
            nx, ny = x + dx[di], y + dy[di]

            if 0 <= nx < 4 and 0 <= ny < 4:
                tmp = 0

                if board[nx][ny] and vi2[nx][ny] == 0:
                    vi2[nx][ny] = 1
                    tmp += len(board[nx][ny])
                    q.append([nx, ny, fish + tmp, cnt + 1, path + sharkDi[di], vi2])
                else:
                    q.append([nx, ny, fish, cnt + 1, path + sharkDi[di], vi2])

    paths = list(map(int, paths))
    paths.sort()
    return paths[0]


sharkDi2 = {1: 2, 2: 0, 3: 6, 4: 4}

for _ in range(s):
    copys = []
    boardtmp = [[[] for _ in range(4)] for _ in range(4)]
    fish_before = deepcopy(board)

    for r in range(4):
        for c in range(4):
            if board[r][c]:
                for d in board[r][c]:
                    cango = False
                    di = d
                    for _ in range(8):
                        d1, d2 = dx[di], dy[di]
                        nx, ny = r + d1, c + d2

                        if 0 <= nx < 4 and 0 <= ny < 4 and smell[nx][ny] == 0 \
                                and not (nx == sx and ny == sy):
                            cango = True
                            break
                        di = (di + 7) % 8
                    if not cango:
                        boardtmp[r][c].append(d)
                        continue

                    boardtmp[nx][ny].append(di)

    board = deepcopy(boardtmp)
    path = move(sx, sy)
    for p in str(path):
        sx, sy = sx + dx[sharkDi2[int(p)]], sy + dy[sharkDi2[int(p)]]
        if board[sx][sy]:
            smell[sx][sy] = 3
            board[sx][sy] = []

    for r in range(4):
        for c in range(4):
            if smell[r][c] > 0:
                smell[r][c] -= 1

    for i in range(4):
        for j in range(4):
            if fish_before[i][j]:
                for d in fish_before[i][j]:
                    board[i][j].append(d)
ans = 0
for r in range(4):
    for c in range(4):
        tmp = 0
        if board[r][c]:
            tmp += len(board[r][c])

        ans += tmp

print(ans)
