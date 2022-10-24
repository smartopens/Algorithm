import sys
from itertools import permutations

def solve(li):
    global  t_idx
    score = 0
    idx = 0
    for play in players:
        base1, base2, base3 = 0, 0, 0
        out = 0
        while out < 3:

            if li == [1, 6, 2, 0, 8, 5, 3, 4, 7]:
                print(base1,base2,base3,out,idx,play[li[idx]],score)

            if play[li[idx]] == 0:
                out += 1
            elif play[li[idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif play[li[idx]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif play[li[idx]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif play[li[idx]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0

            if li == [1, 6, 2, 0, 8, 5, 3, 4, 7]:
                print(base1,base2,base3,out,idx,play[li[idx]],score,"!!",t_idx)
            idx = (idx+1) % 9
            t_idx += 1

    return score

t_idx = 0
N = int(sys.stdin.readline())
players = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
for li in permutations(i for i in range(1, 9)):
    answer = max(answer, solve(list(li[:3]) + [0] + list(li[3:])))
print(answer)