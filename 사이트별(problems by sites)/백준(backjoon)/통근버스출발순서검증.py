from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
ans = 0
nums_len = len(nums)

for i in range(0,nums_len-2,1):
    f_num = nums[i]
    num_dict = dict()

    for j in range(i+1,nums_len):
        if f_num < nums[j]:
            if j not in num_dict:
                num_dict[j] = 0
        elif f_num > nums[j]:
            for k,v in num_dict.items():
                num_dict[k] += 1

    for k,v in num_dict.items():
        ans += v

print(ans)




