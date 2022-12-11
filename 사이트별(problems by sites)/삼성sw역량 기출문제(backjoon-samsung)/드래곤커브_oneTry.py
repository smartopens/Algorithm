from collections import deque

di = [(1,0),(0,-1),(-1,0),(0,1)]

def findLast(sq,q,lastX,lastY):
    dis = 0
    lx, ly = 0,0
    for sqi in sq:
        if sqi not in q:
            q.append(sqi)

    for x,y in q:
        temp = abs(lastX- x) + abs(lastY- y)
        if dis < temp:
            dis = temp
            lx, ly = x, y

    q.remove((lx,ly))
    q.append((lx,ly))
    return q

def turnCycle(sq):
    maxL = 0
    pX,pY = 0,0
    mX,mY = 0,0
    lastX, lastY = sq[-1][0], sq[-1][1]
    dis = (0,0)

    for x,y in sq:
        if x >= 0:
            pX = max(pX,x)
        if y >= 0:
            pY = max(pY,y)
        if x <= 0:
            mX = max(-mX,x)
        if y <= 0:
            mY = max(-mY,y)
    maxL = max(pX+mX, pY+mY) + 1

    tArr = [[0]*maxL for _ in range(maxL)]
    cArr = [x[:] for x in tArr]


    for x,y in sq:
        tArr[x][y] = 1


    for r in range(maxL):
        for c in range(maxL):
            cArr[c][maxL-1-r] = tArr[r][c]
            if r == lastX and c == lastY:
                dis = (r-c ,c - (maxL-1-r))

                print(r,c)
                print(c, (maxL-1-r))
                print(dis)


    q = deque()
    for r in range(maxL):
        for c in range(maxL):
            if cArr[r][c]:
                q.append((r + dis[0],c + dis[1]))

    for qi in q:
        print(qi)

    q = findLast(sq,q,lastX,lastY)
    tArr = [[0] * 30 for _ in range(30)]


    return q

def doDragon(d,g):

    return

def drawMap(sx,sy,d,g):
    global wholeMap
    nx,ny = sx + d[0], sy + d[1]
    q = deque([(sx,sy),(nx, ny)])

    while g >0:
        print(q,"halo",g)
        q = turnCycle(q)
        g -= 1
    print(q, "q2", g)
    print("findq")
    for q1 in q:
        print(q1)
    while q:
        x, y = q.popleft()
        wholeMap[x][y] = 1
    print("ggg")
    return


n = int(input())
wholeMap = [[0] * 100 for _ in range(100)]
ans = 0
sdi = [(0,1),(1,1),(1,0)]


# oneCount = 0
#
# for w in wholeMap:
#     oneCount += w.count(1)
#     print(w)
# print(oneCount)

for _ in range(n):

    sx,sy,d,g = map(int, input().split(' '))
    #doDragon(d,g)
    drawMap(sy,sx,di[d],g)

for w in wholeMap:
    print(w)

for r in range(100):
    for c in range(100):
        isOk = True
        if wholeMap[r][c] == 1:
            for dx,dy in sdi:
                if not wholeMap[r+dx][c+dy]:
                    isOk = False
                    break

            if isOk:
                ans += 1


print(ans,"a")
