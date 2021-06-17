n = int(input())


def checked(x):
    for i in range(x):
        if col[x] == col[i]:
            return False

        if abs(col[x] - col[i]) == x - i:
            return False
    return True


def dfs(x):
    global result
    if x == n:
        result += 1

    else:
        for i in range(n):
            col[x] = i

            if checked(x):
                dfs(x + 1)


row = [0] * n
result = 0
dfs(0)

print(result)
