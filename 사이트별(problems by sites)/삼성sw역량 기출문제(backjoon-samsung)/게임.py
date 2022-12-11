from collections import deque

n, m = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if board[r][c] == "H":
            continue
        board[r][c] = int(board[r][c])

dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = 0
is_infinite = False
vi[0][0] = 1

def bfs(vi):
    global answer, is_infinite

    q = deque([(0,0,0,vi)])
    max_cnt = n*m

    while q:
        r,c,cnt,vi = q.popleft()
        answer = max(answer,cnt)
        dist = board[r][c]

        if cnt > max_cnt:
            is_infinite = True
            break

        for i in range(4):
            nr, nc = r + dr[i]*dist, c + dc[i]*dist

            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != "H" and cnt + 1 > dp[nr][nc]:
                dp[nr][nc] = cnt + 1
                vi[nr][nc] = 1
                q.append((nr,nc,cnt+1,vi))
                vi[nr][nc] = 0

        if is_infinite:
            break

    return

bfs(vi)

if is_infinite:
    print(-1)
else:
    print(answer+1)