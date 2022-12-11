def dfs(cnt, gameMap, redDol, blueDol):
    global answer
    tempMap = gameMap
    isRed = False
    isBlue = False

    redX,redY = redDol
    blueX, blueY = blueDol



    if cnt > 10:
        answer = 11
        return

    redoriX, redoriY = redX, redY
    blueoriX, blueoriY = blueX, blueY
    # 상
    while gameMap[redX][redY] != "#":

        isOut = False
        if 0<= redY -1 < n:
            redY -= 1
            if gameMap[redX][redY] == "O":
                isOut = True
                isRed = True
            elif gameMap[redX][redY] == "#" or "B":
                isOut = True
                redY += 1
        else:
            break

        if isOut:
            break
    while gameMap[blueX][blueY] != "#":
        isOut = False
        if 0<= blueY -1 < n:
            blueY -= 1
            if gameMap[blueX][blueY] == "O":
                isOut = True
                isblue = True
            elif gameMap[blueX][blueY] == "#" or "R":
                blueY += 1
                isOut = True
        else:
            break

        if isOut:
            break
    if isRed == True and isBlue == False:
        answer = min(answer, cnt + 1)
        return
    elif isRed == True and isBlue == True:
        return
    elif isRed == False and isBlue == True:
        return
    else:
        gameMap[redoriX][redoriY] = "."
        gameMap[blueoriX][blueoriY] = "."
        gameMap[redX][redY] = "R"
        gameMap[blueX][blueY] = "B"

        (cnt+1, gameMap, (redX,redY), (blueX,blueY))

        gameMap[redoriX][redoriY] = "R"
        gameMap[blueoriX][blueoriY] = "B"
        gameMap[redX][redY] = "."
        gameMap[blueX][blueY] = "."

    redX,redY = redoriX, redoriY
    blueX,blueY = blueoriX, blueoriY
    isRed = False
    isBlue = False

    # 하
    while gameMap[redX][redY] != "#":
        isOut = False
        if 0 <= redY + 1 < n:
            redY += 1
            if gameMap[redX][redY] == "O":
                isOut = True
                isRed = True
            elif gameMap[redX][redY] == "#" or "B":
                isOut = True
                redY -= 1
        else:
            break

        if isOut:
            break
    while gameMap[blueX][blueY] != "#":
        isOut = False
        if 0 <= blueY + 1 < n:
            blueY += 1
            if gameMap[blueX][blueY] == "O":
                isOut = True
                isblue = True
            elif gameMap[blueX][blueY] == "#" or "R":
                blueY -= 1
                isOut = True
        else:
            break

        if isOut:
            break
    if isRed == True and isBlue == False:
        answer = min(answer, cnt + 1)
        return
    elif isRed == True and isBlue == True:
        return
    elif isRed == False and isBlue == True:
        return
    else:
        gameMap[redoriX][redoriY] = "."
        gameMap[blueoriX][blueoriY] = "."
        gameMap[redX][redY] = "R"
        gameMap[blueX][blueY] = "B"

        (cnt + 1, gameMap, (redX, redY), (blueX, blueY))

        gameMap[redoriX][redoriY] = "R"
        gameMap[blueoriX][blueoriY] = "B"
        gameMap[redX][redY] = "."
        gameMap[blueX][blueY] = "."

    redX,redY = redoriX, redoriY
    blueX,blueY = blueoriX, blueoriY
    isRed = False
    isBlue = False
    # 좌
    while gameMap[redX][redY] != "#":

        isOut = False
        if 0 <= redX - 1 < m:
            redX -= 1
            if gameMap[redX][redY] == "O":
                isOut = True
                isRed = True
            elif gameMap[redX][redY] == "#" or "B":
                isOut = True
                redX += 1
        else:
            break

        if isOut:
            break
    while gameMap[blueX][blueY] != "#":
        isOut = False
        if 0 <= blueX - 1 < m:
            blueX -= 1
            if gameMap[blueX][blueY] == "O":
                isOut = True
                isblue = True
            elif gameMap[blueX][blueY] == "#" or "R":
                blueX += 1
                isOut = True
        else:
            break

        if isOut:
            break
    if isRed == True and isBlue == False:
        answer = min(answer, cnt + 1)
        return
    elif isRed == True and isBlue == True:
        return
    elif isRed == False and isBlue == True:
        return
    else:
        gameMap[redoriX][redoriY] = "."
        gameMap[blueoriX][blueoriY] = "."
        gameMap[redX][redY] = "R"
        gameMap[blueX][blueY] = "B"

        (cnt + 1, gameMap, (redX, redY), (blueX, blueY))

        gameMap[redoriX][redoriY] = "R"
        gameMap[blueoriX][blueoriY] = "B"
        gameMap[redX][redY] = "."
        gameMap[blueX][blueY] = "."
    # 우
    redX,redY = redoriX, redoriY
    blueX,blueY = blueoriX, blueoriY
    isRed = False
    isBlue = False
    while gameMap[redX][redY] != "#":

        isOut = False
        if 0 <= redX + 1 < m:
            redX += 1
            if gameMap[redX][redY] == "O":
                isOut = True
                isRed = True
            elif gameMap[redX][redY] == "#" or "B":
                isOut = True
                redX -= 1
        else:
            break

        if isOut:
            break
    while gameMap[blueX][blueY] != "#":
        isOut = False
        if 0 <= blueX + 1 < m:
            blueX += 1
            if gameMap[blueX][blueY] == "O":
                isOut = True
                isblue = True
            elif gameMap[blueX][blueY] == "#" or "R":
                blueX -= 1
                isOut = True
        else:
            break

        if isOut:
            break
    if isRed == True and isBlue == False:
        answer = min(answer, cnt + 1)
        return
    elif isRed == True and isBlue == True:
        return
    elif isRed == False and isBlue == True:
        return
    else:
        gameMap[redoriX][redoriY] = "."
        gameMap[blueoriX][blueoriY] = "."
        gameMap[redX][redY] = "R"
        gameMap[blueX][blueY] = "B"

        (cnt + 1, gameMap, (redX, redY), (blueX, blueY))

        gameMap[redoriX][redoriY] = "R"
        gameMap[blueoriX][blueoriY] = "B"
        gameMap[redX][redY] = "."
        gameMap[blueX][blueY] = "."


    return

n, m = map(int, input().split())
gameMap = []

for _ in range(n):
    gameMap.append(list(input()))

for r in range(n):
    for c in range(m):
        if gameMap[r][c] == "R":
            redDol = (r,c)
        elif gameMap[r][c] == "B":
            blueDol = (r,c)
answer = 100

dfs(1,gameMap,redDol,blueDol)

print(answer)
if answer >10:
    print(-1)
else:
    print(answer)


