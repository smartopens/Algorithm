from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
di = 0
r, c = 0, 0
ans = 0


for _ in range(k):
    if 0 > r + dr[di] or r + dr[di] >= n:
        di = 1 if di == 3 else 3

    if 0 > c + dc[di] or c + dc[di] >= m:
        di = 0 if di == 2 else 2

    nr, nc = r + dr[di], c + dc[di]
    if di == 0:
        tmp = dice[1][2]
        dice[1][2], dice[1][1], dice[1][0] = dice[1][1], dice[1][0], dice[3][1]
        dice[3][1] = tmp
    elif di == 1:
        tmp = dice[3][1]
        dice[3][1], dice[2][1], dice[1][1] = dice[2][1], dice[1][1], dice[0][1]
        dice[0][1] = tmp
    elif di == 2:
        tmp = dice[1][0]
        dice[1][0], dice[1][1], dice[1][2] = dice[1][1], dice[1][2], dice[3][1]
        dice[3][1] = tmp
    elif di == 3:
        tmp = dice[0][1]
        dice[0][1], dice[1][1], dice[2][1] = dice[1][1], dice[2][1], dice[3][1]
        dice[3][1] = tmp

    vi = [[0] * m for _ in range(n)]
    vi[nr][nc] = 1
    q = deque([(nr, nc)])
    board_num = board[nr][nc]
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]

            if 0 <= nx < n and 0 <= ny < m:
                if vi[nx][ny] == 0 and board[nx][ny] == board_num:
                    vi[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1

    ans += board_num * cnt
    if dice[3][1] > board[nr][nc]:
        di = (di + 1) % 4
    elif dice[3][1] < board[nr][nc]:
        di = (di - 1) % 4

    r,c = nr, nc

print(ans)