from collections import deque

n, k = map(int, input().split())
convayer_w_layer = list(map(int, input().split()))
convayer_w = deque(convayer_w_layer[:n] + convayer_w_layer[n:])
robots = deque([0]*n)
zero_count = 0
ans = 1

while True:

    if zero_count >= k:
        break
    #로봇, convayer 회전
    convayer_w.rotate(1)
    robots.rotate(1)
    robots[-1] = 0

    # 로봇 이동
    for i in range(n-1,0,-1):
        if robots[i] == 0 and robots[i-1]> 0 and convayer_w[i]>0:
            robots[i] += 1
            robots[i - 1] -= 1
            convayer_w[i] -= 1

        robots[-1] = 0

    if robots[0] == 0 and convayer_w[0] > 0:
        robots[0] += 1
        convayer_w[0] -= 1

    zero_count = convayer_w.count(0)

    print(convayer_w)
    print(robots)
    print(zero_count)

    if zero_count >= k:
        break
    ans += 1

print(ans)

idx = 20




