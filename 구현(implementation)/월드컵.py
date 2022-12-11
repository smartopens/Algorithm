
from collections import deque
from itertools import combinations

possibleList = [[0, 0, 0] for _ in range(6)]

def isPossible(num, testNum, testCase):
    global res
    if num == 15:
        sum_ = 0
        for case in testCase:
            sum_ += case.count(0)

        if sum_ == 18:
            res = 1
        return

    t1, t2 = cases[num]

    # t1승 t2패
    if testCase[t1][0] > 0 and testCase[t2][2] > 0:
        testCase[t1][0] -= 1
        testCase[t2][2] -= 1
        isPossible(num + 1, testNum, testCase)
        testCase[t1][0] += 1
        testCase[t2][2] += 1

    # t1, t2 무
    if testCase[t1][1] > 0 and testCase[t2][1] > 0:
        testCase[t1][1] -= 1
        testCase[t2][1] -= 1
        isPossible(num + 1, testNum, testCase)
        testCase[t1][1] += 1
        testCase[t2][1] += 1


    # t1패, t2승
    if testCase[t1][2] > 0 and testCase[t2][0] > 0:
        testCase[t1][2] -= 1
        testCase[t2][0] -= 1
        isPossible(num + 1, testNum, testCase)
        testCase[t1][2] += 1
        testCase[t2][0] += 1

testList = list()
result = []

for _ in range(4):
    oneTempList = list(map(int, input().split(' ')))
    oneList = list()
    oneQ = deque(oneTempList)

    while oneQ:
        tempList = list()
        for _ in range(3):
            tempList.append(oneQ.popleft())

        oneList.append(tempList)

    testList.append(oneList)

cases = list(combinations(range(6), 2))
# isPossible(0,0)

for i in range(4):
    # possibleList = [[0, 0, 0] for _ in range(6)]
    res = 0
    isPossible(0,0,testList[i])
    result.append(res)


for i in result:
    print(i, end=' ')