from collections import deque

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
size = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1


for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            tmp_size = 1
            board[r][c] = 0
            q = deque([(r,c)])

            while q:
                x,y = q.popleft()

                for i in range(4):
                    nx,ny = x + dr[i], y + dc[i]

                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 1:
                            board[nx][ny] = 0
                            tmp_size += 1
                            q.append((nx,ny))

            if tmp_size > size:
                size = tmp_size
print(size)


