from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
dist = [[0] * n for _ in range(n)]
sx, sy, tx, ty = map(int, input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
ans = -1

def bfs(sx,sy,tx,ty):
    global ans

    q = deque([(sx,sy)])
    dist[sx][sy] = 0

    while q:
        x,y = q.popleft()
        if x == tx and y == ty:
            ans = dist[x][y]
            return

        for i in range(6):
            nx, ny = x + dx[i],y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

    return
bfs(sx, sy, tx, ty)
print(ans)