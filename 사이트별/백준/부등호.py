import sys
sys.setrecursionlimit(10**6)

n = int(input())
problem = list(input().split(' '))
case = [0,1,2,3,4,5,6,7,8,9]
vi = [0]*10
ans = []

def dfs(idx,vi,tmp):
    global ans, case, problem

    if idx == len(problem)+1:
        ans.append(tmp)
        return

    for i in range(10):
        if vi[i] == 0:
            if idx == 0:
                vi[i] = 1
                dfs(idx+1,vi,tmp+str(case[i]))
                vi[i] = 0
                continue

            if problem[idx-1] == "<":
                if case[i] > int(tmp[idx-1]):
                    vi[i] = 1
                    dfs(idx+1,vi,tmp+str(case[i]))
                    vi[i] = 0
            elif problem[idx-1] == ">":
                if case[i] < int(tmp[idx-1]):
                    vi[i] = 1
                    dfs(idx+1,vi,tmp+str(case[i]))
                    vi[i] = 0
    return

dfs(0,vi,"")
ans_int = []

for idx, v in enumerate(ans):
    ans_int.append((idx,int(v)))

ans_int.sort(key = lambda x:x[1])
print(ans[ans_int[-1][0]])
print(ans[ans_int[0][0]])