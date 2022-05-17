from collections import deque

n, m, x, y, k = map(int, input().split(' '))
map_ = []
doll = [[0]*3 for _ in range(4)]
direction = [(0,1),(0,-1),(-1,0),(1,0)]
dx,dy = 1,1

i = 0

for _ in range(n):
    map_.append(list(map(int, input().split(' '))))

opers = list(map(int, input().split(' ')))

while k >0:
    nx, ny = x + direction[opers[i]-1][0], y + direction[opers[i]-1][1]

    if 0 <= nx < n and 0 <= ny < m:
        if opers[i] == 1:
            r = 1
            for _ in range(1):
                dollTemp1 = doll[1][2]
                dollTemp2 = doll[3][1]

                for j in range(2,0,-1):
                    doll[1][j] = doll[1][j-1]
                doll[1][0] = dollTemp2
                doll[3][1] = dollTemp1

                if not map_[nx][ny]:
                    map_[nx][ny] = doll[3][1]
                    x,y = nx,ny
                else:
                    doll[3][1] = map_[nx][ny]
                    map_[nx][ny] = 0
                    x,y = nx,ny
                print(doll[1][1])
        elif opers[i] == 2:
            r = 1
            for _ in range(1):
                dollTemp1 = doll[1][0]
                dollTemp2 = doll[3][1]

                for j in range(2):
                    doll[1][j] = doll[1][j+1]

                doll[1][2] = dollTemp2
                doll[3][1] = dollTemp1
                if not map_[nx][ny]:
                    map_[nx][ny] = doll[3][1]
                    x,y = nx,ny
                else:
                    doll[3][1] = map_[nx][ny]
                    map_[nx][ny] = 0
                    x,y = nx,ny
                print(doll[1][1])
        elif opers[i] == 3:
            c = 1
            for _ in range(1):
                dollTemp = doll[0][1]
                for j in range(3):
                    doll[j][1] = doll[j+1][1]
                doll[3][1] = dollTemp

                if not map_[nx][ny]:
                    map_[nx][ny] = doll[3][1]
                    x,y = nx,ny
                else:
                    doll[3][1] = map_[nx][ny]
                    map_[nx][ny] = 0
                    x,y = nx,ny
                print(doll[1][1])
        elif opers[i] == 4:
            c = 1
            for _ in range(1):
                dollTemp = doll[3][1]
                for j in range(3,0,-1):
                    doll[j][1] = doll[j-1][1]
                doll[0][1] = dollTemp

                if not map_[nx][ny]:
                    map_[nx][ny] = doll[3][1]
                    x,y = nx,ny
                else:
                    doll[3][1] = map_[nx][ny]
                    map_[nx][ny] = 0
                    x,y = nx,ny
                print(doll[1][1])
    i += 1
    k -= 1