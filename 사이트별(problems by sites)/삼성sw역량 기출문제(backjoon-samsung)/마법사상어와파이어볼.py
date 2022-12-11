from copy import deepcopy

n, m, k = map(int, input().split())
board = [[0] * n for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
ans = 0

def move(x, y, s, d):
    s = s % n

    while s > 0:
        x += dx[d]
        y += dy[d]
        s -= 1
        if x >= n:
            x = 0
        if x < 0:
            x = n-1
        if y >= n:
            y = 0
        if y < 0:
            y = n - 1

    return x, y


for _ in range(m):
    r, c, w, s, d = map(int, input().split())
    board[r-1][c-1] = [[w, s, d]]

for _ in range(k):
    board_tmp = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if board[r][c]:
                fire_list = board[r][c]
                x, y = r, c

                for fire in fire_list:
                    w, s, d = fire
                    nx, ny = move(x, y, s, d)

                    if not board_tmp[nx][ny]:
                        board_tmp[nx][ny] = [[w, s, d]]
                    else:
                        board_tmp[nx][ny].append([w, s, d])

    board = [b[:] for b in board_tmp]

    for r in range(n):
        for c in range(n):
            if board[r][c] and len(board[r][c]) >= 2:
                fire_list = board[r][c]
                fire_len = len(fire_list)
                fire_w = 0
                fire_s = 0
                a = 0
                b = 0

                for fire in fire_list:
                    w, s, d = fire
                    fire_w += w
                    fire_s += s

                    if d % 2 == 0:
                        a += 1
                    else:
                        b += 1
                fire_w = fire_w // 5
                fire_s = fire_s // fire_len

                if fire_w == 0:
                    board[r][c] = 0
                    continue

                if a == fire_len or b == fire_len:
                    board[r][c] = [[fire_w, fire_s, 0], [fire_w, fire_s, 2],
                                   [fire_w, fire_s, 4], [fire_w, fire_s, 6]]
                else:
                    board[r][c] = [[fire_w, fire_s, 1], [fire_w, fire_s, 3],
                                   [fire_w, fire_s, 5], [fire_w, fire_s, 7]]


for r in range(n):
    for c in range(n):
        if board[r][c]:
            fire_list = board[r][c]

            for fire in fire_list:
                ans += fire[0]
print(ans)