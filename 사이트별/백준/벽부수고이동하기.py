from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
ans = 1e9
dr = [-1,1,0,0]
dc = [0,0,-1,1]
vi = [[0]*m for _ in range(n)]
distance = [[1e9]*m for _ in range(n)]

def dfs(r,c,wall,vi,cnt):
    global ans
    vi[r][c] = 1

    if r == n-1 and c == m-1:
        ans = min(ans,cnt)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if vi[nr][nc] == 0:
                if board[nr][nc] == 1 and wall > 0:
                    vi[nr][nc] = 1
                    dfs(nr,nc,0,vi,cnt+1)
                    vi[nr][nc] = 0
                elif board[nr][nc] == 0:
                    vi[nr][nc] = 1
                    dfs(nr, nc, wall, vi,cnt+1)
                    vi[nr][nc] = 0
def bfs():
    global ans
    vi = [[0]*m for _ in range(n)]
    q = deque([(0,0,1,1)])
    vi[0][0] = 1

    while q:
        r,c,cnt,wall = q.popleft()

        if r == n - 1 and c == m - 1:
            ans = min(ans, cnt)
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if vi[nr][nc] == 0:
                    if board[nr][nc] == 1 and wall > 0:
                        vi[nr][nc] = 1
                        q.append((nr,nc,cnt+1,0))
                    elif board[nr][nc] == 0:
                        vi[nr][nc] = 1
                        q.append((nr,nc,cnt+1,wall))

    return

bfs()

if ans == 1e9:
    print(-1)
else:
    print(ans)