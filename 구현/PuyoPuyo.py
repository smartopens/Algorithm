from collections import deque

def move(s, puyoMap):
    global  puyoColors
    x,y = s

    while x+1 <= 11 and puyoMap[x+1][y] == '.':
        x += 1

    return x,y

def changeMap(puyoMap):
    global puyoColors

    for i in range(10, -1, -1):
        for j in range(6):
            if puyoMap[i][j] in puyoColors and puyoMap[i+1][j] == ".":
                nx, ny = move((i,j), puyoMap)
                puyoMap[nx][ny] = puyoMap[i][j]
                puyoMap[i][j] = '.'

    return puyoMap

def countPuyo(s, c, visited, puyoMap):

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    q= deque([])
    q.append((s,1))
    slist = list()
    totalCnt = 1

    while q:
        start, cnt = q.popleft()
        x,y = start
        visited[x][y] = True
        slist.append((x,y))

        for dx, dy in directions:
            nx,ny = x+ dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6:
                if visited[nx][ny] == False:
                    if puyoMap[nx][ny] == c:
                        visited[nx][ny] = True
                        totalCnt += 1
                        q.append(((nx,ny), cnt+1))

    return totalCnt, slist, visited

def detectEvent():
    global isBreak, puyoMap, puyoColors
    visited = [[False]*6 for _ in range(12)]
    q= deque([])

    for i in range(12):
        for j in range(6):
            if puyoMap[i][j] in puyoColors and not visited[i][j]:
                cnt, temp, visited = countPuyo((i,j),puyoMap[i][j],visited, puyoMap)

                if len(temp) >= 4:
                    q.extend(temp)
                    isBreak = True
    return q

puyoMap = list()
puyoColors = ["R", "G","B","P","Y"]

for _ in range(12):
    puyoMap.append(list(input()))

isBreak = False
ans = 0

while True:
    queue = detectEvent()
    if queue:
        for q in queue:
            x,y = q
            puyoMap[x][y] = '.'

    if not isBreak:
        break
    else:
        ans += 1
        puyoMap = changeMap(puyoMap)
    isBreak = False

print(ans)

# from collections import deque
# import sys
#
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def bfs(x, y, flag):
#     q = deque()
#     c = [[0]*6 for _ in range(12)]
#     q.append([x, y])
#     cnt = 1
#     c[x][y] = cnt
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < 12 and 0 <= ny < 6:
#                 if a[nx][ny] == a[x][y] and c[nx][ny] == 0:
#                     cnt += 1
#                     c[nx][ny] = 1
#                     q.append([nx, ny])
#
#     if cnt >= 4:
#         print(cnt, c)
#         flag += 1
#         for i in range(12):
#             for j in range(6):
#                 if c[i][j] == 1:
#                     a[i][j] = '.'
#     return flag
#
# def check_fall():
#     for i in range(10, -1, -1):
#         for j in range(6):
#             if a[i][j] != '.' and a[i+1][j] == '.':
#                 for k in range(i+1, 12):
#                     if k == 11 and a[k][j] == '.':
#                         a[k][j] = a[i][j]
#                     elif a[k][j] != '.':
#                         a[k-1][j] = a[i][j]
#                         break
#                 a[i][j] = '.'
#
# a = [list(map(str, input().strip())) for _ in range(12)]
#
# ans = 0
# while True:
#     cnt = 0
#     for i in range(12):
#         for j in range(6):
#             if a[i][j] != '.':
#                 cnt = bfs(i, j, cnt)
#     if cnt == 0:
#         print(ans)
#         break
#     else:
#         ans += 1
#     check_fall()


