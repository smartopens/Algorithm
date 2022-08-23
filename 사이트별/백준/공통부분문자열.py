first = input()
second = input()
first_len = len(first)
second_len = len(second)
dp = [[0]*(second_len+1) for _ in range((first_len+1))]

for i in range(first_len):
    for j in range(second_len):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0

ans_num = 0
for i in dp:
    max_tmp = max(i)
    if max_tmp > ans_num:
        ans_num = max_tmp

print(ans_num)
