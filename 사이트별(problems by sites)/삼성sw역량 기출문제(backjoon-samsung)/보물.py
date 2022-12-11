n = int(input())
a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))
a_nums.sort()
b_nums_sorted = sorted(b_nums, reverse= True)
b_nums_idx = []
answer = 0

for i in range(n):
    b_nums_idx.append((b_nums_sorted[i],i))

for i in range(n):
    answer += a_nums[b_nums_idx[i][1]]*b_nums_sorted[i]

print(answer)