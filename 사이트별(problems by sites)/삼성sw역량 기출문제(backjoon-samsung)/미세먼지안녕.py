from collections import deque

r,c,t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
cr1,cc1,cr2,cc2 = 0,0,0,0
di = [(-1,0),(1,0),(0,1),(0,-1)]
ans = 0

for x in range(r):
    for y in range(c):
        if room[x][y] == -1:
            cr2, cc2 = x,y

cr1,cc1 = cr2-1, cc2

while t > 0:
    dusts = deque([])

    for x in range(r):
        for y in range(c):
            if 0 < room[x][y]:
                dusts.append((x,y))

    while dusts:
        x, y = dusts.popleft()
        cnt = 0
        for dx, dy in di:
            nx,ny = x + dx, y + dy

            if 0<= nx < r and 0<= ny < c:
                if room[nx][ny] != -1:
                    cnt += 1
                    exDust = room[x][y] // 5
                    room[nx][ny] += exDust

        room[x][y] -= exDust*cnt


    tmp1 = room[cr1][-1]
    for j in range(c-1,1,-1):
        room[cr1][j] = room[cr1][j-1]
    room[cr1][1] = 0

    tmp2 = room[0][c-1]
    for j in range(0,cr1-1):
        room[j][-1] = room[j+1][-1]

    room[cr1 - 1][-1] = tmp1
    tmp3 = room[0][0]
    for j in range(c-2):
        room[0][j] = room[0][j+1]
    room[0][-2] = tmp2

    for j in range(cr1-1,-1,-1):
        room[j][0] = room[j-1][0]
    room[1][0] = tmp3

    for a in room:
        print(a)
    print()

    ## cycle
    tmp1 = room[cr2][-1]
    for j in range(c-1, 1, -1):
        room[cr2][j] = room[cr2][j - 1]
    room[cr2][1] = 0
    tmp2 = room[-1][-1]

    for j in range(r-1,cr2,-1):
        room[j][-1] = room[j - 1][-1]
    room[cr2 + 1][-1] = tmp1

    tmp3 = room[r-1][0]
    for j in range(c - 2):
        room[-1][j] = room[-1][j + 1]
    room[-1][c - 2] = tmp2


    room[-2][0] = tmp3
    for j in range(cr2 + 1, r-1):
        room[j][0] = room[j + 1][0]

    t -= 1


for r in room:
    ans += sum(r)

for a in room:
    print(a)

print(ans +2)






