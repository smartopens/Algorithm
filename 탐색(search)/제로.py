import sys
sys.setrecursionlimit(100000)

n = int(input())
map_ = [list(map(int,input().split(' '))) for _ in range(n)]
maxNum = 0
ans = 0

for i in range(n):
    maxNum = max(map_[i])

def countNum(r,c):
    global vi, ans, map_
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    vi[r][c] = 0

    for dx,dy in directions:
        nx, ny = r + dx, c + dy

        if 0 <= nx < n and 0 <= ny < n:
            if vi[nx][ny]:
                countNum(nx,ny)

    return

for num in range(maxNum):
    vi = [[1] * n for _ in range(n)]

    for vr in range(n):
        for vc in range(n):
            if map_[vr][vc] <= num:
                vi[vr][vc] = 0

    tempAns = 0
    for r in range(n):
        for c in range(n):
            if vi[r][c]:
                countNum(r,c)
                tempAns += 1

    ans = max(ans, tempAns)

print(ans)
