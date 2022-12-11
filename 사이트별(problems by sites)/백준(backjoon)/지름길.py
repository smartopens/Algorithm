n, dist = map(int, input().split())
fast_start = []
fast_dict = dict()

for _ in range(n):
    fast =  list(map(int, input().split()))
    if fast[1] > dist:
        continue
    fast_start.append(fast[0])

    if fast[0] not in fast_dict:
        fast_dict[fast[0]] = [fast]
    else:
        fast_dict[fast[0]].append(fast)

dp = [i for i in range(dist+1)]

for i in range(len(dp)):

    dp[i] = min(dp[i],dp[i-1]+1)
    if i in fast_start:
        for f_list in fast_dict[i]:
            dp[f_list[1]] = min(dp[f_list[1]],
                                      dp[i] + f_list[2])

print(dp[dist])