from collections import deque
from copy import deepcopy

n, m, k = map(int, input().split())
area = [list(map(str, input().strip())) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
ans = 0

def bfs():
    global ans
    vi = [[0] * m for _ in range(n)]
    vi[n-1][0] = 1
    q = deque([(n-1,0,1,vi)])

    while q:
        r,c,cnt,vi = q.popleft()
        if r == 0 and c == m-1:
            if cnt == k:
                ans += 1
            continue

        for i in range(4):
            nr,nc = r + dr[i], c + dc[i]
            vi_tmp = deepcopy(vi)

            if 0 <= nr < n and 0 <= nc < m:
                if vi[nr][nc] == 0 and area[nr][nc] == ".":
                    vi_tmp[nr][nc] = 1
                    q.append((nr,nc,cnt+1,vi_tmp))

    return

bfs()
print(ans)
