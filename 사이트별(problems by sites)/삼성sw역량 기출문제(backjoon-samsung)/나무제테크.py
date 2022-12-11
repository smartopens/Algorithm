from collections import deque
from copy import deepcopy

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ground = [[5] * n for _ in range(n)]
treeList = [[[]] * n for _ in range(n)]
ans = 0

for _ in range(m):
    r, c, tree = map(int, input().split())
    r -= 1
    c -= 1
    treeList[r][c] = [tree]

for t in treeList:
    print(t)

while k > 0:
    for tr in treeList:
        for t in tr:
            t.sort()

    deadQ = deque([])
    di = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    for r in range(n):
        for c in range(n):
            if treeList[r][c]:
                worth = ground[r][c]
                tidx = 0
                tmp = deepcopy(treeList[r][c])
                while worth > 0 and tmp:
                    dead = tmp.pop(0)
                    worth -= dead

                    if worth < 0:
                        deadQ.append([r, c, dead])
                        break
                    tidx += 1

                ground[r][c] = worth

                for _ in range(len(treeList[r][c]) - tidx):
                    treeList[r][c].pop()


                if treeList[r][c]:
                    for t2 in range(len(treeList[r][c])):
                        treeList[r][c][t2] += 1

    while deadQ:
        r, c, w = deadQ.popleft()
        w = w // 2
        ground[r][c] += w

    for r in range(n):
        for c in range(n):
            if treeList[r][c]:
                tnum = 0
                for t in treeList[r][c]:
                    if t % 5 == 0:
                        tnum += 1
                for _ in range(tnum):
                    for dr, dc in di:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            if treeList[nr][nc]:
                                treeList[nr][nc].append(1)
                            else:
                                treeList[nr][nc] = [1]
    for t in treeList:
        print(t)
    print("t")

    for r in range(n):
        for c in range(n):
            ground[r][c] += arr[r][c]

    for g in ground:
        print(g)
    print("g")

    k -= 1

for t in treeList:
    print(t)

for tr in treeList:
    for t in tr:
        ans += len(t)

print(ans)