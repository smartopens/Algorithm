from collections import deque
 
n, m = map(int, input().split(' '))
r,c,d = map(int, input().split(' '))
area = [list(map(int, input().split(' '))) for _ in range(n)]
vi = [[False]*m for _ in range(n)]

def bfs(r,c,d1,vi):
    global area, n,m
    q = deque([(r,c,d1)])
    di = [(-1,0),(0,1),(1,0),(0,-1)]
    vi[r][c] = True

    while q:
        x,y,d = q.popleft()
        isBreak = False
        isStop = False

        for _ in range(4):
            if isBreak:
                  break

            d = (d+3)%4
            nx,ny = x + di[d][0], y + di[d][1]

            if 0 <= nx < n and 0 <= ny < m:
                if area[nx][ny] != 1 and not vi[nx][ny]:
                    isBreak = True
                    vi[nx][ny] = True
                    q.append([nx,ny,d])

        if not isBreak:
            tempd = d
            tempd = (tempd -2)%4
            nx, ny = x + di[tempd][0], y + di[tempd][1]

            if 0 <= nx < n and 0 <= ny < m:
                if area[nx][ny] != 1:
                    q.append([nx, ny, d])
                else:
                    isStop = True

        if isStop:
            break
    return

bfs(r,c,d,vi)
ans = 0


for v in vi:
    ans += v.count(True)

print(ans)