import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virusQ = deque([])
ans = sys.maxsize
di = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virusQ.append((i,j))

for com in combinations(virusQ,m):
    q = deque([])
    arrTmp = deepcopy(arr)
    vi = [[0]*n for _ in range(n)]

    for c in com:
        q.append((c[0],c[1],0))
        vi[c[0]][c[1]] = 1

    check = 0
    total = 0

    while q:
        x, y, time = q.popleft()

        for dx, dy in di:
            nx,ny = x+dx, y+dy

            if 0<= nx < n and 0<= ny < n and vi[nx][ny] == 0:
                if arrTmp[nx][ny] != 1:
                    if arrTmp[nx][ny] == 0:
                        total = time + 1
                        arrTmp[nx][ny] = 2
                    vi[nx][ny] = 1
                    q.append((nx,ny,time+1))

    for i in arrTmp:
        check += i.count(0)

    if check == 0:
        ans = min(ans, total)


if ans == sys.maxsize:
    ans = -1
print(ans)






