from collections import deque

n = int(input())
map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split(' '))))
ans = 0
q = deque()

def merge(i,j,di,dj):
    while q:
        x = q.popleft()
        if not map_[i][j]:
            map_[i][j] = x
        elif map_[i][j] == x:
            map_[i][j] = x*2
            i += di
            j += dj
        else:
            i += di
            j += dj
            map_[i][j] = x
    return

def get(i,j):
    if map_[i][j]:
        q.append(map_[i][j])
        map_[i][j] = 0

    return

def move(k):
    # 아래에서 위로 이동
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i,j)
            merge(0,j,1,0)
    # 위에서 아래로 이동
    elif k == 1:
        for j in range(n):
            for i in range(n-1,-1,-1):
                get(i,j)
            merge(n-1,j,-1,0)
    # 오른쪽에서 왼쪽로 이동
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i,j)
            merge(i,0,0,1)
    # 왼쪽에서 오른쪽으로 이동
    else:
        for i in range(n):
            for j in range(n-1,-1,-1):
                get(i,j)
            merge(i,n-1,0,-1)



def solve(cnt):
    global ans, map_

    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, map_[i][j])
        return
    # deepcopy map_
    m = [i[:] for i in map_]

    for k in range(4):
        move(k)
        solve(cnt+1)
        map_ = [i[:] for i in m]

solve(0)
print(ans)
