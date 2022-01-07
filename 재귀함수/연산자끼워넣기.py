import sys

def dfs(n_list,operators,idx,res,n):
    global max_, min_

    if idx == n-1:
        max_ = max(max_, res)
        min_ = min(min_, res)
        return

    for i in range(len(operators)):
        if operators[i] != 0:
            if i == 0:
                operators[i] -= 1
                dfs(n_list, operators, idx + 1, res + n_list[idx+1], n)
                operators[i] += 1
            elif i == 1:
                operators[i] -= 1
                dfs(n_list, operators, idx + 1, res - n_list[idx+1], n)
                operators[i] += 1
            elif i == 2:
                operators[i] -= 1
                dfs(n_list, operators, idx + 1, res * n_list[idx+1], n)
                operators[i] += 1
            else:
                operators[i] -= 1
                dfs(n_list, operators, idx + 1, int(res / n_list[idx+1]), n)
                operators[i] += 1

n = int(input())
n_list = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))
max_ = -sys.maxsize - 1
min_ = sys.maxsize
idx = 0


dfs(n_list,operators,idx,n_list[0],n)
print(max_)
print(min_)
