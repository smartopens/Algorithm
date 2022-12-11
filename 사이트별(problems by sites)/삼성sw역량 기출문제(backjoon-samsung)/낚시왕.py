from copy import deepcopy
br, bc, m = map(int, input().split())
sea = [[0] * bc for _ in range(br)]
ans = 0
di = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def move(r, c, s, d):
    nr, nc = r, c
    if d== 0 or d== 1:
        s = s%(br+1)
    else:
        s = s%(bc+1)

    for _ in range(s):
        nr += di[d][0]
        nc += di[d][1]

        if nr < 0:
            nr = 1
            d = 1
        elif nr > br - 1:
            nr = br - 2
            d = 0

        if nc < 0:
            nc = 1
            d = 2

        elif nc > bc - 1:
            nc = bc - 2
            d = 3

    return nr, nc, d


for i in range(m):
    r, c, s, d, z = map(int, input().split())
    sea[r - 1][c - 1] = [s, d - 1, z]

for sec in range(bc):

    for r in range(br):
        if sea[r][sec] != 0:
            ans += sea[r][sec][2]
            sea[r][sec] = 0
            break

    tmp = [[0] * bc for _ in range(br)]
    for r in range(br):
        for c in range(bc):
            if sea[r][c] != 0:
                s, d, z = sea[r][c]
                nr, nc, d2 = move(r, c, s, d)

                if tmp[nr][nc] != 0:
                    if tmp[nr][nc][2] < z:
                        tmp[nr][nc] = [s, d2, z]
                else:
                    tmp[nr][nc] = [s, d2, z]


    sea = deepcopy(tmp)


print(ans)
