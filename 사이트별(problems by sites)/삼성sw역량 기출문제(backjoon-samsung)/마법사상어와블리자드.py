from copy import deepcopy

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
magics = [list(map(int, input().split())) for _ in range(m)]
sx, sy = n // 2, n // 2
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
magic_dr = [-1, 1, 0, 0]
magic_dc = [0, 0, -1, 1]
doll_road = []
dist = 1
is_done = False
ans = 0

while True:
    for di in range(4):
        for _ in range(dist):
            sx, sy = sx + dr[di], sy + dc[di]
            doll_road.append((sx, sy))

            if sx == 0 and sy == 0:
                is_done = True
                break

        if (di + 1) % 2 == 0:
            dist += 1

        if is_done:
            break

    if is_done:
        break

sx, sy = n // 2, n // 2

for di, si in magics:
    di -= 1
    for dist in range(1, si + 1):

        nr, nc = sx + magic_dr[di] * dist, sy + magic_dc[di] * dist
        if 0 <= nr < n and 0 <= nc < n:
            array[nr][nc] = 0
        else:
            break

    road_stack = []
    for i in range(len(doll_road)):
        r, c = doll_road[i]

        if array[r][c] != 0:
            road_stack.append(array[r][c])

    idx = 0
    for i in range(len(doll_road)):
        r, c = doll_road[i]
        if idx == len(road_stack):
            array[r][c] = 0
            continue

        array[r][c] = road_stack[i]
        idx += 1


    bomb_doll = 0
    doll_cnt = 1


    while True:

        bomb_list = []
        doll_cnt = 1
        for i in range(1,len(doll_road)):
            r, c = doll_road[i]
            nr, nc = doll_road[i-1]

            if array[r][c] == array[nr][nc]:
                doll_cnt += 1
            else:
                if doll_cnt >= 4:

                    for j in range(1,doll_cnt+1):
                        x, y = doll_road[i-j]
                        bomb_list.append((x,y))

                doll_cnt = 1

        if bomb_list:
            for bomb in bomb_list:
                r,c = bomb

                if array[r][c] == 1:
                    ans += 1
                elif array[r][c] == 2:
                    ans += 2
                elif array[r][c] == 3:
                    ans += 3
                array[r][c] = 0

            road_stack = []
            for i in range(len(doll_road)):
                r, c = doll_road[i]

                if array[r][c] != 0:
                    road_stack.append(array[r][c])

            idx = 0
            for i in range(len(doll_road)):
                r, c = doll_road[i]
                if idx == len(road_stack):
                    array[r][c] = 0
                    continue

                array[r][c] = road_stack[i]
                idx += 1

        else:
            break

    new_doll_list = []
    new_cnt = 1
    new_num = 0

    for i in range(len(doll_road) - 1):
        r, c = doll_road[i]
        nr, nc = doll_road[i + 1]
        new_num = array[r][c]

        if array[r][c] == array[nr][nc]:
            new_cnt += 1
        else:
            new_doll_list.append(new_cnt)
            new_doll_list.append(new_num)
            new_cnt = 1
    next = False
    for i in range(len(doll_road) - 1):
        r, c = doll_road[i]
        if len(new_doll_list) <= i:
            next = True
        if not next:
            array[r][c] = new_doll_list[i]
        else:
            array[r][c] = 0

print(ans)