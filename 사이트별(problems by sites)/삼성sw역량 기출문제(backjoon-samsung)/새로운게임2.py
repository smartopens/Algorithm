import sys

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dolls = [[0]*n for _ in range(n)]
di = [(0,1),(0,-1),(-1,0),(1,0)]
ans = 0

for i in range(k):
    x,y,d = map(int, input().split())
    dolls[x-1][y-1] = [[i,d-1]]


while ans <= 1000:
    for i in range(k):
        cnt = 0
        for x in range(n):
            if cnt: break
            for y in range(n):
                if cnt: break
                if dolls[x][y]:
                    idx = 0
                    for doll in range(len(dolls[x][y])):

                        if dolls[x][y] and i == dolls[x][y][doll][0]:

                            d = dolls[x][y][doll][1]
                            nx,ny = x + di[d][0], y + di[d][1]
                            move = dolls[x][y][idx:]
                            cnt += 1
                            nx2 = -1
                            ny2 = -1
                            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] ==2:
                                if d == 0:
                                    d = 1
                                elif d == 1:
                                    d = 0
                                elif d == 2:
                                    d = 3
                                elif d == 3:
                                    d = 2

                                nx2, ny2 = x + di[d][0], y + di[d][1]

                                if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= n or board[nx2][ny2] ==2:
                                    dolls[x][y][doll][1] = d
                                    nx2, ny2 = -1, -1
                                    continue
                                else:
                                    dolls[x][y] = dolls[x][y][:idx]
                                    move[0][1] = d
                                    if board[nx2][ny2] == 0:
                                        if dolls[nx2][ny2]:
                                            dolls[nx2][ny2].extend(move)
                                        else:
                                            dolls[nx2][ny2] = move
                                    else:
                                        move.reverse()
                                        if dolls[nx2][ny2]:
                                            dolls[nx2][ny2].extend(move)
                                        else:
                                            dolls[nx2][ny2] = move

                            elif board[nx][ny] == 0:

                                dolls[x][y] = dolls[x][y][:idx]
                                if dolls[nx][ny]:
                                    dolls[nx][ny].extend(move)
                                else:
                                    dolls[nx][ny] = move



                            else:
                                dolls[x][y] = dolls[x][y][:idx]
                                move.reverse()
                                if dolls[nx][ny]:
                                    dolls[nx][ny].extend(move)
                                else:
                                    dolls[nx][ny] = move

                            if (0 <= nx2 <n and 0 <= ny2 <n and dolls[nx2][ny2] and len(dolls[nx2][ny2]) >= 4) or\
                                    (0 <= nx <n and 0 <= ny <n and dolls[nx][ny] and len(dolls[nx][ny]) >= 4):
                                print(ans+1)
                                sys.exit()


                            break



                        idx += 1

    ans += 1


if ans == 1001:
    ans = -1

print(ans)