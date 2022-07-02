import sys
n, k = map(int, input().split())
ans = 0
do_more = True

def dfs(max_case, idx, problem, check):
    global ans
    if max_case == 0:
        tmp = 0
        for string in problem:
            isNotOk = False
            for s in string:
                if check[ord(s) - ord('a')] == 0:
                    isNotOk = True
                    break

            if isNotOk:
                continue
            tmp += 1

        ans = max(ans, tmp)

        return

    for i in range(idx,26):
        if check[i] == 0:
            check[i] = 1
            dfs(max_case - 1, i, problem, check)
            check[i] = 0
    return


if k < 5:
    do_more = False
elif k == 26:
    ans = n
    do_more = False

if do_more:
    max_case = k - 5
    problems = []
    possible = []
    check = [0] * 26

    problems = [set(sys.stdin.readline().rstrip()) for _ in range(n)]

    for i in ["a", "n", "t", "c", "i"]:
        check[ord(i) - ord('a')] = 1
    #    ["a", "n", "t", "c", "i"]
    dfs(max_case
        , 0, problems, check
        )

print(ans)
