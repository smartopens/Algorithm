def bfs(x,y,fishMap):
    global time, size

    maxNum = 0
    for i in range(len(fishMap)):
        maxNum = max(maxNum, max(fishMap[i]))

    if
    return

n = int(input())
fishMap = []

for _ in range():
    fishMap.append(list(map(int, input().split(' '))))

x,y = 0,0
for r in range(n):
    for c in range(n):
        if fishMap[r][c] == 9:
            x = r
            y = c
time = 0
size = 2
bfs(x,y,fishMap)
