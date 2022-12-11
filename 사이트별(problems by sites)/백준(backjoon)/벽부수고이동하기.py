from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
ans = 1e9
dr = [-1,1,0,0]
dc = [0,0,-1,1]
vi = [[[0]*2 for _ in range(m)] for _ in range(n)]
distance = [[1e9]*m for _ in range(n)]

def bfs():
    global ans
    q = deque([(0,0,1,1)])
    vi[0][0][0] = 1

    while q:
        r,c,cnt,wall = q.popleft()

        if r == n - 1 and c == m - 1:
            ans = min(ans, cnt)
            return

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if vi[nr][nc][wall] == 0:
                    if board[nr][nc] == 1 and wall > 0:
                        vi[nr][nc][0] = vi[r][c][1] + 1
                        q.append((nr,nc,cnt+1,0))
                    if board[nr][nc] == 0:
                        vi[nr][nc][wall] = vi[r][c][wall] + 1
                        q.append((nr,nc,cnt+1,wall))

    return

bfs()

if ans == 1e9:
    print(-1)
else:
    print(ans)