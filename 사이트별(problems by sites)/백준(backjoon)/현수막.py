from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dr = [-1,1,0,0,-1,1,-1,1]
dc = [0,0,-1,1,-1,1,1,-1]
ans = 0

def findString(x,y):
    q = deque([(x,y)])
    vi[x][y] = 1

    while q:
        r,c = q.popleft()
        for i in range(8):
            nr,nc = r + dr[i],c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1 and not vi[nr][nc]:
                    q.append((nr,nc))
                    vi[nr][nc] = 1
    return

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not vi[i][j]:
            findString(i,j)
            ans += 1

print(ans)