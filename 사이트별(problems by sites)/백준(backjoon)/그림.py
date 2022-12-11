from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n) ]
sizes = []
vi = [[0]*m for _ in range(n)]
drow_num = 0
max_size = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y):
    global max_size

    q = deque([(x,y)])
    size = 1

    while q:
        r,c = q.popleft()
        vi[r][c] = 1

        for i in range(4):
            nr, nc = r + dr[i],c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if not vi[nr][nc] and board[nr][nc] == 1:
                    vi[nr][nc] = 1
                    size += 1
                    q.append((nr,nc))

    if size > max_size:
        max_size = size

for r in range(n):
    for c in range(m):
        if board[r][c] == 1 and not vi[r][c]:
            drow_num += 1
            bfs(r,c)

print(drow_num)
print(max_size)
