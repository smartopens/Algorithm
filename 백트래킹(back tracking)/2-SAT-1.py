# a1, a2, a3, a4, ..., a20 --> m(max:100)개의 식까지
# 하나의 절: a1 + a2 로 생각, not은 말그대로 반대 1이냐 -1이냐 --> 를 1이냐 0이냐 -->
# not:(ori:1 -> 0, ori:0 -> 1) : 1 - an 으로 표현
# 1~20이 0에서 1중 어떤것으로 배정되느냐 --> 이 중 true 판단
# 모든 m개의 경우가 1로 판단될 수 있는지를 봐야함

from itertools import permutations
from itertools import combinations

n, m = map(int, input().split())
is_ok = True
problems = []

for _ in range(m):
    x, next_x = map(int, input().split())
    problems.append((x, next_x))

# i 는 1

case = [0] * n
true_case = []
total = range(n)

for i in range(1,n+1):
    is_ok = True
    for com in combinations(total, i):
        is_ok = True
        case = [0] * n
        sat_check = [0]*m
        tmp_ok = True
        for j in com:
            case[j] = 1
        for x, next_x in problems:
            a,b = 0,0

            if x < 0:
                if case[abs(x)-1]:
                    a = 0
                else:
                    a = 1
            else:
                a = case[x-1]

            if next_x < 0:
                if case[abs(next_x)-1]:
                    b = 0
                else:
                    b = 1
            else:
                b = case[next_x-1]

            if a + b < 1:
                tmp_ok = False
                break

        if not tmp_ok:
            is_ok = False

        if tmp_ok:
            break

    if is_ok:
        break

if is_ok:
    print(1)
else:
    print(0)


# -x1 + x2, -x2+x3, x1+x3, x3+x2