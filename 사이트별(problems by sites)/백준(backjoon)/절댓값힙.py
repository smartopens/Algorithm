import sys
import heapq

n = int(input())
p_q = []
m_q = []

for _ in range(n):
    num = int(int(sys.stdin.readline().rstrip()))

    if num == 0:
        if not p_q and not m_q:
            print(0)
            continue
        plus, minus = 0,0

        if not m_q and p_q:
            plus = heapq.heappop(p_q)
            print(plus)
            continue

        if not p_q and m_q:
            minus = heapq.heappop(m_q)
            print(-minus)
            continue

        if p_q and m_q:
            plus = heapq.heappop(p_q)
            minus = heapq.heappop(m_q)

        ans = 0

        if abs(plus) < abs(minus):
            ans = plus
            heapq.heappush(m_q, minus)
        else:
            ans = -minus
            heapq.heappush(p_q, plus)
        print(ans)
    else:
        if num > 0:
            heapq.heappush(p_q, num)
        else:
            heapq.heappush(m_q, -num)