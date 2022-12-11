from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ans = 0

# 좌 상 우 하
d1 = deque([(-1, 0), (-1, -1), (-1, -2), (1, 0), (1, -1), (1, -2), (-2, -1), (2, -1), (0, -3)])
d2 = deque([(0, -1), (-1, -1), (-2, -1), (0, 1), (-1, 1), (-2, 1), (-1, -2), (-1, 2), (-3, 0)])
d3 = deque([(-1, 0), (-1, 1), (-1, 2), (1, 0), (1, 1), (1, 2), (-2, 1), (2, 1), (0, 3)])
d4 = deque([(0, -1), (1, -1), (2, -1), (0, 1), (1, 1), (2, 1), (1, -2), (1, 2), (3, 0)])
sand_percent = [0.01, 0.07, 0.1, 0.01, 0.07, 0.1, 0.02, 0.02, 0.05]

sx, sy = n // 2, n // 2
is_done = False
dist = 1
di = 0

while True:
    for _ in range(dist):
        sand = board[sx][sy - 1]
        sand_tmp = 0

        for i in range(9):
            send_moved = int(sand * sand_percent[i])
            nx, ny = sx + d1[i][0], sy + d1[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] += send_moved
            else:
                ans += send_moved

            sand_tmp += send_moved

        if 0 <= sx < n and 0 <= sy - 2 < n:
            board[sx][sy - 2] += (sand - sand_tmp)
        else:
            ans += (sand - sand_tmp)
        board[sx][sy - 1] = 0
        sx, sy = sx, sy - 1

        if sx == 0 and sy == 0:
            is_done = True
            break

    if is_done:
        break
    for _ in range(dist):
        sand = board[sx + 1][sy]
        sand_tmp = 0

        for i in range(9):
            send_moved = int(sand * sand_percent[i])
            nx, ny = sx + d4[i][0], sy + d4[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] += send_moved
            else:
                ans += send_moved

            sand_tmp += send_moved

        if 0 <= sx + 2 < n and 0 <= sy < n:
            board[sx + 2][sy] += (sand - sand_tmp)
        else:
            ans += (sand - sand_tmp)

        board[sx + 1][sy] = 0
        sx, sy = sx + 1, sy
    dist += 1

    for _ in range(dist):
        sand = board[sx][sy + 1]
        sand_tmp = 0

        for i in range(9):
            send_moved = int(sand * sand_percent[i])
            nx, ny = sx + d3[i][0], sy + d3[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] += send_moved
            else:
                ans += send_moved

            sand_tmp += send_moved

        if 0 <= sx < n and 0 <= sy + 2 < n:
            board[sx][sy + 2] += (sand - sand_tmp)
        else:
            ans += (sand - sand_tmp)
        board[sx][sy + 1] = 0
        sx, sy = sx, sy + 1
    for _ in range(dist):
        sand = board[sx - 1][sy]
        sand_tmp = 0

        for i in range(9):
            send_moved = int(sand * sand_percent[i])
            nx, ny = sx + d2[i][0], sy + d2[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] += send_moved
            else:
                ans += send_moved

            sand_tmp += send_moved

        if 0 <= sx - 2 < n and 0 <= sy < n:
            board[sx - 2][sy] += (sand - sand_tmp)
        else:
            ans += (sand - sand_tmp)
        board[sx-1][sy] = 0
        sx, sy = sx-1, sy
    dist += 1


print(ans)