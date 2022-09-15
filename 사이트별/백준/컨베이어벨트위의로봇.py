from collections import deque

n, k = map(int, input().split())
convayer_w_layer = list(map(int, input().split()))
convayer_w = [convayer_w_layer[:n], convayer_w_layer[n:]]
robots = [[0]*n for _ in range(2)]

convayer_w = deque(convayer_w_layer[:n] + convayer_w_layer[n:])
robots = deque([0]*n)

zero_count = 0
ans = 1

while True:

    if zero_count >= k:
        break
    #로봇, convayer 회전
    robots[0][-1] = 0

    first_layer_robots = robots[0]
    second_layer_robots = robots[1]
    down_robot = first_layer_robots.pop()
    up_robot = second_layer_robots.pop(0)

    first_layer_robots = [up_robot] + first_layer_robots
    second_layer_robots = second_layer_robots + [down_robot]

    robots = [first_layer_robots, second_layer_robots]

    first_layer_w= convayer_w[0]
    second_layer_w = convayer_w[1]
    down_w = first_layer_w.pop()
    up_w = second_layer_w.pop(0)

    first_layer_w = [up_w] + first_layer_w
    second_layer_w = second_layer_w + [down_w]

    convayer_w = [first_layer_w, second_layer_w]
    robots[0][-1] = 0

    # 로봇 이동
    for i in range(n-1,0,-1):
        if robots[0][i] == 0 and robots[0][i-1]> 0 and convayer_w[0][i]>0:
            robots[0][i] += 1
            robots[0][i - 1] -= 1
            convayer_w[0][i] -= 1

        robots[0][-1] = 0

    if robots[0][0] == 0 and convayer_w[0][0] > 0:
        robots[0][0] += 1
        convayer_w[0][0] -= 1

    zero_count = 0
    for i in range(2):
        zero_count += convayer_w[i].count(0)
    print(convayer_w)
    print(robots)
    print(zero_count)

    if zero_count >= k:
        break
    ans += 1

print(ans)

