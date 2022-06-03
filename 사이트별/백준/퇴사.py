dayDict = dict()
n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]
ans = 0

def dfs(d,w):
    global ans

    if d > n:
        ans = max(ans,w)
        return

    if d + dayDict[d][0] <= n+1:
        dfs(d + dayDict[d][0], w + dayDict[d][1])

    dfs(d+1, w)
    return

for i in range(n):
    dayDict[i+1] = list(map(int, input().split(' ')))

dfs(1,0)
print(ans)
