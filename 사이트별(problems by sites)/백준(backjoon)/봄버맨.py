from collections import deque
from copy import deepcopy

r, c, n = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]
tmp = [[0]*c for _ in range(r)]
tmp2 = [[0]*c for _ in range(r)]
tmp_reset = [["O"]*c for _ in range(r)]

for x in range(r):
    for y in range(c):
        if board[x][y] == "O":
            tmp[x][y] = 1

s = 0

for s in range(1,n+1):
    if s == 1:
        continue
    if (s-1) % 2 == 1:
        for x in range(r):
            for y in range(c):
                if board[x][y] == ".":
                    tmp2[x][y] = 1
                    board[x][y] = "O"

    elif (s-1) % 2 == 0:
        for x in range(r):
            for y in range(c):
                if tmp[x][y] == 1:
                    for i in range(x-1,x+2):
                        if 0 <= i < r:
                            board[i][y] = "."
                            tmp2[i][y] = 0
                    for i in range(y-1,y+2):
                        if 0 <= i < c:
                            board[x][i] = "."
                            tmp2[x][i] = 0
        tmp = deepcopy(tmp2)

for x in range(r):
    for y in range(c):
        print(board[x][y], end = '')
    print()

