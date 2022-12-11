from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    q = deque([pz])
    while q:
        s = q.popleft()

        if s == '123456780':
            print(visit[s])
            return

        cf = s.find('0')
        x = cf // 3
        y = cf % 3
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                ls = list(s)
                cs = nx * 3 + ny
                ls[cf], ls[cs] = ls[cs], ls[cf]
                ns = ''.join(ls)
                if not visit.get(ns):
                    visit[ns] = visit[s] + 1
                    q.append(ns)

    return -1


pz = ""
for _ in range(3):
    pz += ''.join(list(input().split(' ')))

visit = {pz: 0}

if bfs() == -1:
    print(-1)
