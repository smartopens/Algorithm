from collections import deque

def bfs(start):
    global visited, bScore, wScore, battleMap,n,m
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    fColor = battleMap[start[0]][start[1]]
    cnt = 1
    q = deque([(start)])

    while q:
        s = q.popleft()
        x,y = s
        visited[x][y] = True

        for dx,dy in directions:
            nx, ny = x + dx, y + dy

            if 0<= nx < m and 0<= ny < n and not visited[nx][ny]:
                if battleMap[nx][ny] == fColor:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append(((nx,ny)))

    if fColor == "B":
        bScore += cnt**2
    else:
        wScore += cnt**2

    return

n, m = map(int, input().split())
battleMap = []
visited = [[False]*n for _ in range(m)]
bScore = 0
wScore = 0

for _ in range(m):
    battleMap.append(list(input()))

for r in range(m):
    for c in range(n):
        if not visited[r][c]:
            bfs((r,c))

print(wScore,bScore)