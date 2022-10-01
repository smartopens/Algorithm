from collections import deque

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
ground_dist = [[0]*m for _ in range(n)]
vi = [[0]*m for _ in range(n)]
tr,tc = 0,0
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for r in range(n):
    for c in range(m):
        if ground[r][c] == 2:
            tr,tc = r,c
            break

def bfs():
    vi[tr][tc] = 1
    q = deque([(tr,tc,0)])

    while q:
        r,c,dist = q.popleft()

        for i in range(4):
            nr,nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if vi[nr][nc] == 0 and ground[nr][nc] == 1:
                    ground_dist[nr][nc] = dist + 1
                    vi[nr][nc] = 1
                    q.append((nr,nc,dist+1))
    return

bfs()

for r in range(n):
    for c in range(m):
        if vi[r][c] == 0 and ground[r][c] == 1:
            ground_dist[r][c] = -1

for r in range(n):
    for c in range(m):
        if c == m-1:
            print(ground_dist[r][c], end='')
            continue
        print(ground_dist[r][c], end = ' ')
    print()
