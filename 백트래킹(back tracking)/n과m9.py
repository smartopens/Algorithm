from itertools import permutations

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
tempa = []
aDict = {}

for com in permutations(arr,m):
    tempa.append(list(com))

tempa.sort()

for t in tempa:
    t = ''.join(map(str, t))
    if t not in aDict:
        aDict[t] = 1

i = 0
maxI = len(aDict)

for k in aDict.keys():
    i += 1
    for ki in k:
        print(int(ki), end = ' ')
    if i == maxI:
        continue
    print()