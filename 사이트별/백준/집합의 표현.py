import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
parent = dict()

for i in range(n+1):
    parent[i] = i


def find(x, parent):

    if x != parent[x]:
        parent[x] = find(parent[x], parent)

    return parent[x]


def Union(a, b,parent):

    a = find(a, parent)
    b = find(b, parent)

    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

    return

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        if find(a,parent) != find(b,parent):
            Union(a,b,parent)
    else:
        if find(a,parent) != find(b,parent):
            print("NO")
        else:
            print("YES")