from collections import deque

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
vi = set()
cnt = 0


def bfs(vi):
    global cnt
    vi.add(((0, 0), (0, 1)))
    q = deque([(0, 0, 0, 1, vi)])

    while q:
        r1, c1, r2, c2, vi = q.popleft()

        if r1 > r2:
            r1, r2 = r2, r1

        if c1 > c2:
            c1, c2 = c2, c1

        if home[r2][c2] == 0 and r2 == n - 1 and c2 == n - 1:
            cnt += 1
            continue

        if r1 == r2:
            nr1, nc1 = r1, c1 + 1
            nr2, nc2 = r2, c2 + 1
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:

                if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                    q.append((nr1, nc1, nr2, nc2, vi|{((nr1, nc1), (nr2, nc2))}))

            nr1, nc1 = r1, c1 + 1
            nr2, nc2 = r2 + 1, c2 + 1
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
                if home[nr1 + 1][nc1] == 0 and home[nr1][nc1 + 1] == 0:
                    if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                        q.append((nr1, nc1, nr2, nc2,vi|{((nr1, nc1), (nr2, nc2))}))

        elif c1 == c2:
            nr1, nc1 = r1 + 1, c1
            nr2, nc2 = r2 + 1, c2
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
                if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                    q.append((nr1, nc1, nr2, nc2,vi|{((nr1, nc1), (nr2, nc2))}))

            nr1, nc1 = r1 + 1, c1
            nr2, nc2 = r2 + 1, c2 + 1
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
                if home[nr1 + 1][nc1] == 0 and home[nr1][nc1 + 1] == 0:
                    if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                        q.append((nr1, nc1, nr2, nc2,vi|{((nr1, nc1), (nr2, nc2))}))

        else:
            nr1, nc1 = r1 + 1, c1 + 1
            nr2, nc2 = r2, c2 + 1
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
                if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                    q.append((nr1, nc1, nr2, nc2,vi|{((nr1, nc1), (nr2, nc2))}))

            nr1, nc1 = r1 + 1, c1 + 1
            nr2, nc2 = r2 + 1, c2
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
                if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                    q.append((nr1, nc1, nr2, nc2,vi|{((nr1, nc1), (nr2, nc2))}))

            nr1, nc1 = r1 + 1, c1 + 1
            nr2, nc2 = r2 + 1, c2 + 1
            if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n:
                if home[nr1 + 1][nc1] == 0 and home[nr1][nc1 + 1] == 0:
                    if home[nr2][nc2] == 0 and ((nr1, nc1), (nr2, nc2)) not in vi:
                        q.append((nr1, nc1, nr2, nc2,vi|{((nr1, nc1), (nr2, nc2))}))

    return


bfs(vi)
print(cnt)
