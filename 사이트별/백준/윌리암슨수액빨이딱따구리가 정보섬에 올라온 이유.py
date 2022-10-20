from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().strip())) for _ in range(n)]
dists = [[0]*m for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
sx,sy = 0,0
dishes = set()

for r in range(n):
    for c in range(m):
        if area[r][c] == 2:
            sx,sy = r,c
        elif area[r][c] > 1:
            dishes.add((r,c))

def bfs(sx,sy):
    q = deque([(sx,sy,0)])

    while q:
        r,c,dist = q.popleft()

        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not vi[nr][nc] and area[nr][nc] != 1:
                    if area[nr][nc] > 2:
                        return dists[r][c] + 1

                    vi[nr][nc] = 1
                    dists[nr][nc] = dists[r][c] + 1
                    q.append((nr,nc,dist+1))

    return -1

ans_dist = bfs(sx,sy)
if ans_dist == -1:
    print("NIE")
else:
    print("TAK")
    print(ans_dist)