from collections import deque

di = [(1,0),(0,-1),(-1,0),(0,1)]

def doDragon(q):
    qR = deque(reversed(q))

    for qri in range(len(qR)):
        qR[qri] += 1
        if qR[qri] > 3:
            qR[qri] = 0
    q.extend(qR)

    return q

def drawMap(sx,sy,sd,g):
    global wholeMap
    q = deque([sd])
    wholeMap[sy][sx] = 1

    while g > 0:
        q = doDragon(q)
        g -= 1

    while q:
        d = q.popleft()
        dx,dy = di[d]
        nx, ny = sx + dx, sy + dy
        wholeMap[ny][nx] = 1
        sx, sy = nx, ny

    return


n = int(input())
wholeMap = [[0] * 101 for _ in range(101)]
ans = 0
sdi = [(1,0),(0,1),(1,1)]

for _ in range(n):
    sx,sy,d,g = map(int, input().split(' '))
    drawMap(sx,sy,d,g)

isOk = 0
for r in range(101):
    for c in range(101):
        isOk = 0
        if wholeMap[r][c] == 1:
            for dx,dy in sdi:
                if 0<= r+dy <101 and 0<= c+dx < 101 and wholeMap[r+dy][c+dx]:
                    isOk += 1

            if isOk == 3:
                ans += 1
                isOk = 0

print(ans)
