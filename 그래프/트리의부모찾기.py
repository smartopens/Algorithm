from collections import deque

n = int(input())

tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

tree_p = {}
q = deque([1])

while q:
    parent = q.popleft()

    for child in tree[parent]:
        if not visited[child]:
            tree_p[child] = parent
            visited[child] = True
            q.append(child)

for i in range(2, n + 1):
    print(tree_p.get(i))
