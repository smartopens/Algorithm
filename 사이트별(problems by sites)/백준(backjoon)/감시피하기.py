from collections import deque
from itertools import combinations

n = int(input())

board = [list(input().split()) for _ in range(n)]
board2 = [b[:] for b in board]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

q = deque([])

for r in range(n):
    for c in range(n):
        if board[r][c] == 'X':
            if (r,c) not in q:
                q.append((r, c))


is_ok = True
for combi in combinations(q,3):
    tmp = deque([])
    for r,c in combi:
        board[r][c] = "O"
        tmp.append((r,c))
    is_ok = True

    for r in range(n):
        for c in range(n):
            if board[r][c] == "T":
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]

                    while 0 <= nr  < n and 0 <= nc < n and board[nr][nc] != "O":
                        if board[nr][nc] == "S":
                            is_ok = False
                            break
                        nr += dr[i]
                        nc += dc[i]
    if is_ok:
        break
    for r,c in tmp:
        board[r][c] = "X"


if not is_ok:
    print("NO")
else:
    print("YES")
