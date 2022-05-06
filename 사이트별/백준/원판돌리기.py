from collections import deque
from copy import deepcopy
n, m, t = map(int, input().split())
disks = [list(map(int, input().split())) for _ in range(n)]
disks2 = []
opers = [list(map(int, input().split())) for _ in range(t)]
#
# for idx, di in enumerate(disk1):
#     disks.append([idx] + di)

def update():
    global disks, m, n

    isPlus = False
    score = 0

    tmpDisk = deepcopy(disks)
    for i in range(n):
        for j in range(m):
            if j == m-1:
                if disks[i][j] and disks[i][j] == disks[i][0]:
                    tmpDisk[i][j] = 0
                    tmpDisk[i][0] = 0
                    isPlus = True
                continue

            if disks[i][j] and disks[i][j] == disks[i][j+1]:

                tmpDisk[i][j] = 0
                tmpDisk[i][j+1] = 0
                isPlus = True


    for i in range(n-1):
        for j in range(m):
            if disks[i][j] and disks[i][j] == disks[i+1][j]:
                tmpDisk[i][j] = 0
                tmpDisk[i+1][j] = 0
                isPlus = True

    disks = deepcopy(tmpDisk)
    if not isPlus:
        tmp = 0
        for i in range(n):
            for j in range(m):
                if disks[i][j]:
                    score += disks[i][j]
                    tmp += 1

        if tmp != 0:
            num = score / tmp
            for i in range(n):
                for j in range(m):
                    if disks[i][j]:
                        if disks[i][j] > num:
                            disks[i][j] -= 1
                        elif disks[i][j] < num:
                            disks[i][j] += 1

    return

def rotate(d,cnt,k):
    global disks, m
    num = 0
    if d == 0:
        num = cnt % m
    else:
        num = ((m-1)*cnt)%m

    tmp = disks[k]
    for _ in range(num):
        tmp.insert(0,tmp.pop())

    disks[k] = tmp

    return


for oper in opers:
    x, d, cnt = oper

    for i in range(n):
        if (i+1)%x == 0:
            rotate(d,cnt,i)

    update()

total = 0

for i in disks:
    total += sum(i)

print(total)
