from itertools import permutations

n = int(input())
eggs = list()
max_ans = 0

for _ in range(n):
    s, w = map(int, input().split())
    eggs.append([s,w])

def dfs(idx):
    global max_ans

    if idx >= n:
        ans = 0
        for i in eggs:
            if i[0] <= 0:
                ans += 1
        if ans > max_ans:
            max_ans = ans
        return

    if eggs[idx][0] <= 0:
        dfs(idx + 1)
        return

    is_Full = True
    for i in range(n):
        if idx == i:
            continue

        if eggs[i][0] > 0:
            is_Full = False
            break

    if is_Full:
        ans = 0
        for i in eggs:
            if i[0] <= 0:
                ans += 1
        if ans > max_ans:
            max_ans = ans

        return

    for i in range(n):
        if i == idx: continue

        if eggs[i][0] > 0:
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            dfs(idx+1)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]


dfs(0)
print(max_ans)

