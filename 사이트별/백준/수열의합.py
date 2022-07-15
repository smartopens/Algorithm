partSum, Lens = map(int, input().split())
tmpLen = 0
isOk = True

def getStart(partSum, n):
    x = partSum - n*(n+1)//2
    return x // n

for i in range(Lens,101):
    n = getStart(partSum, i)
    tmp = n
    res = 0
    ans = []

    if n < -1:
        continue

    for _ in range(i):
        tmp2 = tmp + 1
        res += tmp2
        tmp += 1
        ans.append(tmp2)

    if res == partSum:
        for a in ans:
            print(a, end = ' ')
        isOk = False
        break

if isOk:
    print(-1)



