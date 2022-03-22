from collections import deque

def change(arr):
    n = len(arr)
    m = len(arr[0])
    newTetro = [["X"] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            newTetro[r][m-1-c] = arr[r][c]

    return newTetro

def rotation(arr):
    n = len(arr)
    m = len(arr[0])
    newTetro = [["X"]*m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            newTetro[c][n-1-r] = arr[r][c]

    return newTetro

possibleCase = []

tetromino1 = [["O"]*4, ["X"]*4,["X"]*4,["X"]*4]
tetromino2 = [["O","O","X","X"],["O","O","X","X"],["X"]*4,["X"]*4]
tetromino3 = [["O","X","X","X"],["O","X","X","X"],["O","O","X","X"],["X"]*4]
tetromino4 = [["O","X","X","X"],["O","O","X","X"],["X","O","X","X"],["X"]*4]
tetromino5 = [["O","O","O","X"],["X","O","X","X"],["X"]*4,["X"]*4]



# 회전
temp = tetromino1
possibleCase.append(tetromino1)
for _ in range(1):
    temp = rotation(temp)
    possibleCase.append(temp)

possibleCase.append(tetromino2)

temp = tetromino3
possibleCase.append(temp)
for _ in range(3):
    temp = rotation(temp)
    possibleCase.append(temp)

temp = change(tetromino3)
possibleCase.append(temp)
for _ in range(3):
    temp = rotation(temp)
    possibleCase.append(temp)

temp = tetromino4
possibleCase.append(temp)
for _ in range(1):
    temp = rotation(temp)
    possibleCase.append(temp)

temp = change(tetromino4)
possibleCase.append(temp)
for _ in range(1):
    temp = rotation(temp)
    possibleCase.append(temp)

temp = tetromino5
possibleCase.append(temp)
for _ in range(3):
    temp = rotation(temp)
    possibleCase.append(temp)

n, m = map(int, input().split())
scoreMap = []
for _ in range(n):
    scoreMap.append(list(map(int, input().split())))

len_ = len(possibleCase)
print(len_)
answer = 0
for i in range(len_):
    tetro = possibleCase[i]
    q = deque([])

    height = 0
    width = 0

    for h in range(4):
        for w in range(4):
            if tetro[h][w] == "O":
                height = max(height,h)
                width = max(width,w)
                q.append((h,w))

    print(tetro)
    # print(width)
    # print(height)
    # rint(q)
    newN = n - height - 1
    newM = m - width - 1

    for k in range(newN):
        for l in range(newM):
            # totalMap = [["X"]*m for _ in range(n)]
            tempAns = 0

            #for r in range(height):
            #   for c in range(width):
            #       totalMap[r+k][c+l] = tetro[r][c]

            #            for totalR in range(n):
            #   for totalC in range(m):
            #       if totalMap[totalR][totalC] == "O":
            #           tempAns += scoreMap[totalR][totalC]

            for qList in q:
                dx,dy = qList
                tempAns += scoreMap[k+dx][l+dy]


            answer = max(answer, tempAns)

print(answer)

