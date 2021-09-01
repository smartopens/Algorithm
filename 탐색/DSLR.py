from collections import deque
import sys

input = sys.stdin.readline

test_case = int(input())


def bfs():
    s_result = ""
    q = deque([[x, s_result]])
    visited[x] = True

    while q:
        n, result = q.popleft()

        dn = 2 * n % 10000
        if dn == y:
            return result + "D"
        if not (visited[dn]):
            visited[dn] = True
            q.append([dn, result + "D"])

        sn = n - 1 if n != 0 else 9999
        if sn == y:
            return result + "S"
        if not (visited[sn]):
            visited[sn] = True
            q.append([sn, result + "S"])

        ln = int((n % 1000) * 10 + n / 1000)
        if ln == y:
            return result + "L"
        if not (visited[ln]):
            visited[ln] = True
            q.append([ln, result + "L"])

        rn = int((n / 10) + (n % 10) * 1000)

        if rn == y:
            return result + "R"
        if not (visited[rn]):
            visited[rn] = True
            q.append([rn, result + "R"])


for _ in range(test_case):
    x, y = map(int, input().split())
    visited = [False] * (10000)
    print(bfs())
