from collections import deque

n, m = map(int, input().split())
mirror = []
keys = []
mirrorKeys = ['a','b','c','d','e','f']
mirrorDoors = ['A','B','C','D','E','F']
minCnt = 10000

def goToMoon(start):
    global keys, mirror, mirrorKeys, mirrorDoors, minCnt

    visited = [[False]*m for _ in range(n)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque([(start,0)])
    visited[start[0]][start[1]] = True


    while q:
        s, cnt = q.popleft()
        x,y = s
        visited[x][y] = True
        print(visited)


        for dx,dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if mirror[nx][ny] != "#":

                    if mirror[nx][ny] in mirrorDoors and mirror[nx][ny] in keys:
                        q.append(((nx,ny),cnt+1))
                        print(mirror[nx][ny],"oo")
                        print(keys)
                        print(cnt)

                    elif mirror[nx][ny] in mirrorKeys:
                        visited = [[False]*m for _ in range(n)]
                        keys.append(mirror[nx][ny].upper())
                        q.append(((nx, ny), cnt + 1))
                        visited[nx][ny] = True

                        print(mirror[nx][ny])
                        print(cnt)

                    elif mirror[nx][ny] == "." or mirror[nx][ny] == "0":
                        q.append(((nx, ny), cnt + 1))
                        print(cnt+1, mirror[nx][ny])
                    elif mirror[nx][ny] == "1":
                        cnt += 1
                        print(cnt)
                        minCnt = min(minCnt, cnt)
                        return True

    return False

for _ in range(n):
    mirror.append(input())

start = (0,0)
for i in range(n):
    for j in range(m):
        if mirror[i][j] == "0":
            start = (i,j)
            break

if goToMoon(start):
    print(minCnt)
else:
    print(-1)
