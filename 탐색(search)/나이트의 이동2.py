import sys
from collections import deque
t = int(input())

def moveTo(x,y,tx,ty,vi):
    global n,ans
    directions = [(-2,-1),(-1,-2),(1,-2),(2,-1),
                  (-2,1),(-1,2),(1,2),(2,1)]
    q = deque([(x,y,0)])

    while q:
        x,y, cnt = q.popleft()

        if x == tx and y == ty:
            ans = min(ans,cnt)
            return
        print(x,y,cnt)
        print(vi)
        vi[x][y] = 0

        for dx,dy in directions:
            nx,ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n:
                if vi[nx][ny]:
                    vi[nx][ny] = 0
                    q.append((nx,ny,cnt+1))



for _ in range(t):
    n = int(input())
    x, y = map(int, input().split(' '))
    tx, ty = map(int, input().split(' '))

    vi = [[1]*n for _ in range(n)]
    ans = sys.maxsize
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (-2, 1), (-1, 2), (1, 2), (2, 1)]
    q = deque([(x,y,0)])
    while q:
        x,y,cnt = q.popleft()

        if x == tx and y == ty:
            ans = min(ans,cnt)
            break

        print(x,y,cnt)
        print(vi)
        vi[x][y] = 0

        for dx,dy in directions:
            nx,ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n:
                if vi[nx][ny]:
                    vi[nx][ny] = 0
                    q.append((nx,ny,cnt+1))

    print(ans)
