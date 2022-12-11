t = int(input())

for _ in range(t):
    n = int(input())

    dp0 = [1,0] + [0]*39
    dp1 = [0,1] + [0]*39

    if n >= 2:
        for i in range(2,n+1):
            dp0[i] = dp0[i - 1] + dp0[i - 2]

        for i in range(2,n+1):
            dp1[i] = dp1[i - 1] + dp1[i - 2]

    print(dp0[n],dp1[n])

