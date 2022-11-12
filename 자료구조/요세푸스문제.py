n, k = map(int, input().split(' '))
personDict = dict()
res = []

for i in range(n):
    personDict[i] = 1
idx = -1

t = n
while t > 0:
    tk = k
    while tk > 0:
        idx += 1
        if idx > n-1:
            idx = 0
        if personDict[idx] != 1:
            continue
        tk -= 1

    res.append(idx+1)
    personDict[idx] = 0
    t -= 1


print("<", end ="")
for r in range(len(res)):
    if r == len(res) - 1:
        print(str(res[r])+">")
        continue
    print(str(res[r]), end=", ")