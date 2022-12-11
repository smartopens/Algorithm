def solve(n,cnt,sqrN):
    global dp

    if n <= len(dp):
        return

    if cnt > n:
        return

    if n <= 1:
        return
    else:
        l = len(dp)
        index = l
        for i in range(l-1):
            dp[index] = dp[l-1] + dp[i]
            index += 1
            cnt += 1
        dp[index] = (3**sqrN)
        solve(n,cnt+1,sqrN+1)

dp = {0:1, 1:3}
n = int(input())

solve(n,0,2)
print(dp[n-1])