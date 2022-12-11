from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
town = [ list(map(int, input().split())) for _ in range(n)]
stores = deque([])
homes = deque([])
dr = [-1,1,0,0]
dc = [0,0,-1,1]
min_ans_dist = 1e9

for r in range(n):
    for c in range(n):
        if town[r][c] == 2:
            stores.append((r,c))

        elif town[r][c] == 1:
            homes.append((r, c))

for r in range(n):
    for c in range(n):
        if town[r][c] == 2:
            town[r][c] = 0

def bfs(x,y):
    vi = [[0]*n for _ in range(n)]
    vi[x][y] = 1
    q = deque([(x,y,0)])

    while q:
        r,c,dist = q.popleft()

        if tmp_town[r][c] == 2:
            return dist

        for i in range(4):
            nr, nc = r + dr[i],c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if not vi[nr][nc]:
                    vi[nr][nc] = 1
                    q.append((nr,nc,dist+1))


    return 0

for coms in combinations(stores ,m):
    tmp_town = deepcopy(town)
    tmp_stores = deque([])

    for sr, sc in coms:
        tmp_town[sr][sc] = 2
        tmp_stores.append((sr,sc))

    total_dists = 0


    for r,c in homes:
        fast_dist = 1e9
        for sr,sc in tmp_stores:
             fast_dist = min(fast_dist,abs(r-sr) + abs(c-sc))

        total_dists += fast_dist

    if min_ans_dist > total_dists:
        min_ans_dist = total_dists

print(min_ans_dist)


