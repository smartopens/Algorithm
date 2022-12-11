a, b, c = map(int, input().split())
tmp = 1
tmp_str = ""
nums = []
is_recur = False

for _ in range(b):
    tmp *= a
    if tmp%c in nums:
        break
    nums.append(tmp%c)

len_nums = len(nums)
print(nums)

print(nums[b % (len_nums) - 1])