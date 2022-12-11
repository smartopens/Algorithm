from collections import deque

n, m, k = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
smell = [[[] for _ in range(n)] for _ in range(n)]
shark_dis = [[] for _ in range(m+1)]
dr = [0] + [-1,1,0,0]
dc = [0] + [0,0,-1,1]
answer = 0
now_shark_di = list(map(int, input().split()))

for r in range(n):
    for c in range(n):
        if sea[r][c] == 0:
            sea[r][c] = []
        else:
            sea[r][c] = [sea[r][c],now_shark_di[sea[r][c]-1]]

for i in range(1,m+1):
    for _ in range(4):
        shark_dis[i].append(list(map(int, input().split())))

shark_num = m
while answer <= 1000:

    for r in range(n):
        for c in range(n):
            if sea[r][c]:
                smell[r][c] = [sea[r][c][0],k]

    new_sea = [[[] for _ in range(n)] for _ in range(n)]
    smell_queue = deque([])

    for r in range(n):
        for c in range(n):
            if sea[r][c]:
                s_id, di = sea[r][c]
                is_go = False

                for i in range(4):
                    n_di = shark_dis[s_id][di-1][i]
                    nr, nc = r + dr[n_di], c + dc[n_di]
                    if 0 <= nr < n and  0 <= nc < n and not smell[nr][nc]:
                        is_go = True

                        if new_sea[nr][nc]:
                            if new_sea[nr][nc][0] > sea[r][c][0]:
                                new_sea[nr][nc] = [sea[r][c][0],n_di]
                                shark_num -= 1
                            else:
                                shark_num -= 1
                        else:
                            new_sea[nr][nc] = [sea[r][c][0], n_di]
                        break

                if not is_go:
                    for i in range(4):
                        n_di = shark_dis[s_id][di-1][i]
                        nr, nc = r + dr[n_di], c + dc[n_di]
                        if 0 <= nr < n and 0 <= nc < n and s_id == smell[nr][nc][0]:
                            new_sea[nr][nc] = [sea[r][c][0], n_di]
                            break
    answer += 1
    for r in range(n):
        for c in range(n):
            if smell[r][c]:
                if smell[r][c][1] > 1:
                    smell[r][c][1] -= 1
                else:
                    smell[r][c] = []

    for r in range(n):
        for c in range(n):
            if new_sea[r][c]:
                smell[r][c] = [new_sea[r][c][0], k]

    if shark_num == 1:
        break

    sea = [x[:] for x in new_sea]


if answer >1000:
    print(-1)
else:
    print(answer)