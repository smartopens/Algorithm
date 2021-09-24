from collections import deque


def bfs(x, y, z):
    q = deque([(x, y, z)])

    while q:
        x, y, z = q.popleft()
        if x == 0:
            ans[z] = 1
        if check[x][y] == 1:
            continue
        check[x][y] = 1
        # a->b
        if x + y > b:
            q.append((x + y - b, b, z))
        else:
            q.append((0, x + y, z))
        # b->c
        if y + z > c:
            q.append((x, y + z - c, c))
        else:
            q.append((x, 0, y + z))
        # a->c
        if x + z > c:
            q.append((x + z - c, y, c))
        else:
            q.append((0, y, x + z))
        # c->a
        if x + z > a:
            q.append((a, y, x + z - a))
        else:
            q.append((x + z, y, 0))
        # b->a
        if x + y > a:
            q.append((a, x + y - a, z))
        else:
            q.append((x + y, 0, z))
        # c->b
        if y + z > b:
            q.append((x, b, y + z - b))
        else:
            q.append((x, y + z, 0))


a, b, c = map(int, input().split())
length = max(a, b, c) + 1

check = [[False] * length for _ in range(length)]
ans = [0] * (length)

bfs(0, 0, c)
for i in range(len(ans)):
    if ans[i] == 1:
        print(i, end=' ')
