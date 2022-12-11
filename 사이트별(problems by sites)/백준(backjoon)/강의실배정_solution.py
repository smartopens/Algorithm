import heapq

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
ans = 0

lectures_sorted = sorted(lectures, key = lambda x : (x[0]))
lectures_squzzed = []
heapq.heappush(lectures_squzzed, lectures_sorted[0][1])

for i in range(1,n):
    if lectures_squzzed[0] > lectures_sorted[i][0]:
        heapq.heappush(lectures_squzzed, lectures_sorted[i][1])
    else:
        heapq.heappop(lectures_squzzed)
        heapq.heappush(lectures_squzzed, lectures_sorted[i][1])

print(len(lectures_squzzed))