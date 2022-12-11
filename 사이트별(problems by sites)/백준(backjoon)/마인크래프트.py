from copy import deepcopy
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
ans_list = []
min_h = 1e9
max_h = 0


for i in range(0,257):
    time_tmp = 0

    for r in range(n):
        for c in range(m):
            if ground[r][c] > i:
                time_tmp += (ground[r][c]-i)*2
                b += 1

    isOk = True

    for r in range(n):
        if not isOk:
            break

        for c in range(m):
            if ground[r][c] < i:
                if b + (ground[r][c]-i) < 0:
                    isOk = False
                    break

                b += (ground[r][c]-i)
                time_tmp += abs((ground[r][c]-i))

    if not isOk:
        continue

    ans_list.append((time_tmp,i))

ans_list.sort(key= lambda x:(x[0], -x[1]))

print(ans_list[0][0], ans_list[0][1])