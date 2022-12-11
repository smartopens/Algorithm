testCase = int(input())
result = []

for _ in range(testCase):

    commands = list(input())
    maxPlusX = 0
    maxMinusX = 0
    maxPlusY = 0
    maxMinusY = 0
    place = [0, 0]
    # 북, 동, 남, 서
    directions = [True, False, False, False]
    idx = 0

    while commands:
        command = commands.pop(0)

        if command == "F":
            if directions[0] == True:
                place[1] += 1
            elif directions[1] == True:
                place[0] += 1
            elif directions[2] == True:
                place[1] -= 1
            elif directions[3] == True:
                place[0] -= 1

            if place[0] >= 0:
                maxPlusX = max(maxPlusX, place[0])
            else:
                maxMinusX = min(maxMinusX, place[0])

            if place[1] >= 0:
                maxPlusY = max(maxPlusY, place[1])
            else:
                maxMinusY = min(maxMinusY, place[1])

        elif command == "B":
            if directions[0] == True:
                place[1] -= 1
            elif directions[1] == True:
                place[0] -= 1
            elif directions[2] == True:
                place[1] += 1
            elif directions[3] == True:
                place[0] += 1

            if place[0] >= 0:
                maxPlusX = max(maxPlusX, place[0])
            else:
                maxMinusX = min(maxMinusX, place[0])

            if place[1] >= 0:
                maxPlusY = max(maxPlusY, place[1])
            else:
                maxMinusY = min(maxMinusY, place[1])

        elif command == "L":
            directions[idx] = False
            idx -= 1
            if idx <0:
                idx = 3
            directions[idx] = True
        elif command == "R":
            directions[idx] = False
            idx += 1
            if idx > 3:
                idx = 0
            directions[idx] = True


    result.append((maxPlusX - maxMinusX)*(maxPlusY - maxMinusY))

for i in result:
    print(i)