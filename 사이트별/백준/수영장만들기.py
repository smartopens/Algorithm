from collections import deque
import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
water_pool = [list(map(int, input().strip())) for _ in range(n)]
height_group = [[] for _ in range(10)]
will_be_watered = [[0]*m for _ in range(n)]
water_vi = [[0]*m for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
max_height = 0
answer = 0

for i in water_pool:
    for j in i:
        max_height = max(max_height,j)

def put_water(x,y,height):
    global answer

    group_vi[x][y] = 1
    water_target = deque([])
    water_target.append((x,y))
    q = deque([(x,y)])
    water_height = 1e9
    is_ok = True

    while q:
        r,c = q.popleft()

        if is_ok and (r == 0 or c == 0 or r == n - 1 or c == m - 1) and water_pool[r][c]:
            is_ok = False

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and group_vi[nr][nc] == 0:

                if water_pool[nr][nc] == height:
                    group_vi[nr][nc] = 1
                    water_target.append((nr,nc))
                    q.append((nr,nc))
                else:
                    if height < water_pool[nr][nc] < water_height:
                        water_height = water_pool[nr][nc]
                    elif water_pool[nr][nc] < height:
                        is_ok = False


    if not is_ok:
        return

    answer += len(water_target)*(water_height - height)
    for r,c in water_target:
        water_pool[r][c] = water_height

    return

def stack_water(group,height):
    global answer
    is_ok = True
    cnt = 0
    max_water = 1e9
    tmp = deque([])

    for r,c in group:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if water_pool[nr][nc] >= height or will_be_watered[nr][nc] == 1\
                        :

                    if (will_be_watered[nr][nc] == 0
                    and (nr,nc) not in group):
                        max_water = min(max_water,water_pool[nr][nc])

                else:
                    return
            else:
                return
        tmp.append((r, c))

    if (max_water-height) <= 0 or max_water == 1e9:
        return
    answer += (max_water-height)*len(tmp)
    for r,c in tmp:
        will_be_watered[r][c] = 1
        water_pool[r][c] = max_water

    height_group[max_water].append(tmp)
    return

for i in range(1,max_height+1):
    group_vi = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if group_vi[r][c] == 0 and water_pool[r][c] == i:
                put_water(r,c,i)

print(answer)