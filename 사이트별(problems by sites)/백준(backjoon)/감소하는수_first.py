from itertools import combinations

idx = 10
num = 10
n = int(input())
dp = list(range(10))
cannot_solve = False

print(dp)

if n >= 10:
    while idx <= n:
        if num > 987654321:
            cannot_solve = True
            break
        string = str(num)
        string_len = len(string)
        isOk = True

        for i in range(string_len-1):
            if string[i] <= string[i+1]:
                isOk = False
                break

        if isOk:
            dp.append(num)
            idx += 1
        num += 1

if cannot_solve:
    print(-1)
else:
    print(dp[n])