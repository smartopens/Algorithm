import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
score_inings = [list(map(int, input().split())) for _ in range(n)]
play_order = list(range(1,9))
answer = 0


for per in permutations(play_order,8):
    order = list(per)
    order.insert(3,0)
    score = 0
    play_idx = 0
    base1, base2, base3 = 0,0,0

    for i in range(n):
        score_ining = score_inings[i]
        out = 0
        base1, base2, base3 = 0,0,0

        while out < 3:
            player = order[play_idx]

            if score_ining[player] == 0:
                out += 1
            elif score_ining[player] == 1:
                score += base3
                base1,base2,base3 = 1,base1,base2
            elif score_ining[player] == 2:
                score += (base2+base3)
                base1,base2,base3 = 0,1,base1
            elif score_ining[player] == 3:
                score += (base1+base2+base3)
                base1,base2,base3 = 0,0,1
            elif score_ining[player] == 4:
                score += (base1+base2+base3+1)
                base1, base2, base3 = 0,0,0

            play_idx = (play_idx + 1)%9

    answer = max(answer,score)

print(answer)