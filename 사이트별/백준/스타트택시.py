from collections import deque

n, m, e = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sx,sy = map(int, input().split())
sx,sy = sx-1,sy-1
customers = []
customers_targets = [[0]*n for _ in range(n)]
is_ok = True
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for _ in range(m):
    cx, cy, tx, ty = map(int, input().split())
    cx,cy,tx,ty = cx-1,cy-1,tx-1,ty-1
    customers.append((cx, cy))
    customers_targets[cx][cy] = (tx, ty)

def find_customer(sr,sc,e):
    global is_ok

    vi = [[0]*n for _ in range(n)]
    vi[sr][sc] = 1
    can_go = []
    q = deque([(sr,sc,e,0)])
    min_dist = 1e9
    final_e = 0

    while q:
        r,c,e,dist = q.popleft()

        if (r,c) in customers and e >= 0:
            if min_dist > dist:
                min_dist = dist
                can_go = [(r,c)]
                final_e = e
            elif min_dist == dist:
                can_go.append((r,c))
                final_e = e

        for i in range(4):
            nr,nc = r + dr[i],c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if vi[nr][nc] == 0 and board[nr][nc] == 0:
                    vi[nr][nc] = 1
                    q.append((nr,nc,e-1,dist+1))

    if not can_go:
        return -1,-1,-1
    can_go.sort(key = lambda x: (x[0],x[1]))
    return can_go[0][0],can_go[0][1],final_e

def find_customer_target(sr,sc,e,tx,ty):
    global is_ok

    vi = [[0]*n for _ in range(n)]
    vi[sr][sc] = 1
    can_go = []
    q = deque([(sr,sc,e,0)])
    final_e = 0
    min_dist = 0

    while q:
        r,c,e,dist = q.popleft()

        if r == tx and c == ty and e >= 0:
            can_go.append((r,c,e))
            final_e = e
            min_dist = dist
            break

        for i in range(4):
            nr,nc = r + dr[i],c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if vi[nr][nc] == 0 and board[nr][nc] == 0:
                    vi[nr][nc] = 1
                    q.append((nr,nc,e-1,dist+1))

    if not can_go:
        return -1,-1,-1

    return can_go[0][0],can_go[0][1],final_e + min_dist*2

while customers:
    sx,sy,e = find_customer(sx,sy,e)

    if sx == -1:
        is_ok = False
        break

    customers.remove((sx,sy))
    tx,ty = customers_targets[sx][sy][0],customers_targets[sx][sy][1]
    sx,sy,e = find_customer_target(sx,sy,e,tx,ty)

    if sx == -1:
        is_ok = False
        break

if is_ok:
    print(e)
else:
    print(-1)