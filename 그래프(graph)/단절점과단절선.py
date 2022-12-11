import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
node_cnt = defaultdict(int)
edges = []

for _ in range(n-1):
    x,y = map(int, input().split())
    node_cnt[x] += 1
    node_cnt[y] += 1
    edges.append((x,y))

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())

    if t == 1:
        if node_cnt[k] > 1:
            print("yes")
        else:
            print("no")

    else:
        x,y = edges[k-1]
        if node_cnt[x] >= 1 and node_cnt[y] >= 1:
            print("yes")
        else:
            print("no")
