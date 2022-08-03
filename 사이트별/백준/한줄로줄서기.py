from itertools import permutations
from collections import deque

n = int(input())
q = deque([0]*n)
case = list(map(int, input().split()))
nums = list(range(1,n+1))

def isOk(pers):

    if pers[case[0]] != 1:
        return False

    for i in range(n):
        k = case[i]
        tmp = 0

        for j in range(n):
            if pers[j] == i+1:
                break

            if pers[j] > i+1:
                tmp += 1

        if tmp != k:
            return False

    return  True

for pers in permutations(nums,n):
    if isOk(pers):
        for i in pers:
            print(i, end = ' ')
        break

# for i in range(n):
#     if i == 0:
#         q[case[i]] = 1
#         continue
#
#     tmp = case[i]
#     idx = 0
#
#     for j in range(n):
#         if q[j] > i+1:
#             tmp -= 1

