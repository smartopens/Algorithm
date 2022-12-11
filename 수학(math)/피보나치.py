import sys
sys.setrecursionlimit(10**5)
from collections import deque

t = int(input())

nums = [1]
a, b = 1, 1

while True:

    a, b = b, a + b
    if b > 10**9:
        break
    nums.append(b)

def dfs(path,num_sum,idx):
    global paths, path_len

    if num_sum > num or idx < 0:
        return

    if num_sum == num:
        if len(path) < path_len:
            path_len = len(path)
            paths = path[:]
        return

    dfs(path, num_sum, idx - 1)
    path.append(nums[idx])
    dfs(path, num_sum+nums[idx], idx - 1)
    path.pop()

for _ in range(t):
    num = int(input())
    nums_len = len(nums)
    path = []

    for i in range(nums_len-1,-1,-1):
        if nums[i] <= num:
            path.append(nums[i])
            num -= nums[i]

            if num <= 0:
                break
    path.sort()
    for i in path:
        print(i, end = ' ')
    print()