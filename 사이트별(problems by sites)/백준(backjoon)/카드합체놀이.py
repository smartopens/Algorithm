import heapq

n, m = map(int, input().split())
nums = list(map(int, input().split()))
heapq.heapify(nums)


for _ in range(m):
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    new_num = first + second

    heapq.heappush(nums, new_num)
    heapq.heappush(nums, new_num)

print(sum(nums))