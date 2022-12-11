n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for idx in range(n):
    lectures[idx].append(idx)

lectures_sorted = sorted(lectures, key = lambda x : (x[1],x[0]))
vi = set()

while len(vi) < n:
    end_time_Flag, end_time = False, 0

    for i in range(n):
        if not end_time_Flag and lectures_sorted[i][2] not in vi:
            end_time = lectures_sorted[i][1]
            end_time_Flag = True
            vi.add(lectures_sorted[i][2])

        if end_time <= lectures_sorted[i][0] and lectures_sorted[i][2] not in vi:
            end_time = lectures_sorted[i][1]
            vi.add(lectures_sorted[i][2])

    ans += 1

print(ans)