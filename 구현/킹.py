place1, place2, n = map(str, input().split())
n = int(n)
chessMap = [[0]*8 for _ in range(8)]
colDict = {"A": 0, "B": 1, "C": 2, "D": 3,
           "E": 4, "F": 5, "G": 6, "H": 7}
rowDict = {"8": 0, "7": 1, "6": 2, "5": 3,
           "4": 4, "3": 5, "2": 6, "1": 7}
# nothing: 0, king : 1, dol: 2
y1,x1 = rowDict[place1[1]], colDict[place1[0]]
y2,x2 = rowDict[place2[1]], colDict[place2[0]]

# king : 1, dol : 2
chessMap[rowDict[place1[1]]][colDict[place1[0]]] = 1
chessMap[rowDict[place2[1]]][colDict[place2[0]]] = 2

for _ in range(n):
    command = input()

    if command == "R":
        nx, ny = x1 +1, y1
        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if nx == 7:
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny][nx+1] = 2
                x2, y2 = nx+1, ny
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny

    elif command == "L":
        nx, ny = x1 - 1, y1

        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if nx == 0:
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny][nx-1] = 2
                x2, y2 = nx-1, ny
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny
    elif command == "B":

        nx, ny = x1, y1+1

        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if ny == 7:
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny+1][nx] = 2
                x2, y2 = nx, ny+1
                x1, y1 = nx, ny
                continue

            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny
    elif command == "T":
        nx, ny = x1 , y1-1
        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if ny == 0:
                    continue
                chessMap[y1][x1] = 0
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny-1][nx] = 2
                x2, y2 = nx, ny-1
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny
    elif command == "RT":
        nx, ny = x1 + 1, y1-1
        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if nx == 7 or ny == 0:
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny-1][nx+1] = 2
                x2, y2 = nx+1, ny-1
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny
    elif command == "LT":
        nx, ny = x1 - 1, y1-1
        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if nx == 0 or ny == 0:
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny-1][nx-1] = 2
                x2, y2 = nx-1, ny-1
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny

    elif command == "RB":
        nx, ny = x1 + 1, y1+1
        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if nx == 7 or ny == 7 :
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny+1][nx+1] = 2
                x2, y2 = nx+1, ny+1
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny
    elif command == "LB":
        nx, ny = x1 - 1, y1+1
        if 0 <= nx < 8 and 0 <= ny < 8:
            if nx == x2 and ny == y2:
                if nx == 0 or ny == 7:
                    continue
                chessMap[y1][x1] = 0
                chessMap[ny][nx] = 1
                chessMap[ny+1][nx - 1] = 2
                x2, y2 = nx - 1, ny+1
                x1, y1 = nx, ny
                continue
            chessMap[y1][x1] = 0
            chessMap[ny][nx] = 1
            x1, y1 = nx, ny

for r in range(8):
    for c in range(8):
        if chessMap[r][c] == 1:
            x1,y1 = c,r
        elif chessMap[r][c] == 2:
            x2,y2 = c,r

for k, v in colDict.items():
    if v == x1:
        resultx1 = k
    if v == x2:
        resultx2 = k

for k, v in rowDict.items():
    if v == y1:
        resulty1 = k
    if v == y2:
        resulty2 = k

print(resultx1+ resulty1)
print(resultx2+ resulty2)
