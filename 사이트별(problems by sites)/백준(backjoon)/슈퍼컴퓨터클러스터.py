import heapq

n, b = map(int, input().split())
coms = list(map(int, input().split()))
coms.sort()
min_t = coms[0]
is_ok = True
answer = -1

while True:
    ori_b = b

    for i in coms:
        if i < min_t:
            ori_b -= (min_t-i)**2

    if ori_b < 0:
        is_ok = False
        break
    else:
        answer = min_t
        min_t += 1

print(answer)