def solution(stones, k):
    left = 1
    right = 200000000

    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for s in stones:
            if s <= mid:
                tmp += 1
            else:
                tmp = 0

            if tmp >= k:
                break

        if tmp < k:
            left = mid + 1
        else:
            right = mid - 1

    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))