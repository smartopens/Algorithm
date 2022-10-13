from collections import deque

n, m, d = map(int, input().split())
enemy_road_castle = [list(map(int, input().split())) for _ in range(n)] + [[0]*m]
defender = [0]*(m)
aligns = []
align_vi = [0]*m
dr = [-1,1,0,0]
dc = [0,0,-1,1]
max_ans = 0

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i + 1:], r - 1):
                yield [array[i]] + next

align = [i for i in range(m)]
aligns = combinations(align,3)
aligns = list(aligns)
ori_enemy_road_castle = [x[:] for x in enemy_road_castle]

for align in aligns:
    enemy_road_castle = [x[:] for x in ori_enemy_road_castle]
    for i in align:
        enemy_road_castle[n][i] = 1

    enemy_total = set()
    enemy_num = 0
    get_enemy = 0
    for e in range(n):
        enemy_num += sum(enemy_road_castle[e])
    while enemy_num > 0:
        enemies = set()
        for a in range(m):
            if enemy_road_castle[n][a] == 1:
                dists = [[0] * m for _ in range(n + 1)]
                min_dist = 1e9
                min_col = 1e9
                get_r,get_c = -1,-1
                vi = [[0] * m for _ in range(n+1)]

                q = deque([(n,a,0)])

                while q:
                    r,c,dist = q.popleft()
                    if dists[r][c] > d:
                        continue
                    if r != n and enemy_road_castle[r][c] == 1:
                        if min_dist >= dists[r][c]:
                            min_dist = dists[r][c]

                            if min_col > c:
                                min_col = c
                                get_r, get_c = r,c
                        continue

                    for i in range(4):
                        nr,nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n+1 and 0 <= nc < m:
                            if vi[nr][nc] == 0:
                                dists[nr][nc] = dists[r][c] + 1
                                vi[nr][nc] = 1
                                q.append((nr,nc,dist+1))
                if get_r != -1:
                    enemies.add((get_r,get_c))

        for r,c in enemies:
            enemy_road_castle[r][c] = 0
            get_enemy += 1

        for i in range(n,0,-1):
            for j in range(m):
                if i == n:
                    if enemy_road_castle[i-1][j] == 1:
                        enemy_road_castle[i-1][j] = 0
                        enemy_num -= 1
                        continue
                    else:
                        continue
                enemy_road_castle[i][j] = enemy_road_castle[i-1][j]

        enemy_road_castle[0] = [0]*m
        enemy_num = 0
        for e in range(n):
            enemy_num += sum(enemy_road_castle[e])

    max_ans = max(max_ans,get_enemy)

print(max_ans)