from itertools import combinations
from collections import deque

n = int(input())
people_nums = list(map(int, input().split()))
group_graph = [[] for _ in range(n+1)]
orders = range(1,n+1)
group_a = set()
group_b = set()
answer = 1e9

def check_possible(a,b):
    sa = a[0]
    ba = b[0]
    a_vi = [0] * (n + 1)
    b_vi = [0] * (n + 1)
    a_vi[sa] = 1
    q = deque([sa])
    a_len = len(a)
    b_len = len(b)

    while q:
        v = q.popleft()

        for n_v in group_graph[v]:
            if a_vi[n_v] == 0 and n_v in a:
                a_vi[n_v] = 1
                q.append(n_v)

    if sum(a_vi) != a_len:
        return False
    q = deque([ba])
    a_vi[ba] = 1
    while q:
        v = q.popleft()

        for n_v in group_graph[v]:
            if a_vi[n_v] == 0 and n_v in b:
                a_vi[n_v] = 1
                q.append(n_v)

    if sum(a_vi) != (a_len+b_len):
        return False
    return True

for i in range(1,n+1):
    nodes = list(map(int, input().split()))
    for j in range(len(nodes)):
        if j == 0:
            continue
        x = nodes[j]
        group_graph[i].append(x)
        group_graph[x].append(i)

for i in range(1,n):
    for com in combinations(orders,i):
        a = com
        group_a.add(a)

total_set = set(orders)
is_ok = False

for a in group_a:
    a = set(a)
    b = total_set - a
    a = list(a)
    b = list(b)

    if check_possible(a,b):
        sum_a = 0
        sum_b = 0
        for i in a:
            sum_a += people_nums[i-1]

        for i in b:
            sum_b += people_nums[i - 1]

        answer = min(answer,abs(sum_a - sum_b))
        is_ok= True

if is_ok:
    print(answer)
else:
    print(-1)