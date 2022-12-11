from collections import deque
import math

n, l, r2 = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
q = deque()
unions = [[0]*n for _ in range(n)]

def findUnion():
    global q, unions, arr

    di = [(-1,0),(1,0),(0,1),(0,-1)]
    isFind = False

    for r in range(n):
        for c in range(n):
            for dr, dc in di:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    dis = abs(arr[nr][nc] - arr[r][c])
                    if l <= dis <= r2:
                        unions[r][c] = 1
                        unions[nr][nc] = 1
                        isFind = True
    return isFind

def updateArr(r,c):
    global unions,total,cNum, arr

    di = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    total = arr[r][c]
    q = deque([(r,c)])
    upQ = deque([(r,c)])
    unions[r][c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in di:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if unions[nr][nc]:
                    unions[nr][nc] = 0
                    total += arr[nr][nc]
                    cNum += 1
                    q.append((nr,nc))
                    upQ.append((nr,nc))
    cNum = len(upQ)
    mNum = math.floor(total / cNum)

    while upQ:
        r,c = upQ.popleft()
        arr[r][c] = mNum

    return


while findUnion():

    for r in range(n):
        for c in range(n):
            if unions[r][c]:
                total = 0
                cNum = 1
                updateArr(r,c)
    for a in arr:
        print(a)
    print()
    ans += 1

print(ans)