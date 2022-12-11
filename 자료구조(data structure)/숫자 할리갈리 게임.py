from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
do_q = deque([])
su_q = deque([])
do_ground = deque([])
su_ground = deque([])
do_win,su_win = False, False

for _ in range(n):
    a,b =  map(int, input().split())
    do_q.append(a)
    su_q.append(b)

while m > 0:

    do_ground.append(do_q.pop())

    if not do_q:
        su_win = True
        break

    if do_ground[-1] == 5:
        while su_ground:
            do_q.appendleft(su_ground.popleft())
        while do_ground:
            do_q.appendleft(do_ground.popleft())


    if do_ground and su_ground and do_ground[-1] + su_ground[-1] == 5:
        while do_ground:
            su_q.appendleft(do_ground.popleft())
        while su_ground:
            su_q.appendleft(su_ground.popleft())
    m -= 1

    if m == 0:
        break
    su_ground.append(su_q.pop())

    if not su_q:
        do_win = True
        break


    if su_ground[-1] == 5:
        while su_ground:
            do_q.appendleft(su_ground.popleft())
        while do_ground:
            do_q.appendleft(do_ground.popleft())

    if do_ground and su_ground and do_ground[-1] + su_ground[-1] == 5:
        while do_ground:
            su_q.appendleft(do_ground.popleft())
        while su_ground:
            su_q.appendleft(su_ground.popleft())
    m -= 1


if do_win:
    print("do")
elif su_win:
    print("su")
else:
    if len(do_q) == len(su_q):
        print("dosu")
    elif len(do_q) > len(su_q):
        print("do")
    else:
        print("su")