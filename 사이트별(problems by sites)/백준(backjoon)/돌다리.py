import sys
sys.setrecursionlimit(10**5)

a, b, n, m = map(int, input().split())
vi = set()
di = [1,-1,a,b,-a,-b]
min_ans = 1e9
def dfs(now_n,cnt):
    global min_ans,vi,di,a,b
    if cnt > abs(m-n):
        return
    if now_n > m + abs(m-n):
        return
    if now_n == m:
        if min_ans > cnt:
            min_ans = cnt
        return

    vi.add(now_n)
    for d in di:
        next_n = now_n + d

        if next_n not in vi:
            dfs(next_n, cnt+1)


    for i in [a,b]:
        next_n = now_n*i

        if next_n not in vi:
            dfs(next_n, cnt + 1)\


dfs(n,0)
print(min_ans)