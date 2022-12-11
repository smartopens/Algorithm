from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
loveList = [0] * (n ** 2 + 1)
order = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n ** 2):
    s, l1, l2, l3, l4 = map(int, input().split())
    loveList[s] = [l1, l2, l3, l4]
    order.append(s)


def getScore(r, c, s):
    num = 0
    scoreList = [0,1,10,100,1000]
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] in loveList[s]:
            num += 1

    return scoreList[num]

def countLove(r, c, s):
    num = 0
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] in loveList[s]:
            num += 1

    return num


def countEmpty(r, c):
    num = 0
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
            num += 1

    return num

def insertNum(s):
    possible = list()
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                possible.append((r,c,countLove(r,c,s),countEmpty(r,c)))
    possible.sort(key = lambda x : (x[2],x[3]), reverse = True)
    return (possible[0][0], possible[0][1])

ans = 0

for s in order:
    x,y = insertNum(s)
    board[x][y] = s

for r in range(n):
    for c in range(n):
        ans += getScore(r,c,board[r][c])

print(ans)
