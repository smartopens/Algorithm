from itertools import combinations

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    for nums in combinations(n_list, i):

        if sum(nums) == s:
            cnt += 1
print(cnt)