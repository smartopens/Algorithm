import heapq

n,h,t = map(int, input().split())
giant_heights = [-int(input()) for _ in range(n)]
giant_heights.sort()
#heapq.heapify(giant_heights)
is_ok = False
cnt = 0

if -giant_heights[0] < h:
    is_ok = True

else:
    for idx in range(1, t+1):
        target = -heapq.heappop(giant_heights)
        if target == 1:
            heapq.heappush(giant_heights,-1)
            continue
        heapq.heappush(giant_heights,-int(target//2))

        if -giant_heights[0] < h:
            is_ok = True
            cnt = idx
            break

if is_ok:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-giant_heights[0])