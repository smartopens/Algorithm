from collections import deque

n, m = map(int, input().split())
gameMap = []
checkMap = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def move(x,y,dx,dy,c):
    global gameMap

    while gameMap[x+dx][y+dy] != "#" and gameMap[x][y] != "O":
        x = x + dx
        y = y + dy
        c = c + 1

    return x, y, c

def bfs(q):
    global ans, checkMap,gameMap
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        red, blue, cnt = q.popleft()
        rx, ry = red
        bx, by = blue

        if cnt > 10:
            ans = -1
            return

        checkMap[rx][ry][bx][by] = True

        for i in directions:
            nrx, nry, nrc = move(rx,ry,i[0],i[1],0)
            nbx, nby, nbc = move(bx,by,i[0],i[1],0)

            if gameMap[nbx][nby] == "O":
                continue
            if gameMap[nrx][nry] == "O":
                ans = cnt
                return

            if nrx == nbx and nry == nby:
                if nrc > nbc:
                    nrx, nry = nrx - i[0], nry - i[1]
                else:
                    nbx, nby = nbx - i[0], nby - i[1]

            if not checkMap[nrx][nry][nbx][nby]:
                q.append([(nrx,nry), (nbx,nby), cnt+1])

    ans = -1
    return

for _ in range(n):
    gameMap.append(list(input()))

redPos = (0, 0)
bluePos = (0, 0)
ans = 1000

for i in range(n):
    for j in range(m):
        if gameMap[i][j] == "R":
            redPos = (i, j)
        if gameMap[i][j] == "B":
            bluePos = (i, j)

q = deque([])
q.append([redPos, bluePos,1])
bfs(q)
print(ans)