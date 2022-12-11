from collections import deque

n, m = map(int, input().split())

game_map = [list(map(int, input().split())) for _ in range(n)]
vi = [[0]*m for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y):
    vi[x][y] = 1
    q = deque([(x,y,1,game_map[x][y])])

    while q:
        r,c,cnt,items = q.popleft()
        print(r,c,cnt)

        if r == n-1 and c == m-1:
            return cnt - 1

        for i in range(4):
            nr,nc = r,c
            dist = items

            for j in range(1,dist+1):
                nr, nc = r + dr[i]*dist, c + dr[i]*dist
                if 0 <= nr + dr[i]< n and 0 <= nc + dc[i]< m:
                    nc += dc[i]
                    dist -= 1

            if not vi[nr][nc]:
                vi[nr][nc] = 1
                q.append((nr,nc,cnt+1,game_map[nr][nc]))

answer = bfs(0,0)
print(answer)