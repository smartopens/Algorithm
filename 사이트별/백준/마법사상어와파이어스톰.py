from copy import deepcopy
from collections import deque

n, q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2 ** n)]
fire_storm = list(map(int, input().split()))
sx, sy = 0, 0
ice_tmp = [[0] * (2 ** n) for _ in range(2 ** n)]
ice_vi = [[0] * (2 ** n) for _ in range(2 ** n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
ans_ice_num = 0
ans_big_ice_num = 0

for i in range(2 ** n):
    for j in range(2 ** n):
        ice_tmp[i][j] = ice[2 ** n - j - 1][i]
t = 0

for l in fire_storm:
    ice_tmp = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(0, 2 ** n, 2 ** l):
        for j in range(0, 2 ** n, 2 ** l):
            x, y = sx + i, sy + j
            for r in range(2 ** l):
                for c in range(2 ** l):
                    ice_tmp[x + r][y + c] = ice[x + 2 ** l - c - 1][y + r]

    ice_tmp_copy = deepcopy(ice_tmp)
    for r in range(2 ** n):
        for c in range(2 ** n):
            ice_cnt = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < 2 ** n and 0 <= nc < 2 ** n:
                    if ice_tmp_copy[nr][nc] > 0:
                        ice_cnt += 1

            if ice_cnt < 3:

                if ice_tmp[r][c] > 0:
                    ice_tmp[r][c] -= 1

    ice = deepcopy(ice_tmp)


for i in ice:
    ans_ice_num += sum(i)

max_g_num = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if ice_vi[i][j] == 0 and ice[i][j] > 0:
            g_num = 1
            q = deque([(i,j,1)])
            ice_vi[i][j] = 1

            while q:
                r,c,cnt = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < 2 ** n and 0 <= nc < 2 ** n:
                        if ice_vi[nr][nc] == 0 and ice[nr][nc] > 0:
                            ice_vi[nr][nc] = 1
                            g_num += 1
                            q.append((nr,nc,cnt+1))

            if g_num > max_g_num:
                max_g_num = g_num


print(ans_ice_num)
print(max_g_num)