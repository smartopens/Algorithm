import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(str, input().rstrip())) for _ in range(n)]
sr,sc = 0,0
check = [[[0]*(1<<6) for _ in range(m)] for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for r in range(n):
    for c in range(m):
        if maze[r][c] == "0":
            sr, sc = r,c

def bfs(x,y):
    check[x][y][0] = 1
    q = deque([(x,y,0,0)])

    while q:
        r,c,k,cnt = q.popleft()

        if maze[r][c] == "1":
            return cnt

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not check[nr][nc][k]:
                if maze[nr][nc].isupper():
                    if k & (1 <<(ord(maze[nr][nc].lower()) - ord('a'))):
                        check[nr][nc][k] = 1
                        q.append((nr,nc,k,cnt+1))

                elif maze[nr][nc].islower():
                    tmp_key = k | (1 <<(ord(maze[nr][nc]) - ord('a')))
                    check[nr][nc][tmp_key] = 1
                    q.append((nr, nc, tmp_key,cnt+1))

                elif maze[nr][nc] != "#":
                    check[nr][nc][k] = 1
                    q.append((nr, nc, k,cnt+1))
    return -1

answer = bfs(sr,sc)
if answer == -1:
    print(-1)
else:
    print(answer)