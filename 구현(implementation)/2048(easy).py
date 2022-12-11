from collections import deque

n = int(input())
map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split(' '))))
ans = 0


def move(x, y, tempMap, case):
    dx, dy = case

    while 0 <= x + dx < n and 0 <= y + dy < n and tempMap[x + dx][y + dy] != 0:
        x = x + dx
        y = y + dy

    return x,y


def bfs(map_):
    global ans
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    checkMore = [[0] * n for _ in range(n)]

    q = deque([(0, map_)])
    while q:
        cnt, map1 = q.popleft()

        if cnt == 5:
            for i in range(n):
                for j in range(n):
                    ans = max(ans, map1[i][j])
            print(map1)
            return

        for k in range(4):
            checkMore = [[0] * n for _ in range(n)]
            tempMap = map1

            if k == 0 or k == 3:
                for i in range(n):
                    for j in range(n):
                        if not checkMore[i][j]:
                            x, y = move(i, j, tempMap, directions[k])
                            checkMore[i][j] += 1
                            dx, dy = directions[k]

                            if 0 <= x + dx < n and 0 <= y + dy < n and tempMap[x+dx][y+dy] == tempMap[i][j] and checkMore[i][j] != 2:
                                tempMap[x+dx][y+dy] = tempMap[i][j]*2
                                checkMore[x+dx][y+dy] += 1
                                tempMap[i][j] = 0
                            else:
                                if (x,y) != (i,j):
                                    tempMap[x][y] = tempMap[i][j]
                                    tempMap[i][j] = 0

                            print(tempMap)
                q.append([cnt+1,tempMap])


            else:
                for i in range(n - 1, -1, -1):
                    for j in range(n - 1, -1, -1):
                        if not checkMore[i][j]:
                            x, y = move(i, j, tempMap, directions[k])
                            checkMore[i][j] += 1
                            dx, dy = directions[k]

                            if 0 <= x + dx < n and 0 <= y + dy < n and tempMap[x + dx][y + dy] == tempMap[i][j] and checkMore[i][j] != 2:
                                tempMap[x + dx][y + dy] = tempMap[i][j] * 2
                                checkMore[x+dx][y+dy] += 1
                                tempMap[i][j] = 0
                            else:
                                tempMap[x][y] = tempMap[i][j]
                                tempMap[i][j] = 0

                q.append([cnt + 1, tempMap])
    return


bfs(map_)
print(ans)
