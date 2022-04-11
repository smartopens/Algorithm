import sys
input = sys.stdin.readline

def check():
    for i in range(n):
        sta = i

        for j in range(h):
            if mArr[j][sta] == 1:
                sta += 1
            elif mArr[j][sta-1] == 1:
                sta -= 1
        if sta != i:
            return 0

    return 1


def dfs(cnt, i):
    global ans

    if check():
        ans = min(ans,cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for r in range(h):
        for c in range(n-1):
            if mArr[r][c] == 1:
                continue
            if c - 1 >= 0 and mArr[r][c - 1] == 1:
                continue
            if c + 1 < n  and mArr[r][c + 1] == 1:
                continue

            mArr[r][c] = 1
            dfs(cnt + 1, i)
            mArr[r][c] = 0


n, m, h = map(int, input().split())
mArr = [[0]*n for _ in range(h)]

for _ in range(m):
    x, y = map(int, input().split())
    mArr[x-1][y-1] = 1

ans = sys.maxsize
dfs(0,0)

print(ans if ans < 4 else -1)


