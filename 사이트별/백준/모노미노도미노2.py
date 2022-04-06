from collections import deque
from copy import deepcopy

board = [[0] * 10 for _ in range(4)] + [[0] * 4 for _ in range(6)]
score = 0
n = int(input())


def move1(x, y, board, t):
    if t != 3:
        while y + 1 <= 9 and board[x][y + 1] == 0:
            x, y = x, y + 1

        board[x][y] = 1
        if t == 2:
            board[x][y-1] = 1
    else:
        while x + 1 <= 3 and y + 1 <= 9 and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            x, y = x, y + 1

        board[x][y] = 1
        board[x + 1][y] = 1

    return


def move2(x, y, board, t):
    if t != 2:
        while x + 1 <= 9 and board[x + 1][y] == 0:
            x, y = x + 1, y

        board[x][y] = 1
        if t == 3:
            board[x-1][y] = 1
    else:
        while x + 1 <= 9 and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0:
            x, y = x + 1, y

        board[x][y] = 1
        board[x][y + 1] = 1

    return


def remove(color, index):
    if color == 'green':
        for i in range(index, 3, -1):
            if i == 0:
                for j in range(4):
                    board[i][j] = 0
                return
            for j in range(4):
                board[i][j] = board[i - 1][j]
    else:
        for j in range(index, 3, -1):
            if j == 0:
                for i in range(4):
                    board[i][j] = 0
                return
            for i in range(4):
                board[i][j] = board[i][j - 1]


for _ in range(n):
    t, x2, y2 = map(int, input().split())
    q = deque([])
    q.append([x2, y2])
    blue = deepcopy(q)
    green = deepcopy(q)

    while blue:
        x, y = blue.popleft()
        move1(x, y, board, t)

    while green:
        gx, gy = green.popleft()
        move2(gx, gy, board, t)

    for j in range(6, 10):
        cnt = 0
        for i in range(4):
            if board[i][j] == 1:
                cnt += 1

        if cnt == 4:
            remove("blue", j)
            score += 1

    for j in range(6, 10):
        cnt = 0
        for i in range(4):
            if board[j][i] == 1:
                cnt += 1

        if cnt == 4:
            remove("green", j)
            score += 1

    for i in range(4, 6):
        for j in range(4):
            if board[j][i] == 1:
                remove("blue", 9)
                break

    for i in range(4, 6):
        for j in range(4):
            if board[i][j] == 1:
                remove("green", 9)
                break

block = 0

for i in range(6, 10):
    for j in range(4):
        if board[j][i] == 1:
            block += 1

for i in range(6, 10):
    for j in range(4):
        if board[i][j] == 1:
            block += 1

print(score)
print(block)
