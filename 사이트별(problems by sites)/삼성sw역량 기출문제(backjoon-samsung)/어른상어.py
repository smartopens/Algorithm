from copy import deepcopy

n, m, k = map(int, input().split())
directTmp = [0]*m
board = [[0]*n for _ in range(n)]
smell = [[0]*n for _ in range(n)]
sharkP = [0]*m
direct = [0,(-1,0),(1,0),(0,-1),(0,1)]
maxM = m

for j in range(n):
    inputTmp = list(map(int, input().split()))
    for i in range(n):
        if inputTmp[i] != 0:
            board[j][i] = [int(inputTmp[i])-1, k, 0]
            smell[j][i] = [int(inputTmp[i])-1,k]
            directTmp[int(inputTmp[i])-1] = (j,i)

firstDirect = list(map(int, input().split()))
for i in range(m):
    x,y = directTmp[i]
    board[x][y][2] = (firstDirect[i] - 1)

for i in range(m):
    for j in range(4):
        if sharkP[i] == 0:
            sharkP[i] = [list(map(int, input().split(' ')))]
        else:
            sharkP[i].append(list(map(int, input().split(' '))))

t = 0
while True:
    if t > 1000:
        t = -1
        break

    if maxM == 1:
        break

    check = [[0]*n for _ in range(n)]

    for i in range(m):
        sharkD = sharkP[i]
        isDone = False
        for r in range(n):
            if isDone: break
            for c in range(n):
                if board[r][c] and board[r][c][0] == i:
                    nowDi = board[r][c][2]

                    d = 0

                    for di in sharkD[nowDi]:
                        nr, nc = r + direct[di][0], c + direct[di][1]
                        d += 1

                        if 0 <= nr < n and 0 <= nc < n and (smell[nr][nc] == 0 or check[nr][nc] == 1):
                            if board[nr][nc]:
                                if board[nr][nc][0] > i:
                                    board[r][c] = 0
                                    board[nr][nc] = [i,k,di-1]
                                    smell[nr][nc] = [i,k]
                                else:
                                    board[r][c] = 0
                                maxM -= 1
                            else:
                                board[r][c] = 0
                                board[nr][nc] = [i, k, di - 1]
                                smell[nr][nc] = [i, k]
                            check[nr][nc] = 1
                            isDone = True
                            break
                    if isDone:
                        break
                    isDone = True
                    for di in sharkD[nowDi]:
                        nr, nc = r + direct[di][0], c + direct[di][1]
                        d += 1

                        if 0 <= nr < n and 0 <= nc < n and smell[nr][nc] and smell[nr][nc][0] == i:
                            if board[nr][nc]:
                                if board[nr][nc][0] > i:
                                    board[r][c] = 0
                                    board[nr][nc] = [i,k,di-1]
                                    smell[nr][nc] = [i,k]
                                else:
                                    board[r][c] = 0
                                maxM -= 1
                            else:
                                board[r][c] = 0
                                board[nr][nc] = [i, k, di - 1]
                                smell[nr][nc] = [i, k]

                            check[nr][nc] = 1

                            break

                    if isDone:
                        break

    for r in range(n):
        for c in range(n):
            if smell[r][c] and not board[r][c]:
                smell[r][c][1] -= 1

                if smell[r][c][1] <= 0:
                    smell[r][c] = 0

    t += 1

print(t)