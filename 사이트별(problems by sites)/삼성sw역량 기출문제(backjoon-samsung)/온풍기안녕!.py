from collections import deque

n,m,k = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(n)]
degree_up = [[0]*m for _ in range(n)]
cant_go = [[[]]*m for _ in range(n)]
wall_n = int(input())
walls = [list(map(int, input().split())) for _ in range(wall_n)]
ans = 0
warmers = []
detect_spot = []
dr1 = [-1,0,1]
dc1 = [1,1,1]
dr2 = [-1,0,1]
dc2 = [-1,-1,-1]
dr3 = [-1,-1,-1]
dc3 = [-1,0,1]
dr4 = [1,1,1]
dc4 = [-1,0,1]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for r in range(n):
    for c in range(m):
        if 0< home[r][c] < 5:
            warmers.append((r,c,home[r][c]))
        elif home[r][c] == 5:
            detect_spot.append((r,c))

for r,c,d in walls:
    r,c = r-1, c-1
    if d == 0:
        cant_go[r][c].append((r-1,c))
        cant_go[r-1][c].append((r,c))
    else:
        cant_go[r][c].append((r, c+1))
        cant_go[r][c+1].append((r, c))

def get_warm_area(r,c,di,degree_up):
    vi = [[0]*m for _ in range(n)]
    if di == 1:
        r,c = r,c+1
    elif di == 2:
        r,c = r,c-1
    elif di == 3:
        r,c = r-1,c
    elif di == 4:
        r,c = r+1,c

    vi[r][c] = 1
    degree_up[r][c] += 5
    print(degree_up[r][c])
    q = deque([(r, c, di,4)])

    while q:
        r,c,di,degree = q.popleft()

        if degree <= 0:
            continue
        if di == 1:
            for i in range(3):
                nr, nc = r + dr1[i], c + dc1[i]

                if 0 <= nr < n and 0 <= nc < m:
                    if not vi[nr][nc]:
                        if r -1 == nr:
                            if cant_go[r][c]:
                                if (r-1, c) in cant_go[r][c]:
                                    continue
                            if cant_go[r-1][c]:
                                if (r-1, c+1) in cant_go[r - 1][c]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))

                        elif r + 1== nr:
                            if cant_go[r][c]:
                                if (r+1, c) in cant_go[r][c]:
                                    continue
                            if cant_go[r+1][c]:
                                if (r+1, c+1) in cant_go[r + 1][c]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))
                        else:
                            if cant_go[r][c]:
                                if (r, c+1) in cant_go[r][c]:
                                    continue
                            vi[nr][nc] = 1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))

        elif di == 2:
            for i in range(3):
                nr, nc = r + dr2[i], c + dc2[i]

                if 0 <= nr < n and 0 <= nc < m:
                    if not vi[nr][nc]:
                        if r -1 == nr:
                            if cant_go[r][c]:
                                if (r-1, c) in cant_go[r][c]:
                                    continue
                            if cant_go[r-1][c]:
                                if (r-1, c-1) in cant_go[r - 1][c]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))

                        elif r + 1 == nr:
                            if cant_go[r][c]:
                                if (r+1, c) in cant_go[r][c]:
                                    continue
                            if cant_go[r+1][c]:
                                if (r+1, c-1) in cant_go[r + 1][c]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))
                        else:
                            if cant_go[r][c]:
                                if (r, c-1) in cant_go[r][c]:
                                    continue
                            vi[nr][nc] = 1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))
        elif di == 3:
            for i in range(3):
                nr, nc = r + dr3[i], c + dc3[i]

                if 0 <= nr < n and 0 <= nc < m:
                    if not vi[nr][nc]:
                        if c -1 == nc:
                            if cant_go[r][c]:
                                if (r, c-1) in cant_go[r][c]:
                                    continue
                            if cant_go[r][c-1]:
                                if (r-1, c-1) in cant_go[r][c-1]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))

                        elif c +1 == nc:
                            if cant_go[r][c]:
                                if (r, c+1) in cant_go[r][c]:
                                    continue
                            if cant_go[r][c+1]:
                                if (r-1, c+1) in cant_go[r][c+1]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))
                        else:
                            if cant_go[r][c]:
                                if (r-1, c) in cant_go[r][c]:
                                    continue
                            vi[nr][nc] = 1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))
        elif di == 4:
            for i in range(3):
                nr, nc = r + dr4[i], c + dc4[i]

                if 0 <= nr < n and 0 <= nc < m:
                    if not vi[nr][nc]:
                        if c - 1== nc:
                            if cant_go[r][c]:
                                if (r, c-1) in cant_go[r][c]:
                                    continue
                            if cant_go[r][c-1]:
                                if (r+1, c-1) in cant_go[r][c-1]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))

                        elif c + 1== nc:
                            if cant_go[r][c]:
                                if (r, c+1) in cant_go[r][c]:
                                    continue
                            if cant_go[r][c+1]:
                                if (r+1, c+1) in cant_go[r][c+1]:
                                    continue
                            vi[nr][nc]=1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))
                        else:
                            if cant_go[r][c]:
                                if (r+1, c) in cant_go[r][c]:
                                    continue
                            vi[nr][nc] = 1
                            degree_up[nr][nc] += degree
                            q.append((nr,nc,di,degree-1))

    return degree_up

for r,c,di in warmers:
    degree_up = get_warm_area(r,c,di,degree_up)
    for d in degree_up:
        print(d)
    print()


while True:

    for r in range(n):
        for c in range(m):
            home[r][c] += degree_up[r][c]

    control_degree = [[0]*m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if home[r][c] > 0:
                tmp = home[r][c]//4
                real_tmp = 0

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    if 0 <= nr < n and 0 <= nc < m:

                        if cant_go[r][c]:
                            if (nr, nc) in cant_go[r][c]:
                                continue
                        if home[r][c] > home[nr][nc]:
                            control_degree[nr][nc] += tmp
                            real_tmp += tmp

                control_degree[r][c] -= real_tmp


    for r in range(n):
        for c in range(m):
            home[r][c] += control_degree[r][c]
            if home[r][c] < 0:
                home[r][c] = 0

    for r in range(n):
        if home[r][0] > 0:
            home[r][0] -=1
        if home[r][m-1] > 0:
            home[r][m-1] -=1
    for c in range(m):
        if home[0][c] > 0:
            home[0][c] -=1
        if home[n-1][c] > 0:
            home[n-1][c] -=1
    ans += 1

    is_ok = True
    for r,c in detect_spot:
        if home[r][c] < k:
            is_ok = False
            break

    if is_ok:
        break

for h in home:
    print(h)
print()

print(ans)