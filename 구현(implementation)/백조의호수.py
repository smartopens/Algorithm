from collections import deque

r, c = map(int, input().split())
lake = list()

for _ in range(r):
    lake.append(list(input()))

def updateMap(q):
    global lake
    visited = [[-1] * c for _ in range(r)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0<= nx < r and 0 <= ny < c and visited[nx][ny] == -1:
                if lake[nx][ny] == ".":
                    q.append((nx,ny))
                    visited[nx][ny] += 1

                elif lake[nx][ny] == "X" and visited[nx][ny] == -1:
                    lake[nx][ny] = "."
                    visited[nx][ny] += 1
    return


def findBird(lake,start):
    visited = [[False]*c for _ in range(r)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque([start])

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0<= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if lake[nx][ny] != "X":
                    if lake[nx][ny] == "L":
                        return True
                    q.append((nx,ny))
    return False


for i in range(r):
    for j in range(c):
        if lake[i][j] == "L":
            start = (i,j)
            break

success = False
answer = 0
idx = 0

q = deque([])



while True:
    success = findBird(lake, start)

    for i in range(r):
        for j in range(c):
            if lake[i][j] == ".":
                q.append((i, j))
    if success:
        break
    else:
        updateMap(q)
        answer += 1

print(answer)