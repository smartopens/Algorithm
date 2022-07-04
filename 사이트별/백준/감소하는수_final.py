from itertools import combinations

n = int(input())
dp_set = set()

for i in range(1,11):
    for coms in combinations(range(10),i):
        coms = list(coms)
        coms.sort(reverse=True)
        dp_set.add(int(''.join( (map(str, coms)))))
dp = list(dp_set)
dp.sort()

if len(dp) <= n:
    print(-1)
else:
    print(dp[n])