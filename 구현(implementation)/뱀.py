n = int(input())
dummyMap = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    r, c = map(int, input().split(' '))
    dummyMap[r - 1][c - 1] = 1

l = int(input())
timeList = []
cmdList = []

for _ in range(l):
    t, command = map(str, input().split(' '))
    t = int(t)
    timeList.append(t)
    cmdList.append(command)

nowTime = timeList.pop(0)
com = cmdList.pop(0)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i = 0
headX = 0
headY = 0
tailX = 0
tailY = 0
time = 0
snake = [(0, 0)]

while True:
    dx, dy = headX + directions[i][0], headY + directions[i][1]
    if (dx, dy) in snake or dx < 0 or dx >= n or dy < 0 or dy >= n:
        time += 1
        break

    if dummyMap[dx][dy] == 1:
        snake.append((dx, dy))
        headX, headY = dx, dy
        dummyMap[dx][dy] = 0
    else:
        snake.append((dx, dy))
        tailX, tailY = snake.pop(0)
        headX, headY = dx, dy

    time += 1
    if time == nowTime:
        if com == "L":
            i -= 1
            if i < 0:
                i = 3
            if timeList and cmdList:
                nowTime = timeList.pop(0)
                com = cmdList.pop(0)
        elif com == "D":
            i += 1
            if i > 3:
                i = 0
            if timeList and cmdList:
                nowTime = timeList.pop(0)
                com = cmdList.pop(0)

print(time)
